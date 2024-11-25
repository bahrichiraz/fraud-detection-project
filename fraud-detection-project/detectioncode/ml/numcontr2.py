import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

# Connexion à la base de données
engine = create_engine('mysql+mysqlconnector://bahri_chiraz:wwZYY4s7cmw5@185.2.101.12/geoprod_stage_2024')

# Sélectionner les IDs des dossiers
data_doss = pd.read_sql_query("SELECT id FROM etat_dossier WHERE classe != 2", engine)
etats = ','.join([f"'{ids}'" for ids in data_doss['id']])

# Filtrer les affaires par status et num_contrat
data_aff = pd.read_sql_query(f"""
    SELECT id 
    FROM affaire 
    WHERE status IN ({etats}) 
    AND num_contrat NOT LIKE 'AE/FS%' 
    AND num_contrat NOT LIKE 'MAA%' 
    AND num_contrat NOT LIKE 'AE/SE%' 
    AND num_contrat NOT LIKE '02ODC228447/%' 
    AND num_contrat NOT LIKE 'ASCAISC%' 
    AND num_contrat NOT LIKE 'AS%' 
    AND num_contrat NOT LIKE 'PREV%' 
    AND num_contrat IS NOT NULL;
""", engine)

# Ajouter une colonne Type_fraude
data_aff['Type_fraude'] = 'faux contrats'

print(data_aff)

# Sélectionner les colonnes pertinentes
tableau_final = data_aff[['id', 'Type_fraude']]

# Ajouter la date système
tableau_final['Date_systeme'] = datetime.now()

# Convertir en fichier CSV
tableau_final.to_csv('tableau_final3.csv', index=False)

print(tableau_final)
