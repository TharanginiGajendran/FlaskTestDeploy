from flask import Blueprint, request, jsonify

from Model.BookModel import DataBase
from Model.BookModel import PostBooks



# create controller with blueprint
post_controller_bp = Blueprint('create_book_api', __name__)


@post_controller_bp.route("/add_books", methods=['POST'])
def create_book():
    my_data = request.get_json()

    new_book = PostBooks(author=my_data['author'], title=my_data['title'], description=my_data['description'])

    if not my_data['author'] or not my_data['title'] or not my_data['description']:
        raise ValueError("Author and Title,Description cannot be empty")

    DataBase.session.add(new_book)
    DataBase.session.commit()

    added_book_details = {
        "id": new_book.id,
        "author": new_book.author,
        "title": new_book.title,
        "description": new_book.description
    }

    response_format = {

        "data": added_book_details
    }

    return jsonify(response_format)
