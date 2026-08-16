from flask import request
from pymongo import MongoClient

# Initialize connection to MongoDB (running locally on standard port 27017)
mongo_client = MongoClient("mongodb://localhost:27017/")
db = mongo_client["todo_assignment_db"]
collection = db["todo_items"]

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    item_name = request.form.get('itemName')
    item_description = request.form.get('itemDescription')

    if not item_name or not item_description:
        return jsonify({"status": "error", "message": "Missing input data fields"}), 400

    # Insert document payload inside MongoDB collection
    todo_doc = {"itemName": item_name, "itemDescription": item_description}
    collection.insert_one(todo_doc)

    return jsonify({"status": "success", "message": "To-Do item successfully recorded in MongoDB"})



