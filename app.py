from flask import Flask,request
app = Flask(__name__)
# defining a route for the home page
@app.route('/')
def home():# below small html ,css code added.that's not necessary if you don't want you just skip that.
    return '<h1 style="color:blue">Welcome to the home page</h1>' 
#defining a rounte for hanling URL parameters
@app.route('/user/<name>')
def user(name):
    return 'Hello {}'.format(name)

#defining a route for handling URL parameters with data type
# integer parameter
@app.route('/user/<int:age>')
def user_age(age):
    return 'Your Age is: {}'.format(age)
# float parameter
@app.route('/user/<float:weight>')
def user_weight(weight):
    return 'Your Weight is: {}'.format(weight)
#defining a route for handling URL parameters with multiple data types
@app.route('/user/<name>/<int:age>/<float:weight>')
def user_info(name, age, weight):
    return '<h1>Hello {}<br>Your Age is: {} <br> Your Weight is: {}</h1>'.format(name, age, weight)

#3. Using HTTP Methods (GET, POST)
from flask import Flask, request

app = Flask(__name__)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'GET':
        return '''
            <form action="/submit" method="POST">
                <label>Name:</label>
                <input type="text" name="name">
                <label>Age:</label>
                <input type="number" name="age">
                <input type="submit" value="Submit">
            </form>
        '''
    elif request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        return f"Hello {name}, your age is {age}!"

# handling CRUD operations
from flask import Flask, request

app = Flask(__name__)

# Sample data (dictionary acting as a database)
users = {
    1: {"name": "Alice", "age": 25},
    2: {"name": "Bob", "age": 30}
}

@app.route('/')
def home():
    return "<h1>Flask CRUD Example</h1>"

# 1️ READ Operation (GET)
@app.route('/users', methods=['GET'])
def get_users():
    result = "<h2>Users List</h2>"
    for user_id, user in users.items():
        result += f"ID: {user_id}, Name: {user['name']}, Age: {user['age']}<br>"
    return result

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    if user_id in users:
        user = users[user_id]
        return f"ID: {user_id}, Name: {user['name']}, Age: {user['age']}"
    return "User not found", 404

# 2️ CREATE Operation (POST)
@app.route('/users/create', methods=['POST'])
def add_user():
    user_id = max(users.keys()) + 1  # Generate a new user ID
    name = request.form['name']
    age = request.form['age']
    users[user_id] = {"name": name, "age": int(age)}
    return f"User {name} added successfully with ID {user_id}!"

# 3️ UPDATE Operation (PUT)
@app.route('/users/update/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id in users:
        data = request.json  # Get JSON data
        name = data.get('name', users[user_id]['name'])
        age = data.get('age', users[user_id]['age'])
        users[user_id] = {"name": name, "age": int(age)}
        return f"User {user_id} updated successfully!"
    return "User not found", 404

# 4 **DELETE Operation (DELETE)**
@app.route('/users/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return f"User {user_id} deleted successfully!"
    return "User not found", 404




if __name__=='__main__':
    app.run(debug=True)


