import fitz  # PyMuPDF
import cv2
import numpy as np

# Chemin vers le PDF
pdf_path = "C:\\Users\\chiraz\\Downloads\\BA.pdf"

# Ouvrir le PDF
pdf_document = fitz.open(pdf_path)

# Extraire la première page
page = pdf_document.load_page(0)

# Obtenir l'image de la première page
pixmap = page.get_pixmap()

# Convertir l'image en tableau numpy
image_array = np.frombuffer(pixmap.samples, dtype=np.uint8)

# Obtenir les dimensions de l'image
width = pixmap.width
height = pixmap.height

# Remodeler l'array en une matrice 2D RGBA
image_matrix = image_array.reshape((height, width, 4))

# Convertir l'image en niveaux de gris
gray_image = cv2.cvtColor(image_matrix, cv2.COLOR_BGRA2GRAY)

# Utiliser la détection de contours pour trouver les logos
_, binary_image = cv2.threshold(gray_image, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Afficher les contours trouvés
print("Logos de la première page :")
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    print(f"Position : ({x}, {y}), Taille : ({w}, {h})")

# Fermer le PDF
pdf_document.close()





