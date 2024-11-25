import requests
from http import HTTPStatus
import copiepdf.connect.conn as conn
import pandas as pd


from db import selectallquery, selectquery
import pandas as pd


# Appel de la fonction login_geoprod pour obtenir le jeton d'authentification
token = selectquery("select id_session from users where id = 1000096")

json_list = []

list_affaire = selectallquery("select a.id from affaire a left join etat_dossier ed on ed.id = a.status  where ed.classe != 2; ")
for affaire in list_affaire:
    response = requests.get(f"https://dev.ws.as-solutions.cloud.geoprod.com/load_list_document_affaire/{affaire['id']}", headers={"idSession": f"{token['id_session']}"})
    # Traiter la réponse
    if response.status_code == 200:
    # Convertir la réponse JSON en objet Python
        data = response.json()

        # Parcourir les éléments de la liste pour trouver le document avec le nom "Adhésion"
        for document in data:
            if  document.get('name') == "Bulletin d'Adhésion":
                if document.get('existe'):
                    print("Informations du document 'Adhésion':")
                    print("Existe :", document.get('existe'))
                    print("MD5 ID :", document.get('md5_id'))
                    print("Obligatoire :", document.get('oblig'))
                    files_associated = document.get('files', [])
                    if files_associated:
                        pdf_urls = [file_info.get('url') for file_info in files_associated if file_info.get('url').endswith('.pdf')]
                        print("URLs des fichiers PDF associés :", pdf_urls)
                        json_list.append({"id_affaire": affaire['id'], "url": pdf_urls })   
                    else:
                        print("Aucun fichier associé.")
                    break
                else :
                    print(".")
    else:
        print(f"La requête a échoué avec le code : {response.status_code}")

df = pd.DataFrame(json_list)
df.to_excel("output.xlsx", index=False)