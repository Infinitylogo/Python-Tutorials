from flask import Flask, jsonify, request, abort

app = Flask(__name__)
"""
In Flask (and many other Python frameworks), __name__ is a special variable that 
represents the name of the current module. When you create a Flask application 
instance with app = Flask(__name__), you are essentially telling Flask to use the 
current module as the starting point for the application.
"""

# Sample data (in-memory storage)
books = [
    {'id': 1, 'title': 'Book 1', 'author': 'Author 1'},
    {'id': 2, 'title': 'Book 2', 'author': 'Author 2'}
]

# Helper function to find a book by ID
def find_book(book_id):
    for book in books:
        if book['id'] == book_id:
            return book
    return None

# CRUD routes :-- CRUD is the acronym for CREATE, READ, UPDATE and DELETE.
# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({'books': books})

# Get a single book
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = find_book(book_id)
    if book:
        return jsonify({'book': book})
    else:
        abort(404, f'Book with id {book_id} not found')

# Create a new book
@app.route('/books', methods=['POST'])
def create_book():
    if not request.json or 'title' not in request.json or 'author' not in request.json:
        abort(400, 'Title and Author are required')
    
    new_book = {
        'id': books[-1]['id'] + 1,
        'title': request.json['title'],
        'author': request.json['author']
    }
    books.append(new_book)
    return jsonify({'message': 'Book created successfully', 'book': new_book}), 201

# Update a book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = find_book(book_id)
    if not book:
        abort(404, f'Book with id {book_id} not found')
    
    if not request.json:
        abort(400, 'Request body must be JSON')
    
    # Update book details
    if 'title' in request.json:
        book['title'] = request.json['title']
    if 'author' in request.json:
        book['author'] = request.json['author']
    
    return jsonify({'message': 'Book updated successfully', 'book': book})

# Delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = find_book(book_id)
    if not book:
        abort(404, f'Book with id {book_id} not found')
    
    books.remove(book)
    return jsonify({'message': 'Book deleted successfully', 'book': book})

if __name__ == '__main__':
    app.run(debug=True)



# get details of data :-- curl http://127.0.0.1:5000/books
# get books based on id :-- curl http://127.0.0.1:5000/books/1
# POST :-- curl -X POST -H "Content-Type: application/json" -d '{"title":"New Book","author":"New Author"}' http://127.0.0.1:5000/books

#POST used to add new resource in data  :--  Used to send data to the server to create a new resource.

# PUT used to modify the resources.
#curl -X PUT -H "Content-Type: application/json" -d '{"title":"Updated Title"}' http://127.0.0.1:5000/books/1

#DELETE:-- curl -X DELETE http://127.0.0.1:5000/books/1 :--  Deletes data from the server.