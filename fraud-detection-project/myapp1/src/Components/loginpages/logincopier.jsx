import React, { useState } from 'react';
import { FaUser, FaEnvelope, FaLock, FaCheckCircle, FaExclamationCircle } from 'react-icons/fa';
import './login.css';
import axios from 'axios';
import { useNavigate,Link } from 'react-router-dom';

const Logincopi = () => {
    const [action, setAction] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [prenom, setFirstName] = useState(''); // State for first name
    const [nom, setLastName] = useState('');   // State for last name
    const [alertMessage, setAlertMessage] = useState('');
    const [alertType, setAlertType] = useState('');

    const navigate = useNavigate();

    const registerLink = (e) => {
        e.preventDefault();
        setAction('active');
    };

    const switchToLogin = (e) => {
        e.preventDefault();
        setAction('login');
    };

    const showAlert = (message, type) => {
        setAlertMessage(message);
        setAlertType(type);

        setTimeout(() => {
            setAlertMessage('');
            setAlertType('');
        }, 2000);
    };

    const handleLogin = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('/login', { email, password });
            showAlert('Connexion réussie', 'success');
            console.log(response.data);

            // Stocker le rôle et le token dans le localStorage
            localStorage.setItem('accessToken', response.data.token);
            localStorage.setItem('userRole', response.data.role);
            
            navigate('/home');
        } catch (error) {
            showAlert('Erreur lors de la connexion', 'error');
            console.error('Erreur lors de la connexion:', error);
        }
    };

    const handleSignup = async (e) => {
        e.preventDefault();
        if (password !== confirmPassword) {
            showAlert('Les mots de passe ne correspondent pas', 'error');
            return;
        }
        try {
            const response = await axios.post('/signup', {
                email,
                password,
                prenom,
                nom,
            });
            showAlert('Inscription réussie', 'success');
            console.log(response.data);
        } catch (error) {
            showAlert("Erreur lors de l'inscription", 'error');
            console.error("Erreur lors de l'inscription:", error);
        }
    };

    return (
        <div className="login-container">
            <div className={`wrapper ${action}`}>
                <div className="alert-container">
                    {alertMessage && (
                        <div className={`alert ${alertType}`}>
                            {alertType === 'success' && (
                                <FaCheckCircle className="alert-icon success-icon" />
                            )}
                            {alertType === 'error' && (
                                <FaExclamationCircle className="alert-icon error-icon" />
                            )}
                            <span className="alert-text">{alertMessage}</span>
                        </div>
                    )}
                </div>
                <div className="form-box login">
                    <form onSubmit={handleLogin}>
                        <h1>Connexion</h1>
                        <div className="underline"></div>
                        <div className="input-box">
                            <input
                                type="text"
                                placeholder="Email"
                                value={email}
                                onChange={(e) => setEmail(e.target.value)}
                                required
                            />
                            <FaUser className="icon" />
                        </div>

                        <div className="input-box">
                            <input
                                type="password"
                                placeholder="Password"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                                required
                            />
                            <FaLock className="icon" />
                        </div>

                        <div className="remember-forgot">
                           
                           < Link to="/forgot_password">Mot de passe oublié</Link>
                        </div>

                        <button type="submit">Connecter</button>
                        <div className="register-link">
                            <p>
                                Vous n'avez pas de compte ?{' '}
                                <a href="#" onClick={registerLink}>
                                    Registre
                                </a>
                            </p>
                        </div>
                    </form>
                </div>

                <div className="form-box inscription">
                    <form onSubmit={handleSignup}>
                        <h1>Inscription</h1>
                        <div className="underline"></div>
                        <div className="input-box">
                            <input style={{width:"100%"}}
                                type="text"
                                placeholder="Prénom"
                                value={prenom}
                                onChange={(e) => setFirstName(e.target.value)}
                                required
                            />
                            <FaUser className="icon" />
                        </div>

                        <div className="input-box">
                            <input
                                type="text"
                                placeholder="Nom"
                                value={nom}
                                onChange={(e) => setLastName(e.target.value)}
                                required
                            />
                            <FaUser className="icon" />
                        </div>

                        <div className="input-box">
                            <input
                                type="text"
                                placeholder="Email"
                                value={email}
                                onChange={(e) => setEmail(e.target.value)}
                                required
                            />
                            <FaEnvelope className="icon" />
                        </div>

                        <div className="input-box">
                            <input
                                type="password"
                                placeholder="Password"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                                required
                            />
                            <FaLock className="icon" />
                        </div>

                        <div className="input-box">
                            <input
                                type="password"
                                placeholder="Confirm Password"
                                value={confirmPassword}
                                onChange={(e) => setConfirmPassword(e.target.value)}
                                required
                            />
                            <FaLock className="icon" />
                        </div>

                        <div className="remember-forgot">
                            <button type="submit">S'inscrire</button>
                        </div>
                        <div className="register-link">
                            <p>
                                Vous avez déjà un compte?{' '}
                                <a href="#" onClick={switchToLogin}>
                                    Login
                                </a>
                            </p>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    );
};

export default Logincopi;
