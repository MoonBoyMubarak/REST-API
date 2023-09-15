from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///people.db'  # SQLite database URI
db = SQLAlchemy(app)


# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }

# Create the database tables
with app.app_context():
    db.create_all()

# Helper function to check if a value is a valid string
def is_valid_string(value):
    return isinstance(value, str)

# Defining the API endpoints using /api/user/name

# Create a new user
@app.route('/api/user/<name>', methods=['POST'])
def create_user(name):
    # Check if the name is a valid string
    if not is_valid_string(name):
        return jsonify({"error": "Name should be a valid string"}), 400

    user = User(name=name)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User created successfully"}), 201

# Fetching all users
@app.route('/api/users', methods=['GET'])
def get_all_users():
    users = User.query.all()  # Retrieve all user records from the database
    user_list = [user.to_dict() for user in users]  # Convert user objects to dictionaries
    return jsonify(user_list)


# Retrieving a specific user by name
@app.route('/api/user/<name>', methods=['GET'])
def get_user_by_name(name):
    user = User.query.filter_by(name=name).first()
    if user:
        return jsonify(user.to_dict())
    else:
        return jsonify({"message": "User not found"}), 404
    
# Updating a specific user by name
@app.route('/api/user/<name>', methods=['PUT'])
def update_user(name):
    data = request.get_json()
    new_name = data.get('new_name')

    # Error handling and verification : checking  if the new name is a valid string
    if not is_valid_string(new_name):
        return jsonify({"error": "New name should be a valid string"}), 400

    user = User.query.filter_by(name=name).first()
    if user:
        user.name = new_name
        db.session.commit()
        return jsonify({"message": "User updated successfully"})
    else:
        return jsonify({"message": "User not found"}), 404
    
# Deleting a specific user by name
@app.route('/api/user/<name>', methods=['DELETE'])
def delete_user(name):
    user = User.query.filter_by(name=name).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted successfully"})
    else:
        return jsonify({"message": "User not found"}), 404
    
if __name__ == '__main__':
    app.run(debug=True)


