import os
import fitz  # PyMuPDF
import re

def extract_and_combine_text(folder_path, output_filename):
    # Get all PDF files from the specified folder
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]
    
    # Sort PDF files by name
    pdf_files.sort()
    
    # Initialize an empty string to hold the combined text
    combined_text = ''
    
    # Loop through each PDF file and extract text
    for pdf_file in pdf_files:
        pdf_path = os.path.join(folder_path, pdf_file)
        pdf = fitz.open(pdf_path)
        for page in pdf:
            combined_text += page.get_text()
        pdf.close()
    
    # Replace unwanted characters
    combined_text = re.sub(r'\?+', ' ', combined_text)  # Replace sequences of question marks with a single space
    
    # Save the combined text to the output file
    with open(output_filename, 'w', encoding='utf-8') as out:
        out.write(combined_text)

# Usage:
folder_path = "path-to-folder"
output_filename = 'chapters_combined.txt'
extract_and_combine_text(folder_path, output_filename)
