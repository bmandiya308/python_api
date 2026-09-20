from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///api.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    first_sentence = db.Column(db.String(255), nullable=True)
    published = db.Column(db.Integer, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "first_sentence": self.first_sentence,
            "published": self.published,
        }


@app.errorhandler(HTTPException)
def handle_http_exception(error):
    return jsonify({"message": error.description or error.name}), error.code or 500


with app.app_context():
    db.create_all()


@app.route("/getid/<int:id>", methods=["GET", "POST", "PATCH", "DELETE"])
def getdetails(id):
    if request.method == "GET":
        book = Book.query.filter_by(id=id).first()
        if not book:
            return jsonify({"message": f"{id} - is not available"}), 404
        return jsonify(book.to_dict())

    if request.method == "POST":
        if Book.query.filter_by(id=id).first():
            return jsonify({"message": f"{id} - Already Created !"}), 409

        payload = request.get_json(silent=True) or {}
        if not payload:
            return jsonify({"message": "Request body must be JSON"}), 400

        title = payload.get("title")
        author = payload.get("author")
        if not title or not author:
            return jsonify({"message": "title and author are required"}), 400

        book = Book(
            id=id,
            title=title,
            author=author,
            first_sentence=payload.get("first_sentence"),
            published=payload.get("published"),
        )
        db.session.add(book)
        db.session.commit()
        return jsonify(book.to_dict()), 201

    if request.method == "PATCH":
        book = Book.query.filter_by(id=id).first()
        if not book:
            return jsonify({"message": f"{id} - is not available"}), 404

        payload = request.get_json(silent=True) or {}
        if not payload:
            return jsonify({"message": "Request body must be JSON"}), 400

        if "title" in payload and payload["title"] is not None:
            book.title = payload["title"]
        if "author" in payload and payload["author"] is not None:
            book.author = payload["author"]
        if "first_sentence" in payload and payload["first_sentence"] is not None:
            book.first_sentence = payload["first_sentence"]
        if "published" in payload and payload["published"] is not None:
            book.published = payload["published"]

        db.session.commit()
        return jsonify(book.to_dict())

    if request.method == "DELETE":
        book = Book.query.filter_by(id=id).first()
        if not book:
            return jsonify({"message": f"{id} - Not available so cant delete"}), 404

        db.session.delete(book)
        db.session.commit()
        return jsonify({"message": f"Book {id} deleted", "id": id})

    return jsonify({"message": "Method not allowed"}), 405


if __name__ == "__main__":
    import logging

    logging.basicConfig(filename="error.log", format="%(asctime)s - %(message)s", level=logging.INFO)
    app.run(host="0.0.0.0", debug=True)
