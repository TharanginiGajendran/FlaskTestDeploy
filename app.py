from flask import Flask
from flask import Flask

from Contoller.CreateBook import post_controller_bp
from Contoller.GetListOfBooks import get_book_bp
from Model.BookModel import DataBase

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:pythonapi@localhost:3306/test_deploy_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

DataBase.init_app(app=app)

app.register_blueprint(post_controller_bp)
app.register_blueprint(get_book_bp)


if __name__ == "__main__":
    with app.app_context():
        DataBase.create_all()
    app.run(host='0.0.0.0', port=8000, debug=True)
