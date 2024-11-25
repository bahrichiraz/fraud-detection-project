import fitz  # PyMuPDF
from PIL import Image
from io import BytesIO
import numpy as np
import extract

pdf_path = extract.file_name

# Ouvrir le fichier PDF
pdf_document = fitz.open(pdf_path)
page = pdf_document.load_page(0)

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

        image_pil = Image.open(BytesIO(image_bytes))
        
        # Récupérer les informations sur l'image
        image_size = image_pil.size
        image_mode = image_pil.mode
        
        # Convertir l'image en tableau numpy pour obtenir la couleur dominante
        image_np = np.array(image_pil)
        image_colors, color_counts = np.unique(image_np.reshape(-1, image_np.shape[2]), axis=0, return_counts=True)
        dominant_color_index = np.argmax(color_counts)
        dominant_color = image_colors[dominant_color_index]
        
        # Afficher les informations sur l'image
        print(f"Image {image_index + 1}:")
        print(f"   Taille: {image_size}")
        print(f"   Mode couleur: {image_mode}")
        print(f"   Emplacement: {img_info[2]}")
        print(f"   Couleur dominante: {dominant_color}")
        
        # Afficher l'image
        image_pil.show()
        
        # Sauvegarder l'image dans un fichier
        image_file_name = f"image_page_index_{image_index}.{image_extension}"
        with open(image_file_name, "wb") as image_file:
            image_file.write(image_bytes)
        
        print(f"   Image sauvegardée dans '{image_file_name}'")
else:
    print(f"Aucune image n'a été trouvée sur la page.")

# Fermer le document PDF
pdf_document.close()

