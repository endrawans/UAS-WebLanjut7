from flask import Blueprint
from controllers.CategoryController import get_categories, get_category, add_category, update_category, delete_category

category_bp = Blueprint('Category_bp', __name__)

# Route for getting all category
category_bp.route('/api/category', methods=['GET'])(get_categories)

# Route for getting a specific category
category_bp.route('/api/category/<int:cat_id>', methods=['GET'])(get_category)

# Route for creating add new a category
category_bp.route('/api/category', methods=['POST'])(add_category)

# Route for updating a specific category (PUT)
category_bp.route('/api/category/<int:cat_id>', methods=['PUT'])(update_category)

# Route for deleting a specific category (DELETE)
category_bp.route('/api/category/<int:cat_id>', methods=['DELETE'])(delete_category)
