import React, { useState } from 'react';
import SideBar from '../Components/loginpages/navbarhome';
import axios from 'axios';
import './data.css';

const DataPage = () => {
    const [pdfId, setPdfId] = useState('');
    const [fraudCheckResult, setFraudCheckResult] = useState(null);
    const [error, setError] = useState('');

    const handleCheckFraud = async () => {
        try {
            setError(''); // Réinitialiser l'état d'erreur
            if (!pdfId) {
                setError('Veuillez entrer un ID PDF.');
                return;
            }

            console.log('Envoi de la requête de vérification de la fraude pour ID du PDF:', pdfId);
            const response = await axios.post('http://127.0.0.1:5001/check-fraud', { pdfId });
            console.log('Réponse reçue du backend:', response.data);
            setFraudCheckResult(response.data);
        } catch (error) {
            console.error('Erreur lors de la vérification de la fraude:', error.response?.data?.error || error.message);
            setError('Erreur lors de la communication avec le serveur.');
            setFraudCheckResult(null);
        }
    };

    return (
        <div className="dashboard-container">
            <SideBar />
            <div className="main-content">
                <h1>Data Page</h1>
                <form>
                    <label>
                        ID du PDF:
                        <input type="text" value={pdfId} onChange={(e) => setPdfId(e.target.value)} />
                    </label>
                    <button type="button" onClick={handleCheckFraud}>Vérifier la fraude</button>
                </form>
                {error && <p className="error-message">{error}</p>}
                {fraudCheckResult && (
                    <div>
                        <h2>Résultat de la vérification de la fraude:</h2>
                        {fraudCheckResult.success ? (
                            fraudCheckResult.fraud_type === 0 ? (
                                <p>Contrat légal</p>
                            ) : (
                                <div>
                                    <p>Type de fraude: {fraudCheckResult.fraud_type}</p>
                                    <p>Description: {fraudCheckResult.description}</p>
                                </div>
                            )
                        ) : (
                            <p>Erreur: {fraudCheckResult.error}</p>
                        )}
                    </div>
                )}
            </div>
        </div>
    );
};

export default DataPage;

