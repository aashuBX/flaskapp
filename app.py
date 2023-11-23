# from flask import Flask, request, jsonify

# app  = Flask(__name__)
# from flask_sqlalchemy import SQLAlchemy

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:adminadmin@flask.c9koygdtikwy.ap-south-1.rds.amazonaws.com:3306/flask'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# book_list = [
#     {
#         "id": 1,
#         "title": "Pride and Prejudice",
#         "author": "Jane Austen"
#     },
#     {
#         "id": 2,
#         "title": "The Lord of the Rings",
#         "author": "J.R.R. Tolkien"
#     },
#     {
#         "id": 3,
#         "title": "Harry Potter and the Sorcerer's Stone",
#         "author": "J.K. Rowling"
#     },
#     {
#         "id": 4,
#         "title": "The Book Thief",
#         "author": "Markus Zusak"
#     },
#     {
#         "id": 5,
#         "title": "To Kill a Mockingbird",
#         "author": "Harper Lee"
#     }
# ]


# @app.route('/books', methods=['GET', 'POST'])
# def books():
#     if request.method == 'GET':
#         if len(book_list) > 0:
#             return jsonify(book_list)
#         else:
#             "No books found", 404
            
#     if request.method == 'POST':
#         print("step 1")
#         new_author = request.form['author']
#         new_title = request.form['title']
#         id = book_list[-1]['id'] + 1
#         print("step 2 ", new_author)
#         print("step 3 ", new_title)
#         new_obj = {
#             "id":id,
#             "title": new_title,
#             "author": new_author
#         }
#         book_list.append(new_obj)
#         return jsonify(book_list)
    

# @app.route('/books/<int:id>', methods=['GET'])
# def single_book(id):
#     if request.method  == 'GET':
#         for book in book_list:
#             if book['id'] == id:
#                 return jsonify(book)
#             pass
        
    
# if __name__ == '__main__':
#     app.run(debug=True)
    

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:adminadmin@flask-db.c9koygdtikwy.ap-south-1.rds.amazonaws.com/flaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)

with app.app_context():
    db.create_all()
    
    # db.session.add(Book(title='Book 1', author='Author 1'))
    # db.session.add(Book(title='Book 2', author='Author 2'))
    # db.session.commit()

@app.route("/books", methods=['GET'])
def get_book():
    books = Book.query.all()
    book_list = [{'title': book.title, 'author': book.author} for book in books]
    return jsonify({'books': book_list})

@app.route('/book-add',methods=['POST'])
def book_add():
    data = request.get_json()
    new_book = Book(title=data['title'], author=data['author'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book added successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    