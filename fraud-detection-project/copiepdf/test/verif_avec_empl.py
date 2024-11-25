import fitz  # PyMuPDF
from PIL import Image
from io import BytesIO
import numpy as np
import extract

pdf_path = extract.file_name

# Emplacement de l'image que vous recherchez
target_location = 237

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

        # Obtenez l'emplacement de l'image
        image_location = img_info[2]

        # Si l'emplacement correspond à l'emplacement ciblé
        if image_location == target_location:
            image_pil = Image.open(BytesIO(image_bytes))
            
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
