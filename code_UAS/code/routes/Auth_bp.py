from flask import Blueprint
from controllers.AuthController import login, register

auth_bp = Blueprint('Auth_bp', __name__)

auth_bp.route('/api/register', methods=['POST'])(register)
auth_bp.route('/api/login', methods=['POST'])(login)
