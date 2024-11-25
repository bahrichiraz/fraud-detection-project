import pandas as pd
import pdfplumber
import requests
import os

df = pd.read_excel("C:\\Users\\chiraz\\Downloads\\output.xlsx")

# Extract PDF links from the 'url' column and remove leading and trailing characters
pdf_links = df['url'].str.strip("'[").str.strip("]'")

# Create a folder to save downloaded PDF files
output_folder = "downloaded_pdfs"
os.makedirs(output_folder, exist_ok=True)

# Iterate through each PDF link
for pdf_link in pdf_links:
    if pdf_link.endswith("BA.pdf"):
        print("Processing PDF Link:", pdf_link)
        try:
            response = requests.get(pdf_link)
            file_name = os.path.join(output_folder, os.path.basename(pdf_link))
            with open(file_name, "wb") as f:
                f.write(response.content)
            with pdfplumber.open(file_name) as pdf:
                account_info_found = False
                for page in pdf.pages:
                    text = page.extract_text()
                    #print(text)
                    text1 = pdf.pages[0].extract_text()
           
    
        except Exception as e:
            print("Error processing PDF:", e)

