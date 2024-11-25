import logging
import random
import string
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Activation de CORS pour toute l'application

# Configuration de la base de données PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:charouz50@localhost/usersdata'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuration de Flask-Mail pour l'envoi d'e-mails
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'benothmenons09@gmail.com'
app.config['MAIL_PASSWORD'] = 'tvmg oqna uzjz etsf'
app.config['MAIL_DEFAULT_SENDER'] = ('Neopolis Development', 'benothmenons09@gmail.com')  

db = SQLAlchemy(app)
mail = Mail(app)

# Configuration des journaux
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class utilisateur(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'schema': 'users_sch'}

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(400), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    nom = db.Column(db.String(100), nullable=False)
    prenom = db.Column(db.String(100))
    role = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='active')
    verification_code = db.Column(db.String(6))

    def __repr__(self):
        return f'<utilisateur {self.email}>'

    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(400), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    nom = db.Column(db.String(100), nullable=False)
    prenom = db.Column(db.String(100))
    role = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='active')
    verification_code = db.Column(db.String(6))

    def __repr__(self):
        return f'<utilisateur {self.email}>'

@app.route('/signup', methods=['POST'])
def signup():
    try:
        data = request.json
        email = data.get('email')
        password = data.get('password')
        nom = data.get('nom')
        prenom = data.get('prenom')

        if not email or not password or not nom or not prenom:
            return jsonify({'error': 'Email, password, nom, and prenom are required'}), 400

        if len(password) < 8:
            return jsonify({'error': 'Password must be at least 8 characters long'}), 400

        password_hash = generate_password_hash(password)

        new_user = utilisateur(email=email, password_hash=password_hash, nom=nom, prenom=prenom, role='responsable')
        db.session.add(new_user)
        db.session.commit()

        return jsonify({
            "id": new_user.id,
            "email": new_user.email,
            "nom": new_user.nom,
            "prenom": new_user.prenom
        }), 201

    except Exception as e:
        db.session.rollback()  # Rollback in case of exception to avoid partial commits
        logger.error(f"Error in signup: {str(e)}")
        return jsonify({'error': 'An error occurred during signup'}), 500

    try:
        data = request.json
        email = data.get('email')
        password = data.get('password')
        nom = data.get('nom')
        prenom = data.get('prenom')

        if not email or not password or not nom or not prenom:
            return jsonify({'error': 'Email, password, nom, and prenom are required'}), 400

        if len(password) < 8:
            return jsonify({'error': 'Password must be at least 8 characters long'}), 400

        password_hash = generate_password_hash(password)

        new_user = utilisateur(email=email, password_hash=password_hash, nom=nom, prenom=prenom, role='responsable')
        db.session.add(new_user)
        db.session.commit()

        return jsonify({
            "id": new_user.id,
            "email": new_user.email,
            "nom": new_user.nom,
            "prenom": new_user.prenom
        }), 201

    except Exception as e:
        db.session.rollback()  # Rollback in case of exception to avoid partial commits
        logger.error(f"Error in signup: {str(e)}")
        return jsonify({'error': 'An error occurred during signup'}), 500


# Route pour la connexion d'un utilisateur
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({'error': 'Email and password are required'}), 400

        user = utilisateur.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password_hash, password):
            return jsonify({'error': 'Invalid email or password'}), 401

        return jsonify({
            'message': 'Login successful',
            'role': user.role
        }), 200
    except Exception as e:
        logger.error(f"Error in login: {str(e)}")
        return jsonify({'error': 'An error occurred during login'}), 500

# Route pour la réinitialisation du mot de passe
@app.route("/forgot_password", methods=["POST"])
def forgot_password():
    try:
        email = request.json.get("email")
        user = utilisateur.query.filter_by(email=email).first()
        
        if user:
            verification_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            user.verification_code = verification_code
            db.session.commit()
            
            send_verification_email(email, verification_code)
            
            return jsonify({"message": "Un code de vérification a été envoyé à votre adresse e-mail."}), 200
        else:
            return jsonify({"error": "Adresse e-mail non trouvée"}), 404
    except Exception as e:
        logger.error(f"Error in forgot_password: {str(e)}")
        return jsonify({'error': 'Une erreur s\'est produite. Veuillez réessayer plus tard.'}), 500

# Fonction pour envoyer un e-mail de vérification
def send_verification_email(email, verification_code):
    try:
        subject = 'Réinitialisation du mot de passe'
        message = f'Voici votre code de vérification pour réinitialiser votre mot de passe : {verification_code}'
        
        msg = Message(subject, recipients=[email], sender=app.config['MAIL_DEFAULT_SENDER'])
        msg.body = message

        mail.send(msg)
    except Exception as e:
        logger.error(f"Error sending verification email: {str(e)}")

# Route pour réinitialiser le mot de passe
@app.route('/ResetPassword', methods=['POST'])
def reset_password():
    try:
        data = request.json
        email = data.get('email')
        verification_code = data.get('verification_code')
        new_password = data.get('new_password')

        user = utilisateur.query.filter_by(email=email, verification_code=verification_code).first()
        
        if user:
            user.password_hash = generate_password_hash(new_password)
            user.verification_code = None  # Suppression du code de vérification après réinitialisation du mot de passe réussie
            db.session.commit()
            
            return jsonify({'message': 'Mot de passe réinitialisé avec succès'}), 200
        else:
            return jsonify({'error': 'Adresse e-mail ou code de vérification incorrect'}), 400
    except Exception as e:
        logger.error(f"Error in reset_password: {str(e)}")
        return jsonify({'error': 'An error occurred during password reset'}), 500

@app.route('/users', methods=['GET'])
def get_users():
    try:
        users = utilisateur.query.filter_by(status='activer').all()
        users_list = [{'id': user.id, 'email': user.email, 'nom': user.nom, 'prenom': user.prenom, 'status': user.status} for user in users]
        return jsonify(users_list), 200
    except Exception as e:
        logger.error(f"Error in get_users: {str(e)}")
        return jsonify({'error': 'An error occurred fetching users'}), 500



# Route pour désactiver un utilisateur par ID
@app.route('/users/<int:id>/disable', methods=['POST'])
def disable_user(id):
    try:
        user = utilisateur.query.get(id)
        
        if not user:
            return jsonify({'error': 'User not found'}), 404

        user.status = 'désactiver'
        db.session.commit()
        
        return jsonify({'message': 'User disabled successfully'}), 200
    except Exception as e:
        logger.error(f"Error in disable_user: {str(e)}")
        return jsonify({'error': 'An error occurred disabling user'}), 500

# Route pour activer un utilisateur par ID
@app.route('/users/<int:id>/activate', methods=['POST'])
def activate_user(id):
    try:
        user = utilisateur.query.get(id)
        
        if not user:
            return jsonify({'error': 'User not found'}), 404

        user.status = 'activer'
        db.session.commit()
        
        return jsonify({'message': 'User activated successfully'}), 200
    except Exception as e:
        logger.error(f"Error in activate_user: {str(e)}")
        return jsonify({'error': 'An error occurred activating user'}), 500

@app.route('/usersDésactiver', methods=['GET'])
def get_disable_users():
    try:
        users = utilisateur.query.filter_by(status='désactiver').all()
        users_list = [{'id': user.id, 'email': user.email, 'nom': user.nom, 'prenom': user.prenom, 'status': user.status} for user in users]
        return jsonify(users_list), 200
    except Exception as e:
        logger.error(f"Error in get_disable_users: {str(e)}")
        return jsonify({'error': 'An error occurred fetching disabled users'}), 500

  


if __name__ == '__main__':
    app.run(port=5000)
