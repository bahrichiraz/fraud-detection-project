import pdfplumber
import re
import extract
import csv
import os

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        first_page = pdf.pages[0]
        text = first_page.extract_text()
    return text

# Chemin vers votre fichier PDF
pdf_path = extract.file_name
extracted_text = extract_text_from_pdf(pdf_path)

# Extraction de la partie spécifique
def extract_data_after_keyword(text, keyword):
    match = re.search(keyword, text)
    if match:
        start_index = match.end()
        end_index = text.find('\n', start_index)
        if end_index == -1:
            end_index = len(text)
        data = text[start_index:end_index].strip()
        print("Séquence extraite après 'Formule':", data)  # Afficher la séquence extraite
        numbers = [int(num.strip()) for num in data.split(",")]
        return any(num in [2, 1, 3] for num in numbers)
    else:
        return "Mot-clé non trouvé"

pattern = r"Formule"
result = extract_data_after_keyword(extracted_text, pattern)
print("Après le mot-clé 'Formule' :", result)


if not result:
    # Écrire l'erreur dans un fichier CSV
    error_file_path = "errors.csv"
    fieldnames = ['id', 'fraude', 'description']

    # Vérifier si le fichier CSV existe déjà
    file_exists = os.path.exists(error_file_path)

    with open(error_file_path, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Si le fichier CSV n'existe pas, écrire les en-têtes
        if not file_exists:
            writer.writeheader()

        # Écrire les informations d'erreur
        writer.writerow({'id': 1, 'fraude': 'numero formule est faux', 'description': 'Le formule est faux: ' + result})

    print("Erreur enregistrée dans le fichier CSV:", error_file_path)
