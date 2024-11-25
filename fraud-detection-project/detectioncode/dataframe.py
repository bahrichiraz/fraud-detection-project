import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

# Répertoire contenant les fichiers CSV
directory = 'C:\\Users\\chiraz\\Desktop\\mypfe\\detectioncode\\csvfiles'
dfs = []
# Parcourir tous les fichiers dans le répertoire
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        filepath = os.path.join(directory, filename) 
        # Lire le fichier CSV dans un DataFrame
        df = pd.read_csv(filepath)
        # Ajouter le DataFrame à la liste
        dfs.append(df)

# Concaténer tous les DataFrames dans un seul DataFrame
final_table = pd.concat(dfs, ignore_index=True)
final_table.to_csv('fraudes.csv', index=False)

print(final_table)




# Ajouter une colonne pour les classes de fraude
def categorize_fraude(fraude):
    if fraude in ['Faux mca', 'faux numero contrats']:
        return 'top fraude'
    elif fraude in ['Contrat doublant', 'fake tags', 'Faux code postal']:
        return 'moyenne fraude'
    elif fraude in ['fake ville', 'Contrat sans echeancier', 'fausse periode pour aesio', 'fausse periode pour acheel']:
        return 'faible fraude'
    else:
        return 'unknown'

final_table['classe_fraude'] = final_table['type_fraude'].apply(categorize_fraude)

# Encodage des étiquettes
label_encoder = LabelEncoder()
final_table['classe_fraude_encoded'] = label_encoder.fit_transform(final_table['classe_fraude'])

# Préparation des données (ici, nous n'avons pas beaucoup de caractéristiques, donc ajoutons la date comme caractéristique)
final_table['date_system'] = pd.to_datetime(final_table['date_system'])
final_table['year'] = final_table['date_system'].dt.year
final_table['month'] = final_table['date_system'].dt.month
final_table['day'] = final_table['date_system'].dt.day

X = final_table[['year', 'month', 'day']]  # Ajouter d'autres caractéristiques si disponibles
y = final_table['classe_fraude_encoded']

# Normalisation des données
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Séparation des données
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Entraînement du modèle Random Forest
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)

# Prédictions
y_pred = rf_model.predict(X_test)

# Évaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))

# Ajustement des hyperparamètres avec GridSearchCV
param_grid = {'n_estimators': [100, 200, 300], 'max_depth': [None, 10, 20, 30]}
grid = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, refit=True, verbose=2)
grid.fit(X_train, y_train)

# Meilleurs hyperparamètres
print("Best Parameters:", grid.best_params_)

# Prédictions avec le meilleur modèle
best_model = grid.best_estimator_
y_pred_best = best_model.predict(X_test)

# Nouvelle évaluation
print("Accuracy with Best Model:", accuracy_score(y_test, y_pred_best))
print(classification_report(y_test, y_pred_best, target_names=label_encoder.classes_))

# Graphiques
# Répartition des types de fraude
plt.figure(figsize=(10, 6))
sns.countplot(data=final_table, x='type_fraude', order=final_table['type_fraude'].value_counts().index)
plt.title('Répartition des types de fraude')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Matrice de confusion
conf_matrix = confusion_matrix(y_test, y_pred_best)
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=label_encoder.classes_, yticklabels=label_encoder.classes_)
plt.xlabel('Prédictions')
plt.ylabel('Réel')
plt.title('Matrice de confusion')
plt.show()

