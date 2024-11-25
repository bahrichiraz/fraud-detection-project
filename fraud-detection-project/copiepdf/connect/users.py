from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:charouz50@localhost/usersdata'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Users {self.email}>'

# Endpoint for user signup
@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    if len(password) < 8:
        return jsonify({'error': 'Password must be at least 8 characters long'}), 400

    # Generate password hash
    password_hash = generate_password_hash(password)

    # Check if the length of the password hash exceeds the column length
    if len(password_hash) > 255:
        return jsonify({'error': 'Password hash exceeds the length limit'}), 500

    if Users.query.filter_by(email=email).first():
        return jsonify({'error': 'Email already exists'}), 400

    new_user = Users(email=email, password_hash=password_hash)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "id":1,
        "email" : email
    }), 201

# Endpoint for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    user = Users.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({'error': 'Invalid email or password'}), 401

    return jsonify({'message': 'Login successful'}), 200

if __name__ == '__main__':
    app.run(port=5000)
