from flask import jsonify, request

from models.LevelModel import Level
from models.UserModel import User
from config import db
import bcrypt


# Fungsi untuk melakukan hash password
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

# Fungsi untuk memverifikasi password
def check_password_hash(hashed_password, user_password):
    return bcrypt.checkpw(user_password.encode('utf-8'), hashed_password.encode('utf-8'))

def login():
    pass

def get_users():
    users = User.query.all()
    users_with_levels = []
    for user in users:
        # Ambil level terkait dari user
        level = Level.query.get(user.level_id)

        # Tambahkan detail user beserta nama level
        users_with_levels.append({
            'user_id': user.user_id,
            'username': user.username,
            'full_name': user.full_name,
            'level_name': level.name if level else "No Level",
            'status': user.status,
        })

    return jsonify(users_with_levels)


def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'status': 'error', 'message': 'User not found'}), 404

    # Ambil level terkait dari user
    level = Level.query.get(user.level_id)

    user_data = {
        'user_id': user.user_id,
        'username': user.username,
        'full_name': user.full_name,
        'status': user.status,
        'level_name': level.name if level else "No Level"
    }

    return jsonify(user_data)


def add_user():
    new_user_data = request.get_json()
    hashed_pw = hash_password(new_user_data['password'])  # Hash password
    import secrets
    api_key = secrets.token_hex(16)
    new_user = User(
        username=new_user_data['username'],
        password=hashed_pw,  # Simpan password yang sudah di-hash
        full_name=new_user_data['full_name'],
        status=new_user_data['status'],
        level_id=new_user_data['level_id'],
        api_key=api_key
    )
    # return jsonify(new_user.to_dict())
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User added successfully!', 'user': new_user.to_dict()}), 201


def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    updated_data = request.get_json()
    user.username = updated_data.get('username', user.username)
    
    if 'password' in updated_data:
        user.password = hash_password(updated_data['password'])  # Hash password baru jika diperbarui
    
    user.full_name = updated_data.get('full_name', user.full_name)
    user.status = updated_data.get('status', user.status)

    db.session.commit()
    return jsonify({'message': 'User updated successfully!', 'user': user.to_dict()})


def patch_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    patch_data = request.get_json()
    if 'username' in patch_data:
        user.username = patch_data['username']
    if 'password' in patch_data:
        user.password = patch_data['password']  # Pastikan untuk mengenkripsi di aplikasi nyata
    if 'full_name' in patch_data:
        user.full_name = patch_data['full_name']
    if 'status' in patch_data:
        user.status = patch_data['status']

    db.session.commit()
    return jsonify({'message': 'User partially updated successfully!', 'user': user.to_dict()})


def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully!'})
