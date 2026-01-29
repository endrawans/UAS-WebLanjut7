from flask import Blueprint
from controllers.UserController import get_users, get_user, add_user, update_user, patch_user, delete_user

user_bp = Blueprint('User_bp', __name__)

# Route for getting all user
user_bp.route('/api/users', methods=['GET'])(get_users)

# Route for creating a new user
user_bp.route('/api/users', methods=['POST'])(add_user)

# Route for getting a specific user
user_bp.route('/api/users/<int:user_id>', methods=['GET'])(get_user)

# Route for updating a specific user (PATCH)
user_bp.route('/api/users/<int:user_id>', methods=['PATCH'])(update_user)

# Route for updating a specific user (PUT)
user_bp.route('/api/users/<int:user_id>', methods=['PUT'])(patch_user)

# Route for deleting a specific user (DELETE)
user_bp.route('/api/users/<int:user_id>', methods=['DELETE'])(delete_user)
