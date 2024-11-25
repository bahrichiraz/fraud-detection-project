import fitz  # PyMuPDF
from PIL import Image
from io import BytesIO

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
            image_pil.show()
            # Sauvegarder l'image dans un fichier
            image_file_name = f"image_page_index_{image_index}.{image_extension}"
            with open(image_file_name, "wb") as image_file:
                image_file.write(image_bytes)
            
            print(f"Image {image_index + 1}: Sauvegardée dans '{image_file_name}'")
else:
        print(f"Aucune image n'a été trouvée sur la page .")

# Fermer le document PDF
pdf_document.close()
