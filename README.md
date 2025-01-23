# Ce projet consiste à : 
• Développer des systèmes efficaces d’analyse de données pour détecter la fraude dans les bases de données des contrats d’assurance. \
• Utiliser Python pour l’extraction et l’analyse des données afin de garantir une détection précise des situations anormales telles que des erreurs de numéro de contrat. \
• Intégrez Talend pourla gestion et le filtrage des tables de données afin de garantir un fonctionnement efficace des informations dans les entrepôts de données structurés. \
• Utilisez Power BI pour visualiser les résultats et fournir des tableaux de bord interactifs pour mieux comprendre les modèles de fraude. \
• Développez une application Web pour une interaction utilisateur intuitive, y compris des fonctionnalités avancées telles que l’analyse PDF et les alertes de détection de fraude. 

# Technologies et Outils Utilisées : 
- **Python** : Outil principal utilisé pour la création du tableau de bord interactif et la visualisation des données.
- **Flask** : Flask est un micro framework libre développé en Python.
- **Talend** : logiciel de transformation et de chargement (ETL) qui permet d’extraire des données d’une source, de les modifier, puis de les recharger vers un endroit spécifique.
- **DBeaver** outil de base de donnéesuniversel, gratuit et open source pour les développeurs et les administrateurs de bases de données.
- **Power BI** : Outil principal utilisé pour la création du tableau de bord interactif et la visualisation des données.
- **DAX** : Langage de calcul utilisé pour créer des mesures avancées et des KPIs.
- **CSV** : Utilisé pour la préparation des données DES FRAUDES avant leur traitement dans Power BI.
- **PostgreSQL** Système de gestion de base de données relationnelle orienté objet.
- **React**  est une bibliothèque JavaScript frontale à code source ouvert qui permet deconcevoir desinterfaces utilisateur ou des éléments d’interface utilisateur.

# l’Analyse de Données des fraudes à partir d’une base de donnée :

 ### **1. Compréhension des activités :**
 - Les affaires avec faux numéro de contrat
 - Les affaires sans échéancier
 - Modification de chiffre d’affaires annuelle ...
### **2. Compréhension des données :**
La compréhension des données revêt une importance capitale pour tout projet de data mining. Elle implique de faire une exploration et une compréhension des données disponibles, de repérer les variables essentielles et de préparer les données pour une analyse prochaine.
### **3. Application de l’algorithme k-means :**
K-means est un algorithme de clustering non hiérarchique et non supervisé. L’algorithme k-Meansestunetechniquedeclustering largement utilisée en machine learning pour partitionner un ensemble de données en un nombre fixe de clusters.
**Initialisation** : Choisir k points aléatoirement parmi les données comme centres initiaux des clusters (centroïdes). 
**Assignation** : Attribuer chaque point de données au centroïde le plus proche en utilisant une mesure de distance (souvent la distance euclidienne).
**Mise à jour** : Recalculer les centroïdes en prenant la moyenne des points assignés à chaque cluster.
**Répétition** : Répéter les étapes d’assignation et de mise à jour jusqu’à ce que les centroïdes ne changent plus de manière significative, ou qu’un nombre maximum d’itérations soit atteint. \
1. Le graphique du coude : présente une explication de la variance en fonction du nombre de clusters, ce qui permet de déterminer le nombre optimal de clusters. \
   \
![Capture1](https://github.com/user-attachments/assets/3c896896-a5bb-41c2-b0b4-43319affca0b)
3. Nuage de points des clusters :Les points des clusters sont regroupés dans un nuage de points, chaque point étant coloré en fonction de son cluster. \
\
![Capture2](https://github.com/user-attachments/assets/4921fb89-d48c-449b-8cc3-425ada0e7bef)
### **4. Bibliothèques Utilisées :**
- Pandas : utilisée pour la manipulation et l’analyse des données.
- Scikit-Learn : met à disposition de simples outils performants pour l’analyse de données et l’analyse automatique.
- Numpy:Uneextension Python pour les calculs scientifiques.
- Matplotlib : Conçuepourreprésenter visuellement les données, offrant la possibilité de concevoir des graphiques et des visualisations de grande qualité.
# l’Analyse de Données des fraudes dans les Contrats PDF :
 Pour garantir l’exactitude et la fiabilité des informations extraites des contrats PDF, un système automatisé doit être intégré à la base de données.
 - Des algorithmes créés pour extraire les informations textuelles
 - Des algorithmes créés pour extraire les logos : L’objectif principal de cette fonction est de fournir une méthode pour extraire et analyser les emplacements et les couleurs dominantes spécifiques des logos présents dans des images extraites à partir de documents PDF.
# Intégration des données avec Talend :
L’extraction de données constitue la première phase du processus d’intégration des données à l’entrepôt de données. \
Cela implique de "lire" et "interpréter" les données sources, 
puis de les copier dans la zone de préparation pour futures manipulations. \
-La première étape pour faire un projet est de connecter aux sources des données \
-La deuxieme étape créer des jobs ( Pour filtrer les données ) \
-le dernier étape liée au chargemenet des données \
\
![jobs](https://github.com/user-attachments/assets/e50c4d0d-9c93-44e0-b4e0-da44f699459b)
\
![Capture3](https://github.com/user-attachments/assets/8b798004-5ea7-4b3b-8cb8-3973c398f2b5)
