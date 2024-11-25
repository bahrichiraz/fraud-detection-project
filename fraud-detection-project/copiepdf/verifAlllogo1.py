import fitz  # PyMuPDF
from PIL import Image
from io import BytesIO
import extract
import numpy as np
#from sklearn.svm import SVC
#from sklearn.metrics import accuracy_score

# Fonction pour extraire les couleurs des logos à partir des images
def extract_logo_colors(image_bytes):
    image_pil = Image.open(BytesIO(image_bytes))
    image_np = np.array(image_pil)
    image_colors = np.unique(image_np.reshape(-1, image_np.shape[2]), axis=0)
    return image_colors

# Chemin du fichier PDF
pdf_path = extract.file_name

# Emplacements des images que vous recherchez
target_location = [237] # Vous pouvez ajuster cela selon vos besoins

# Taille cible des images
target_size = (237, 158)  # Vous pouvez ajuster cela selon vos besoins

# Mode couleur cible des images
target_color_mode = "RGB"

# Ouvrir le fichier PDF
pdf_document = fitz.open(pdf_path)
page = pdf_document.load_page(0)

# Liste pour stocker les couleurs des logos extraites de chaque image
logo_colors = []

# Boucle sur chaque emplacement d'image recherché
for target_location in target_location:
    image_list = page.get_images(full=True)

    # Vérifier s'il y a des images sur la page
    if image_list:
        print(f"Images trouvées sur la page:")
        # Boucle sur chaque image trouvée sur la page
        for image_index, img_info in enumerate(image_list):
            xref = img_info[0]
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            image_extension = base_image["ext"]

            # Obtenez l'emplacement de l'image
            image_location = img_info[2]

            # Si l'emplacement correspond à l'emplacement ciblé
            if image_location == target_location:
                image_pil = Image.open(BytesIO(image_bytes))
                
                # Vérifier la taille et le mode couleur de l'image
                if image_pil.size != target_size or image_pil.mode != target_color_mode:
                    print("Propriétés d'image incorrectes. C'est une fausse image.")
                else:
                    # Extraire les couleurs des logos
                    colors = extract_logo_colors(image_bytes)
                    logo_colors.extend(colors)
                    
                    # Afficher l'image
                    image_pil.show()
                    print(f"Image trouvée à l'emplacement {target_location}.")
                    
                break
        else:
            print(f"Aucune image trouvée à l'emplacement {target_location}.")
    else:
        print(f"Aucune image n'a été trouvée sur la page.")

# Fermer le document PDF
pdf_document.close()

# Vérifier si le logo est principalement rouge
if len(logo_colors) == 0:
    print("Aucune couleur extraite pour le logo.")
else:
    # Définir la plage de valeurs pour la composante rouge (R) dans l'espace couleur RGB
    red_lower = 150  # Valeur minimale de la composante rouge
    red_upper = 255  # Valeur maximale de la composante rouge

    # Compter le nombre de couleurs extraites qui se situent dans la plage de valeurs spécifiée pour la composante rouge
    red_count = sum(1 for color in logo_colors if red_lower <= color[0] <= red_upper)

    # Calculer le pourcentage de couleurs extraites qui sont dans la plage de valeurs pour la composante rouge
    red_percentage = (red_count / len(logo_colors)) * 100

    # Déterminer si le logo est principalement rouge en fonction du pourcentage de couleurs rouges
    if red_percentage >= 50:  # Vous pouvez ajuster ce seuil selon vos besoins
        print("Le logo est principalement rouge.")
    else:
        print("Le logo n'est pas principalement rouge.")
