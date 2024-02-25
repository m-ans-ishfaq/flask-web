from flask import Flask
from controllers.book import book_bp

app = Flask(__name__)

app.register_blueprint(book_bp)

if __name__ == '__main__':
    app.run(port=3000, debug=True)