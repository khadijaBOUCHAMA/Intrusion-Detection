# Détection d'Intrusions dans le Domaine de la Cybersécurité : Approche avec Machine Learning

## Description du Projet

Ce projet porte sur la détection d'intrusions dans le domaine de la cybersécurité en utilisant des techniques d'apprentissage automatique (Machine Learning).

L'objectif principal est de développer et comparer différents modèles de classification pour identifier les attaques réseau à partir de données de trafic. Le projet explore et multiclasse (différents types d'attaques), en utilisant un ensemble de données récent et pertinent : NF-UQ-NIDS-v2.

Les résultats montrent des performances excellentes, avec une précision atteignant 100% pour certains modèles comme Random Forest, tout en maintenant des temps de prédiction très courts.

## Structure du Projet

Le projet est organisé en plusieurs dossiers :

- `cyermultilass/` : Implémentation pour la classification multiclasse.
  - `multiclasses with smote.ipynb` : Notebook pour multiclasse avec SMOTE.
  - `code&dataset/` : Notebooks pour chaque modèle ML.
  - `Rapport_&_presentation/` : Rapport et présentation en PDF.

- `flask/` : Application web Flask pour le déploiement des modèles entraînés.
  - `main.py` : Code principal de l'application Flask.
  - `template/` : Templates HTML pour l'interface utilisateur.
  - `static/` : Fichiers statiques (images, CSS).
  - `uploads/` : Dossier pour les fichiers uploadés.
  - Modèles sauvegardés : `*.pkl` fichiers pour chaque algorithme.

- `Cyber security.pdf` : Document complémentaire sur la cybersécurité.

## Modèles de Machine Learning Utilisés

Le projet implémente et compare 7 algorithmes de classification :

1. **Decision Tree** : Arbre de décision simple et interprétable.
2. **Random Forest** : Ensemble d'arbres de décision (meilleur modèle avec 100% de précision).
3. **Logistic Regression** : Régression logistique pour classification binaire.
4. **AdaBoost** : Algorithme de boosting adaptatif.
5. **Gradient Boosting** : Boosting par gradient.
6. **XGBoost** : Version optimisée du gradient boosting.
7. **SVM (Support Vector Machine)** : Machines à vecteurs de support.

Chaque modèle est évalué sur des métriques comme la précision, le F1-score, et le temps d'entraînement/prédiction.

## Dataset

Le projet utilise le dataset **NF-UQ-NIDS-v2** (Netflow University of Queensland Network Intrusion Detection System), collecté à l'Université du Queensland en Australie. Ce dataset simule un environnement réseau réel avec du trafic normal et des attaques diverses.

- **Caractéristiques** : 81 951 observations, 44 caractéristiques.
- **Équilibre des classes** : Classes équilibrées pour la classification binaire.
- **Prétraitement** : Nettoyage des données, gestion des valeurs manquantes, groupement des attaques par catégories.

## Installation et Prérequis

### Prérequis
- Python 3.7+
- Bibliothèques Python : pandas, scikit-learn, joblib, flask, werkzeug
- Jupyter Notebook pour exécuter les notebooks

### Installation
1. Clonez ou téléchargez le projet dans un répertoire local.
2. Installez les dépendances :
   ```
   pip install pandas scikit-learn joblib flask werkzeug
   ```
3. Pour les notebooks, assurez-vous d'avoir Jupyter installé :
   ```
   pip install jupyter
   ```

## Utilisation

### Exécution des Notebooks
1. Ouvrez un terminal dans le répertoire du projet.
2. Lancez Jupyter :
   ```
   jupyter notebook
   ```
3. Naviguez vers le dossier cyermultilass et ouvrez les notebooks `.ipynb`.
4. Exécutez les cellules pour entraîner les modèles et analyser les résultats.

### Application Flask
1. Naviguez vers le dossier `flask/` :
   ```
   cd flask
   ```
2. Lancez l'application :
   ```
   python main.py
   ```
3. Ouvrez un navigateur web et allez à `http://127.0.0.1:5000/`.
4. Upload un fichier CSV de test (format compatible avec le dataset) et sélectionnez un modèle pour obtenir des prédictions.

L'application permet de :
- Uploader un fichier CSV contenant des données de trafic réseau.
- Sélectionner un modèle entraîné (Decision Tree, Random Forest, etc.).
- Obtenir des prédictions avec les catégories d'attaques.

## Résultats et Performances

- **Classification Binaire** : Random Forest atteint 100% de précision et F1-score.
- **Temps de Prédiction** : Inférieur à 1 ms pour Decision Tree, 3 ms pour Random Forest.
- **Comparaison** : Tous les modèles sauf Logistic Regression (>86%) montrent d'excellentes performances.

Les matrices de confusion et les métriques détaillées sont disponibles dans les rapports PDF.

