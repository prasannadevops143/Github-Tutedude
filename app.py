@app.route('/todo')
def todo_page():
    return '''
    <form action="/submittodoitem" method="POST">
        <label for="itemName">Item Name:</label>
        <input type="text" id="itemName" name="itemName" required><br><br>
        <label for="itemDescription">Item Description:</label>
        <textarea id="itemDescription" name="itemDescription" required></textarea><br><br>
        <button type="submit">Submit To-Do</button>
    </form>
    '''
