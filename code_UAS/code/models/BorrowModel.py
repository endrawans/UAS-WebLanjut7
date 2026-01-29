from config import db
from datetime import datetime

class Borrow(db.Model):
    __tablename__ = "borrow"

    borrow_id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)

    borrow_date = db.Column(db.DateTime, default=datetime.utcnow)
    return_date = db.Column(db.DateTime, nullable=True)

    status = db.Column(db.String(20), default="borrowed")
    # borrowed | returned | late

    def to_dict(self):
        return {
            "borrow_id": self.borrow_id,
            "user_id": self.user_id,
            "book_id": self.book_id,
            "borrow_date": self.borrow_date,
            "return_date": self.return_date,
            "status": self.status
        }