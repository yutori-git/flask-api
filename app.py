from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__) #create a flask instance

CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///memo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Memo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)


#create database(only for the first time)
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return "Hello, Flask is running on Render!"

#GET
@app.route("/api/memos", methods=["GET"])
def get_memos():
    memos = Memo.query.all()
    return jsonify([{"id": memo.id, "content": memo.content} for memo in memos])

#POST
@app.route("/api/memos", methods=["POST"])
def add_memo():
    data = request.json
    new_memo = Memo(content=data["content"])
    db.session.add(new_memo)
    db.session.commit()
    return jsonify({"message": "The memo was added successfully!", "id": new_memo.id, "content": new_memo.content}), 201


#DELETE
@app.route("/api/memos/<int:memo_id>", methods=["DELETE"])
def delete_memo(memo_id):
    memo = db.session.get(Memo, memo_id)
    if memo:
        db.session.delete(memo)
        db.session.commit()
        return jsonify({"message": f"The memo with ID {memo_id} has been deleted successfully"})
    return jsonify({"message": f"The memo with ID {memo_id} was not found"}), 404

#PUT
@app.route("/api/memos/<int:memo_id>", methods=["PUT"])
def update_memo(memo_id):
    data = request.json
    memo = db.session.get(Memo, memo_id)
    if memo:
        memo.content = data["content"]
        db.session.commit()
        return jsonify({"message": "The memo has been updated successfully"})
    return jsonify({"message": f"The memo with ID {memo_id} was not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)

