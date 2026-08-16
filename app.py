@app.route('/api')
def get_api_data():
    # Updated content for task 2 requirement
    return jsonify({"status": "success", "version": "2.0_new", "data": "Updated content from the Tutedude_new branch"})

