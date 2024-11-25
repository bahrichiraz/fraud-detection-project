import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

engine = create_engine('mysql+mysqlconnector://bahri_chiraz:wwZYY4s7cmw5@185.2.101.12/geoprod_stage_2024')
data_doss = pd.read_sql_query("SELECT id FROM etat_dossier WHERE classe != 2", engine)
etats = ','.join([f"'{ids}'" for ids in data_doss['id']])

data_tags = pd.read_sql_query("SELECT id_tag , id_affaire FROM affaire_tags WHERE id_tag NOT IN (117, 118 , 120) ", engine)
tg = ','.join([f"'{ids}'" for ids in data_tags['id_affaire']])

data_aff = pd.read_sql_query(f"SELECT id FROM affaire WHERE status IN ({etats}) and id IN ({tg})", engine)
data_aff['Type_fraude'] = 'fake tags'
print (data_aff)

tableau_final = data_aff[['id','Type_fraude']]
# Ajouter la date système
tableau_final['Date_systeme'] = datetime.now()

# Convertir en fichier CSV
tableau_final.to_csv('tableau_final5.csv', index=False)
print(tableau_final)

