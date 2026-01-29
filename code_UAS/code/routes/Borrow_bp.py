from flask import Blueprint
from controllers.BorrowController import (
    get_borrows,
    get_borrow,
    add_borrow,
    return_book,
    delete_borrow
)

borrow_bp = Blueprint("borrow_bp", __name__)

borrow_bp.route("/api/borrow", methods=["GET"])(get_borrows)
borrow_bp.route("/api/borrow/<int:borrow_id>", methods=["GET"])(get_borrow)
borrow_bp.route("/api/borrow", methods=["POST"])(add_borrow)
borrow_bp.route("/api/borrow/return/<int:borrow_id>", methods=["PATCH"])(return_book)
borrow_bp.route("/api/borrow/<int:borrow_id>", methods=["DELETE"])(delete_borrow)
