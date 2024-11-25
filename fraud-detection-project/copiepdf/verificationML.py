import numpy as np
from sklearn.svm import SVC
from PIL import Image
from io import BytesIO
import fitz
import extract

# Fonction pour extraire les couleurs des logos à partir des images
def extract_logo_colors(image_bytes):
    image_pil = Image.open(BytesIO(image_bytes))
    image_np = np.array(image_pil)
    image_colors = np.unique(image_np.reshape(-1, image_np.shape[2]), axis=0)
    return image_colors

# Fonction pour calculer la couleur moyenne
def compute_average_color(colors):
    return np.mean(colors, axis=0)

# Fonction pour vérifier si la couleur moyenne est proche du rouge
def is_red(color):
    red_threshold = 150
    return color[0] > red_threshold and color[1] < red_threshold and color[2] < red_threshold

# Chemin du fichier PDF
pdf_path = extract.file_name

# Emplacement de l'image que vous recherchez
target_location = 237

# Ouvrir le fichier PDF
pdf_document = fitz.open(pdf_path)
page = pdf_document.load_page(0)

# Liste pour stocker les couleurs des logos extraites
logo_colors = []

# Boucle sur chaque emplacement d'image recherché
for img_info in page.get_images(full=True):
    xref = img_info[0]
    base_image = pdf_document.extract_image(xref)
    image_bytes = base_image["image"]

    # Obtenez l'emplacement de l'image
    image_location = img_info[2]

    # Si l'emplacement correspond à l'emplacement ciblé
    if image_location == target_location:
        # Extraire les couleurs des logos
        colors = extract_logo_colors(image_bytes)
        logo_colors.extend(colors)
        
        # Calculer la couleur moyenne
        average_color = compute_average_color(logo_colors)
        
        # Afficher l'image
        Image.open(BytesIO(image_bytes)).show()
        
        break

pdf_document.close()

# Vérifier si la couleur moyenne est rouge
if is_red(average_color):
    print("Le logo est principalement rouge.")
else:
    print("Le logo n'est pas principalement rouge.")
