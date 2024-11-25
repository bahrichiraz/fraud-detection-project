import React, { useState } from "react";
import { FaUser, FaEnvelope } from "react-icons/fa";
import { FaLock } from "react-icons/fa";
import './login.css';
import axios from 'axios';

const Login = () => {
    const [action, setAction] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [alertMessage, setAlertMessage] = useState('');

    const registerLink = () => {
        setAction('active');
    };

    const loginLink = () => {
        setAction('');
    };

    const handleLogin = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('/login', { email, password });
            setAlertMessage('Connexion réussie');
            console.log(response.data);
            // Réinitialiser les champs de formulaire si nécessaire
        } catch (error) {
            setAlertMessage('Erreur lors de la connexion');
            console.error('Erreur lors de la connexion:', error);
        }
    };

    const handleSignup = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('/signup', { email, password });
            setAlertMessage('Inscription réussie');
            console.log(response.data);
            // Réinitialiser les champs de formulaire si nécessaire
        } catch (error) {
            setAlertMessage('Erreur lors de l\'inscription');
            console.error('Erreur lors de l\'inscription:', error);
        }
    };

    return (
        <div className={`wrapper ${action}`}>
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
                        <label>
                            <input type="checkbox" />Remember me
                        </label>
                        <a href="/forgot_password">Mot de passe oublié</a>
                    </div>

                    <button type="submit">Login</button>
                    <div className="register-link">
                        <p>
                            Don't have an account? <a href="#" onClick={registerLink}>Register</a>
                        </p>
                    </div>
                </form>
                {alertMessage && <div className="alert">{alertMessage}</div>}
            </div>

            <div className="form-box inscription">
                <form onSubmit={handleSignup}>
                    <h1>Inscription</h1>
                    <div className="underline"></div>
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

                    <div className="remember-forgot">
                        <label>
                            <input type="checkbox" /> J'accepte les termes et les conditions
                        </label>
                        <a href="#">Mot de passe oublié</a>
                    </div>

                    <button type="submit">S'inscrire</button>
                    <div className="register-link">
                        <p>
                            Already have an account? <a href="#" onClick={loginLink}>Login</a>
                        </p>
                    </div>
                </form>
                {alertMessage && <div className="alert">{alertMessage}</div>}
            </div>
           
        </div>
        
    );
};

export default Login;

