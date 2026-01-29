from flask import request, jsonify
from flask_jwt_extended import create_access_token
from models.UserModel import User
from config import db
import bcrypt

def register():
    data = request.get_json()

    # cek user sudah ada
    if User.query.filter_by(username=data['username']).first():
        return jsonify({"message": "Username already exists"}), 400

    hashed = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())

    user = User(
        username=data['username'],
        password=hashed.decode('utf-8'),  # simpan string
        full_name=data['full_name'],
        status=data['status'],
        level_id=data['level_id']
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201


def login():
    data = request.get_json()

    user = User.query.filter_by(username=data['username']).first()

    if not user:
        return jsonify({"message": "Invalid credentials"}), 401

    if not bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
        return jsonify({"message": "Invalid credentials"}), 401

    token = create_access_token(identity=user.user_id)

    return jsonify({
        "access_token": token,
        "user": {
            "user_id": user.user_id,
            "username": user.username,
            "full_name": user.full_name,
            "level_id": user.level_id,
            "status": user.status
        }
    }), 200
