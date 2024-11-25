import pdfplumber
import extract

pdf_path = extract.file_name

with pdfplumber.open(pdf_path) as pdf:
    # Extraire le texte de la page 9
    page = pdf.pages[8]  # Index 8 correspond à la page 9
    text = page.extract_text()

    # Recherche du BIC et de l'IBAN dans le texte
    bic = ""
    iban = ""
    lines = text.split("\n")
    for line in lines:
        if "BIC" in line:
            bic = line.split(":")[-1].strip()
        elif "IBAN" in line:
            iban = line.split(":")[-1].strip()

    # Afficher les résultats
    print("BIC:", bic)
    print("IBAN:", iban)
    