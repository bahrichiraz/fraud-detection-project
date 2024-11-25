import pdfplumber
import re
import extract
import csv

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        first_page = pdf.pages[0]
        text = first_page.extract_text()
    return text
# Chemin vers votre fichier PDF
pdf_path = extract.file_name
extracted_text = extract_text_from_pdf(pdf_path)


# Extraction de la partie spécifique
def extract_data_after_keyword(text, keyword, lines=3):
    match = re.search(keyword, text)
    if match:
        start_index = match.end()
        end_index = start_index
        for i in range(lines):
            end_index = text.find('\n', end_index + 1)
            if end_index == -1:
                break
        return text[start_index:end_index]
    else:
        return "Mot-clé non trouvé"
        

pattern = r"Compte client"
data_after_keyword = extract_data_after_keyword(extracted_text, pattern, lines=3)
print("Les données de 'Compte client':")
print(data_after_keyword)

if data_after_keyword == "Mot-clé non trouvé":
    with open('compte.csv', 'w', newline='') as csvfile:
           fieldnames = ['id', 'fraude', 'description']
           writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Écrire les en-têtes
           writer.writeheader()
           writer.writerow({'id': 1, 'fraude': 'faux contrat', 'description': 'Aucun des numéros de contrat / numero de contrat faux'})
