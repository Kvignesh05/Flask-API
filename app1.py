from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

#Connect to MySQL Database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234", 
    database="flask_db",
)
cursor = db.cursor()

# Home Route
@app.route('/')
def home():
    return "Flask MySQL CRUD API is Running!"

# 1. Create User (POST)
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    query = "INSERT INTO users (name, email) VALUES (%s, %s)"
    values = (data['name'], data['email'])

    cursor.execute(query, values)
    db.commit()

    return jsonify({"message": "User created successfully!", "user_id": cursor.lastrowid})

#  2. Get All Users (GET)
@app.route('/users', methods=['GET'])
def get_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    result = [{"id": u[0], "name": u[1], "email": u[2]} for u in users]

    return jsonify(result)

#  3. Get Single User (GET)
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    query = "SELECT * FROM users WHERE id = %s"
    cursor.execute(query, (id,))
    user = cursor.fetchone()

    if user:
        return jsonify({"id": user[0], "name": user[1], "email": user[2]})
    return jsonify({"error": "User not found"}), 404

# 4. Update User (PUT)
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.json
    query = "UPDATE users SET name = %s, email = %s WHERE id = %s"
    values = (data['name'], data['email'], id)

    cursor.execute(query, values)
    db.commit()

    if cursor.rowcount == 0:
        return jsonify({"error": "User not found"}), 404

    return jsonify({"message": "User updated successfully!"})

#  5. Delete User (DELETE)
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    query = "DELETE FROM users WHERE id = %s"
    cursor.execute(query, (id,))
    db.commit()

    if cursor.rowcount == 0:
        return jsonify({"error": "User not found"}), 404

    return jsonify({"message": "User deleted successfully!"})

#  Run Flask App
if __name__ == '__main__':
    app.run(debug=True)
