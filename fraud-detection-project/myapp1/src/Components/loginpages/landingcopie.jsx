import React , { useState } from 'react';
import Lottie from 'lottie-react';
import { motion } from 'framer-motion';
import animationData from './Assets/Animationrobot- 1716287052688.json'; 
import backgroundAnimation from './Assets/Animationred - 1715952238515.json'; 
import logo from './Assets/asl.jpeg';
import logo1 from './Assets/aaaaa.png' 
import './lnd.css'
import Logincopi from './logincopier';

const LandingPage1 = () => {
    const [showLogin, setShowLogin] = useState(false);

    const handleLoginClick1 = () => {
        setShowLogin(true);
        window.scrollTo({
            top: document.body.scrollHeight,
            behavior: 'smooth'
        });
    };

    const handleLoginClick = (e) => {
        e.preventDefault();
        document.getElementById('login-section').scrollIntoView({ behavior: 'smooth' });
    };

    return (
        <div className="landing-page">
            <div className="main-content">
                
                <div className="left-section">
                <Lottie
                  animationData={backgroundAnimation}
                  loop={true}
                  className="animation-container"
                  aria-label="Background Animation"
                />
                </div>
                <div className="right-section">
                    <div className="content">
                        <motion.div
                            className="text-container"
                            initial={{ opacity: 0 }}
                            animate={{ opacity: 1 }}
                            transition={{ duration: 2 }}
                        >
                            <motion.h1
                                initial={{ x: -100 }}
                                animate={{ x: 0 }}
                                transition={{ type: 'spring', stiffness: 100 }}
                            >
                               Bienvenue sur la page d'accueil ! 
                            </motion.h1>
                            <motion.h1
                                initial={{ x: -100 }}
                                animate={{ x: 0 }}
                                transition={{ type: 'spring', stiffness: 100 }}
                            >
                              Notre plateforme est pour l'analyse et détection de fraude
                            </motion.h1>
                            <motion.p
                                initial={{ x: 100 }}
                                animate={{ x: 0 }}
                                transition={{ type: 'spring', stiffness: 100 }}
                            >
                                "Protéger votre entreprise et analyser vos données contre la fraude avec neopolis development."
                            </motion.p>
                            <motion.div
                                className="buttons"
                                initial={{ y: 100 }}
                                animate={{ y: 0 }}
                                transition={{ type: 'spring', stiffness: 100 }}
                            >
                               
                                <motion.button
                                    whileHover={{ scale: 1.1 }}
                                    whileTap={{ scale: 0.9 }}
                                    onClick={handleLoginClick}
                                >
                                    Login / Register
                                </motion.button>
                            </motion.div>
                        </motion.div>
                    </div>
                </div>
            </div>
            <div className="logo-container">
             <img src={logo} alt="Company Logo" className="logo" />
             <img src={logo1} alt="Company Logo" className="log" />
</div>

            
           
            <div className="lottie-container">
                <Lottie animationData={animationData} />
                <h2>Connectez-vous pour accéder à votre tableau de bord</h2>
              
            </div> 

            <div id="login-section" className="login-section">
                <Logincopi />
            </div>
         
        </div>
    );
};



export default LandingPage1;

