from flask_sqlalchemy import SQLAlchemy

DataBase = SQLAlchemy()


class PostBooks(DataBase.Model):

    __tablename__ = 'tbl_post_books'

    id = DataBase.Column(DataBase.Integer, primary_key=True)
    author = DataBase.Column(DataBase.String(225), nullable=False)
    title = DataBase.Column(DataBase.String(225), nullable=False)
    description = DataBase.Column(DataBase.String(255), nullable=False)
