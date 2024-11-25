import React, { useState } from 'react';
import SideBar from './navbarhome';
import { Form, Input, Button, Card } from 'antd';
import { color, motion } from 'framer-motion';
import './fakedata.css'; // Assurez-vous que le chemin est correct
import { redirect } from 'react-router-dom';

const FakeDataPage = () => {
    const [pdfId, setPdfId] = useState('19710569.258');
    const [fraudType, setFraudType] = useState('Faux numéro de contrat');

    const handleCheckFraud = () => {
        // Fonctionnalité de vérification de la fraude ici (simulation pour l'exemple)
        setPdfId('19710569.258');
        setFraudType('Faux numéro de contrat');
    };

    return (
        <div className="fake-data-container">
            <SideBar />

            <div className="title-container">
                <h1>Chercher les Données Factices</h1>
            </div>

            <Form className="form-container">
            <Form.Item label="ID du PDF" style={{ color: 'blue', fontWeight: 'bold' }}>
    <Input value={pdfId} readOnly />
</Form.Item>

                  
                <Form.Item>
                    <Button style={{ color: 'red', fontWeight: 'bold', width: '300px' }} >
                        Vérifier la fraude
                    </Button>
                </Form.Item>
            </Form>

            <Card className="result-card">
                <h2>Résultat de la vérification</h2>
                <p>ID de PDF: {pdfId}</p>
                <p>Type de fraude: {fraudType}</p>
            </Card>

            <motion.h1
                initial={{ x: -100 }}
                animate={{ x: 0 }}
                transition={{ type: 'spring', stiffness: 100 }}
                className="animated-info"
            >
                Id de contrat : {pdfId}
            </motion.h1>

            <motion.h1
                initial={{ x: -100 }}
                animate={{ x: 0 }}
                transition={{ type: 'spring', stiffness: 100 }}
                className="animated-info"
            >
                Type de fraude : {fraudType}
            </motion.h1>
        </div>
    );
};

export default FakeDataPage;





