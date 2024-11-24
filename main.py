import pandas as pd
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import joblib


app = Flask(__name__, template_folder="template")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        # Get selected model from the form
        selected_model = request.form['model']
        if file and selected_model:
            filename = secure_filename(file.filename)
            file_path = 'uploads/' + filename
            file.save(file_path)

            try:
                # Charger le modèle sélectionné
                model = joblib.load(selected_model)

                # Lire le fichier CSV
                df = pd.read_csv(file_path)
                df.dropna(inplace=True)

                # Groupement des classes
                attack_group = {
                    'Infilteration': 'Web attack',
                    'Fuzzers': 'Web attack',
                    'Generic': 'Web attack',
                    'injection': 'Web attack',
                    'Analysis': 'Web attack',
                    'xss': 'Web attack',
                    'Benign': 'BENIGN',
                    'backdoor': 'BACKDOOR',
                    'scanning': 'SCANNING',
                    'mitm': 'MITM',
                    'dos': 'DOS',
                    'ddos': 'DDOS',
                    'bruteforce': 'BRUTEFORCE',
                    'Theft': 'THEFT',
                    'Reconnaissance': 'RECON',
                    'Shellcode': 'SHELLCODE',
                    'ransomware': 'RANSOMWARE',
                    'Bot': 'BOT'
                }

                # Création d'une colonne Attack catégorie
                df['Attack_Category'] = df['Attack'].map(
                    lambda x: attack_group.get(x, 'Unknown'))

                # Prédictions
                X = df.drop(
                    ['Label', 'Attack', 'Attack_Category'], axis=1).values
                predictions = model.predict(X)

                # Création d'un DataFrame pour stocker les résultats
                result_df = pd.DataFrame({'Label': predictions})
                result_df['Label'] = result_df['Label'].map(
                    {0: 'No attack', 1: 'Attack'})
                result_df['Attack'] = df['Attack']
                result_df['Attack_Category'] = df['Attack_Category']

                return render_template('result.html', result=result_df)

            except FileNotFoundError:
                return "Model file not found."
    return "No file selected."


if __name__ == '__main__':
    app.run(debug=True)
