import fitz  # PyMuPDF
from PIL import Image
import io
import numpy as np
import extract
 

pdf_path = extract.file_name

# Chemin vers le fichier PDF

# Ouvrir le fichier PDF
pdf_document = fitz.open(pdf_path)

# Sélectionner la première page
page = pdf_document[0]

# Récupérer les annotations de la page
annotations = page.first_page.annots()

# Rechercher les annotations de type "Widget" (qui sont souvent utilisées pour les images)
logo_annotations = [a for a in annotations if a.type[0] == 2]

if logo_annotations:
    # Récupérer les coordonnées de l'image
    x0, y0, x1, y1 = logo_annotations[0].rect
    x0, y0, x1, y1 = round(x0), round(y0), round(x1), round(y1)

    # Extraire l'image sous forme de matrice de pixels RGB
    image_matrix = page.get_pixmap(alpha=False, matrix=fitz.Matrix(1, 1)).samples[y0:y1, x0:x1]
    
    # Convertir la matrice en objet d'image Pillow
    logo = Image.fromarray(image_matrix)

    # Afficher l'image
    logo.show()

    # Vérifier la couleur du pixel en haut à gauche pour déterminer si le logo est rouge
    pixel_color = logo.getpixel((0, 0))
    if pixel_color == (255, 0, 0):
        print("Le logo est rouge, c'est un logo valide.")
    else:
        print("Le logo n'est pas rouge, c'est un faux logo.")
else:
    print("Aucun logo trouvé dans le PDF.")
