import React from 'react';
import Lottie from 'lottie-react';
import { motion } from 'framer-motion';
import backgroundAnimation from '../Components/loginpages/Assets/Animationred - 1715952238515.json'; // Adjust the path if needed
import logo from './Assets/asl.jpeg';
import logo1 from './Assets/aaaaa.png' // Adjust the path to your logo image if needed
import './landingPage.css';

const LandingPage = ({ history }) => {
    const handleRegisterClick = () => {
        history.push('/register');
    };

    const handleLoginClick = () => {
        history.push('/login');
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
                                Welcome to Fraud Detection
                            </motion.h1>
                            <motion.p
                                initial={{ x: 100 }}
                                animate={{ x: 0 }}
                                transition={{ type: 'spring', stiffness: 100 }}
                            >
                                Protecting your business from fraud with cutting-edge technology.
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
                                    onClick={handleRegisterClick}
                                >
                                    Register
                                </motion.button>
                                <motion.button
                                    whileHover={{ scale: 1.1 }}
                                    whileTap={{ scale: 0.9 }}
                                    onClick={handleLoginClick}
                                >
                                    Login
                                </motion.button>
                            </motion.div>
                        </motion.div>
                    </div>
                </div>
            </div>
            
            
            <img src={logo} alt="Company Logo" className="logo" loading="lazy" />
            <img src={logo1} alt="Company Logo" className="log" loading="lazy" />
    
          
            
         
        </div>
    );
};

export default LandingPage;

