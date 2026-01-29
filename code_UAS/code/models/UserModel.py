import enum
import bcrypt
from config import db


class StatusEnum(enum.Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'


class User(db.Model):
    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)

    # perbesar
    password = db.Column(db.String(255), nullable=False)

    full_name = db.Column(db.String(100), nullable=False)

    status = db.Column(db.Enum(StatusEnum), nullable=False)

    api_key = db.Column(db.Text, nullable=True)

    level_id = db.Column(db.Integer, db.ForeignKey('level.id'), nullable=False)

    borrows = db.relationship("Borrow", backref="user", lazy=True)

    # 🔥 AUTO HASH
    def set_password(self, password):
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.password = hashed.decode('utf-8')

    # 🔥 CHECK PASSWORD
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            'full_name': self.full_name,
            'level_id': self.level_id,
            'status': self.status.value
        }
