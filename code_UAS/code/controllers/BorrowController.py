from flask import jsonify, request
from models.BorrowModel import Borrow
from models.BookModel import Book
from models.UserModel import User
from config import db
from flask_jwt_extended import jwt_required
from datetime import datetime

@jwt_required()
def get_borrows():
    borrows = Borrow.query.all()
    borrows_with_details = []
    for borrow in borrows:
        book = Book.query.get(borrow.book_id)
        user = User.query.get(borrow.user_id)
        borrows_with_details.append({
            'id': borrow.id,
            'book_title': book.title if book else "Unknown",
            'user_name': user.full_name if user else "Unknown",
            'borrow_date': borrow.borrow_date.isoformat(),
            'return_date': borrow.return_date.isoformat() if borrow.return_date else None
        })
    return jsonify(borrows_with_details)

def get_borrow(borrow_id):
    borrow = Borrow.query.get(borrow_id)
    if not borrow:
        return jsonify({'error': 'Borrow not found'}), 404
    book = Book.query.get(borrow.book_id)
    user = User.query.get(borrow.user_id)
    borrow_data = {
        'id': borrow.id,
        'book_title': book.title if book else "Unknown",
        'user_name': user.full_name if user else "Unknown",
        'borrow_date': borrow.borrow_date.isoformat(),
        'return_date': borrow.return_date.isoformat() if borrow.return_date else None
    }
    return jsonify(borrow_data)

def add_borrow():
    new_borrow_data = request.get_json()
    new_borrow = Borrow(
        book_id=new_borrow_data['book_id'],
        user_id=new_borrow_data['user_id'],
        borrow_date=datetime.fromisoformat(new_borrow_data['borrow_date']),
        return_date=datetime.fromisoformat(new_borrow_data['return_date']) if new_borrow_data.get('return_date') else None
    )
    db.session.add(new_borrow)
    db.session.commit()
    return jsonify({'message': 'Borrow added successfully!', 'borrow': new_borrow.to_dict()}), 201

def update_borrow(borrow_id):
    borrow = Borrow.query.get(borrow_id)
    if not borrow:
        return jsonify({'error': 'Borrow not found'}), 404

    updated_data = request.get_json()
    if 'return_date' in updated_data:
        borrow.return_date = datetime.fromisoformat(updated_data['return_date'])

    db.session.commit()
    return jsonify({'message': 'Borrow updated successfully!', 'borrow': borrow.to_dict()})

def delete_borrow(borrow_id):
    borrow = Borrow.query.get(borrow_id)
    if not borrow:
        return jsonify({'error': 'Borrow not found'}), 404

    db.session.delete(borrow)
    db.session.commit()
    return jsonify({'message': 'Borrow deleted successfully!'})
