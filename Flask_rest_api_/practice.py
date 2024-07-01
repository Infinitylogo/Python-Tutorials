from flask import jsonify, Flask, request, abort

app = Flask(__name__)

books = [
    {
        "id": 1,
        "author": "rituraj",
        "title": "Never Give Up"
    },
    {
        "id": 2,
        "author": "rituraj",
        "title": "Never Give Up again"
    }
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({'books': books})

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Function to find a book by book ID
def check_book_by_id(book_id):
    return next((book for book in books if book['id'] == book_id), None)

# Function to find a book by author's name
def check_book_by_author(author):
    return next((book for book in books if book['author'] == author), None)

# Route to get a single book by book ID
@app.route('/books/<int:id>', methods=["GET"])
def get_single_book_by_id(id):
    book = check_book_by_id(id)
    if book:
        return jsonify({'book': book})
    else:
        abort(404, f"Book with id {id} not found")

# Route to get a single book by author's name
@app.route('/books/<string:author>', methods=["GET"])
def get_single_book_by_author(author):
    book = check_book_by_author(author)
    if book:
        return jsonify({'book': book})
    else:
        abort(404, f"Book by author '{author}' not found")


# create new resources or book in present db.
@app.route('/books', methods=['POST'])
def create_book():
    print(request.json)
    if not request.json or 'title' not in request.json or not 'author' in request.json:
        abort(400, f'title and author are required')

    new_book_dict = {
        'id':books[-1]['id']+1,
        'title':request.json['title'],
        'author':request.json['author']
    }
    books.append(new_book_dict)
    return jsonify({'message': 'book created successfully', 'book':new_book_dict}), 201

if __name__ == '__main__':
    app.run(debug=True)
