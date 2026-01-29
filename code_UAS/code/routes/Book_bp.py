from flask import Blueprint
from controllers.BookController import get_books, get_book, add_book, update_book, patch_book, delete_book

book_bp = Blueprint('Book_bp', __name__)

# Route for getting all books
book_bp.route('/api/books', methods=['GET'])(get_books)

# Route for getting a specific book
book_bp.route('/api/books/<int:book_id>', methods=['GET'])(get_book)

# Route for creating add new a book
book_bp.route('/api/books', methods=['POST'])(add_book)

# Route for updating a specific book (PATCH)
book_bp.route('/api/books/<int:book_id>', methods=['PATCH'])(update_book)

# Route for updating a specific book (PUT)
book_bp.route('/api/books/<int:book_id>', methods=['PUT'])(patch_book)

# Route for deleting a specific book (DELETE)
book_bp.route('/api/books/<int:book_id>', methods=['DELETE'])(delete_book)
