import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt
import joblib
from datetime import datetime

# Connexion à la base de données
def connect_db():
    engine = create_engine('mysql+mysqlconnector://bahri_chiraz:wwZYY4s7cmw5@185.2.101.12/geoprod_stage_2024')
    return engine

def load_data(engine):
  data_doss = pd.read_sql_query("SELECT id FROM etat_dossier WHERE classe != 2", engine)
  etats = ','.join([f"'{ids}'" for ids in data_doss['id']])

  data_aff = pd.read_sql_query(f"SELECT id, date_deff, date_creation FROM affaire WHERE status IN ({etats})", engine)

  data_aff['date_deff'] = pd.to_datetime(data_aff['date_deff'])
  data_aff['date_creation'] = pd.to_datetime(data_aff['date_creation'])

  data_aff['difference'] = (data_aff['date_deff'] - data_aff['date_creation']).dt.days

  result = data_aff[data_aff['difference'] > 4 * 30]  # 4 mois * 30 jours
  if not result.empty:
    result.loc[:, 'Type_fraude'] = "fausse periode pour aesio"
  result_6_months = data_aff[data_aff['difference'] > 6 * 30]  # 6 mois * 30 jours

  if not result_6_months.empty:
    result_6_months.loc[:, 'Type_fraude'] = "fausse periode pour acheel"

# Concaténer les deux résultats
  final_result = pd.concat([result[['id', 'Type_fraude']], result_6_months[['id', 'Type_fraude']]])
  final_result['id_numerique'] = final_result['id'].apply(lambda x: int(x.split('-')[0]))
  return final_result

def scale_features(final_result):
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(final_result[['id_numerique']])
    joblib.dump(scaler, 'scaler.pkl')
    return scaled_features

# Identifier le nombre optimal de clusters en utilisant le graphique du coude
def find_optimal_clusters(scaled_features):
    range_clusters = range(1, 10)
    variances = []
    for n_clusters in range_clusters:
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        kmeans.fit(scaled_features)
        variances.append(kmeans.inertia_)
    
    plt.figure(figsize=(10, 6))
    plt.plot(range_clusters, variances, marker='o')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Variance Explained')
    plt.title('Elbow Plot')
    plt.show()
    
    # Déterminer le nombre optimal de clusters visuellement (ici, 3 pour l'exemple)
    optimal_n_clusters = 3
    return optimal_n_clusters

# Appliquer l'algorithme de clustering K-means
def apply_kmeans(scaled_features, n_clusters):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(scaled_features)
    joblib.dump(kmeans, 'kmeans_model.pkl')

    
    return clusters

# Traiter les nouvelles affaires et mettre à jour les clusters
def process_new_affaires(new_affaires):
    scaled_features = scale_features(new_affaires)
    optimal_n_clusters = find_optimal_clusters(scaled_features)
    clusters = apply_kmeans(scaled_features, optimal_n_clusters)
    new_affaires['cluster'] = clusters
    
    tableau_final = new_affaires[['id', 'Type_fraude', 'cluster']]
    tableau_final['Date_systeme'] = datetime.now()
    tableau_final.to_csv('periode.csv', index=False)
    
    global processed_affair
    processed_affair = pd.concat([processed_affair, new_affaires[['id']]], ignore_index=True)
    
    print(tableau_final)
    return tableau_final

def initialize_processed_affaire():
    if 'processed_affair' not in globals():
        global processed_affair
        processed_affair = pd.DataFrame(columns=['id'])

# Identifier les nouvelles affaires
def identify_new_affaires(final_result):
    new_affaires = final_result[~final_result['id'].isin(processed_affair['id'])]
    return new_affaires

def main():
    engine = connect_db()
    data_aff = load_data(engine)
    initialize_processed_affaire()
    new_affaires = identify_new_affaires(data_aff)
    
    if not new_affaires.empty:
        print(f"Found {len(new_affaires)} new records.")
        tableau_final = process_new_affaires(new_affaires)
    else:
        print("No new records found.")

if __name__ == "__main__":
    main()