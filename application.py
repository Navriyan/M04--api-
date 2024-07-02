from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data2.db"
db = SQLAlchemy(app)

@app.route('/')
def index():
    return "Hello!"



@app.route('/books')
def get_books():
    books = Book.query.all()
    output = []

    for book in books:
        book_data = {'id': book.id,'book_name': book.book_name,'author':book.author, 'publisher': book.publisher }
        output.append(book_data)
    return {"books": output}

@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {"id": book.id,"book_name": book.book_name,"author":book.author, "publisher": book.publisher}







class Book(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    book_name = db.Column(db.String(80),unique=True,nullable=False)
    author = db.Column(db.String(120))
    publisher = db.Column(db.String(120))
    
    def __repr__(self):
        return f"{self.id} - {self.book_name } - {self.author} - {self.publisher}" 

