import fitz  # PyMuPDF

# Chemin vers le PDF
pdf_path = "C:\\Users\\chiraz\\Downloads\\BA.pdf"

# Ouvrir le PDF
pdf_document = fitz.open(pdf_path)

# Extraire la première page
page = pdf_document.load_page(0)

# Extraire les annotations pour trouver les logos
annotations = page.annots()
if annotations:
    print("Logos de la première page :")
    for annot in annotations:
        if annot.type[0] == 1:  # Type 1 représente une annotation de type image
            x0, y0, x1, y1 = annot.rect
            width = x1 - x0
            height = y1 - y0
            print(f"Position : ({x0}, {y0}), Taille : ({width}, {height})")
            image_bytes = annot.get_data()
            # Faites ce que vous voulez avec l'image, par exemple, enregistrez-la ou affichez-la
            # Par exemple, si vous voulez l'afficher :
            image = fitz.Pixmap(fitz.csRGB, image_bytes)
            image.show()

# Fermer le PDF
pdf_document.close()
