from flask import Blueprint
from controllers.LevelController import get_levels, get_level, add_level, update_level, delete_level

level_bp = Blueprint('Level_bp', __name__)

# Route for getting all level
level_bp.route('/api/level', methods=['GET'])(get_levels)

# Route for getting a specific level
level_bp.route('/api/level/<int:level_id>', methods=['GET'])(get_level)

# Route for creating add new a level
level_bp.route('/api/level', methods=['POST'])(add_level)

# Route for updating a specific level (PUT)
level_bp.route('/api/level/<int:level_id>', methods=['PUT'])(update_level)

# Route for deleting a specific level (DELETE)
level_bp.route('/api/level/<int:level_id>', methods=['DELETE'])(delete_level)
