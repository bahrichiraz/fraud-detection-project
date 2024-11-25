import csv
import pdfplumber
import extract
def is_contract_number_present(pdf_path: str, contract_numbers: list) -> bool:
    """
    Check if any of the contract numbers in the list is present in the first page of the PDF.
    """
    try:
        # Ouvrir le fichier PDF
        with pdfplumber.open(extract.file_name) as pdf:
            first_page = pdf.pages[0]
            first_page_text = first_page.extract_text()
            for contract_number in contract_numbers:
                if contract_number in first_page_text:
                    return True

            return False  
    except Exception as e:
        print("Une erreur s'est produite lors de l'extraction du texte:", e)
        return False

# Chemin du fichier PDF à vérifier
pdf_file_path = "C:\\Users\\chiraz\\Downloads\\BA.pdf"

# Liste de numéros de contrat à rechercher
contract_numbers_to_check = ["N°C10024069", "N°c22222", "N°c33333"]

# Vérifier si l'un des numéros de contrat est présent dans la première page du PDF
if is_contract_number_present(pdf_file_path, contract_numbers_to_check):
    print("Au moins un des numéros de contrat est présent dans la première page du PDF.")
else:
    print("Aucun des numéros de contrat n'est présent dans la première page du PDF ou une erreur s'est produite.")
    with open('output.csv', 'w', newline='') as csvfile:
        fieldnames = ['id', 'fraude', 'description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'id': 1, 'fraude': 'faux contrat', 'description': 'Aucun des numéros de contrat / numero de contrat faux'})