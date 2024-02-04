from flask import Flask,jsonify,Blueprint,request
from flask_sqlalchemy import SQLAlchemy
from Model.BookModel import DataBase
from Model.BookModel import PostBooks


# create controller register
# get_book_bp = Blueprint("get_book_api",__name__)

get_book_bp = Blueprint("get_book_api", __name__, url_prefix='/api')

@get_book_bp.route('/get_books',methods=['GET'])
def get_books():
    books = PostBooks.query.all()
    list_of_books = [{"id":book.id,"author":book.author,"title":book.title,"description":book.description} for book in books]
    return jsonify(list_of_books)

