from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import os
import logging

# Importer les fonctions des fichiers de vérification de fraude
from compte_client import extract_data_after_keyword
from formul import extract_data_after_keyword
from num_contrat import is_contract_number_present

# Configuration du logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Charger le fichier Excel une fois lors du démarrage de l'application
try:
    df = pd.read_excel("C:\\Users\\chiraz\\Downloads\\output.xlsx")
    logging.info("Fichier Excel chargé avec succès.")
    logging.info("Contenu du DataFrame : %s", df.head())
except Exception as e:
    logging.error("Erreur lors du chargement du fichier Excel: %s", e)
    df = None
def get_pdf_path_from_id(pdf_id):
    if df is not None:
        row = df[df['id_affaire'].apply(lambda x: pdf_id in x)]
        if not row.empty:
            url = row.iloc[0]['url']
            pdf_path = url.split('/')[-1]  
            logging.info(f"Chemin PDF trouvé: {pdf_path}")
            return pdf_path
              
        logging.warning("Aucun chemin PDF trouvé pour l'ID: %s", pdf_id)
    else:
        logging.error("Le DataFrame est vide ou non chargé.")
    return None



@app.route('/check-fraud', methods=['POST'])
def check_fraud():
    try:
        logging.info("Requête reçue à /check-fraud")
        data = request.json
        pdf_id = data.get('pdfId')
        logging.info(f"ID PDF reçu: {pdf_id}")
        if not pdf_id:
            logging.warning("Aucun ID PDF fourni dans la requête.")
            return jsonify({'success': False, 'error': 'Aucun ID PDF fourni'})

        pdf_path = get_pdf_path_from_id(pdf_id)
        logging.info(f"Chemin PDF trouvé: {pdf_path}")
        
        if not pdf_path or not os.path.exists(pdf_path):
            logging.warning("PDF non trouvé pour l'ID: %s", pdf_id)
            return jsonify({'success': False, 'error': 'PDF non trouvé'})

        logging.info("Vérification de la fraude pour le PDF: %s", pdf_path)

        # Vérification de la fraude pour les trois types
        compte_client_fraud, compte_client_desc = extract_data_after_keyword(pdf_path)
        formul_fraud, formul_desc = extract_data_after_keyword(pdf_path)
        numero_contrat_fraud, numero_contrat_desc = is_contract_number_present(pdf_path)

        # Déterminer le type de fraude
        if compte_client_fraud:
            fraud_type = 1
            description = compte_client_desc
            logging.info("Fraude détectée: Type 1 - %s", description)
        elif formul_fraud:
            fraud_type = 2
            description = formul_desc
            logging.info("Fraude détectée: Type 2 - %s", description)
        elif numero_contrat_fraud:
            fraud_type = 3
            description = numero_contrat_desc
            logging.info("Fraude détectée: Type 3 - %s", description)
        else:
            fraud_type = 0
            description = 'Contrat légal'
            logging.info("Aucune fraude détectée, contrat légal.")

        return jsonify({'success': True, 'fraud_type': fraud_type, 'description': description})
    except Exception as e:
        logging.error("Erreur lors de la vérification de la fraude: %s", e)
        return jsonify({'success': False, 'error': str(e)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)



