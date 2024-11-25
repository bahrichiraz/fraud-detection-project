import pdfplumber
from PIL import Image
import extract
import io

pdf_path = extract.file_name

# Ouvrir le fichier PDF
with pdfplumber.open(pdf_path) as pdf:
    # Sélectionner la première page
    page = pdf.pages[0]

    # Récupérer les images de la page
    images = page.images
    if images:
        # Récupérer la première image (supposée être le logo)
        image_obj = images[0]['obj']  # Récupérer l'objet image
        image_data = image_obj.get_data()  # Récupérer les données de l'image
        logo = Image.open(io.BytesIO(image_data))
        print("Logo found")
        # Vérifier la couleur du logo
        if logo.getbbox():
            # Obtenir les coordonnées du logo
            left, top, right, bottom = logo.getbbox()
            logo_width = right - left
            logo_height = bottom - top

            # Vérifier si la couleur du logo est rouge
            if logo.getpixel((left, top)) == (255, 0, 0):
                print("Le logo est rouge, c'est un logo valide.")
            else:
                print("Le logo n'est pas rouge, c'est un faux logo.")

            # Afficher le logo
            logo.show()

        else:
            print("Aucune image n'a été trouvée sur la première page.")
    else:
        print("Aucune image n'a été trouvée dans le PDF.")