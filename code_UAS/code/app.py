from config import app, db
from routes.Book_bp import book_bp
from routes.Category_bp import category_bp
from routes.Level_bp import level_bp
from routes.User_bp import user_bp
from routes.Auth_bp import auth_bp
from routes.Borrow_bp import borrow_bp
from flasgger import Swagger


# register blueprint
app.register_blueprint(book_bp)
app.register_blueprint(category_bp)
app.register_blueprint(user_bp)
app.register_blueprint(level_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(borrow_bp)

@app.route('/')
def index():
    db.create_all()
    return 'API Flask JWT Ready'


if __name__ == '__main__':
    app.run(debug=True)
