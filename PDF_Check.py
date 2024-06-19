from PyPDF2 import PdfReader

def check_pdf_compatibility(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PdfReader(file)
            print(f"The PDF at {pdf_path} can be opened with PyPDF2.")
    except Exception as e:
        print(f"An error occurred while trying to open the PDF with PyPDF2: {e}")

# Usage
check_pdf_compatibility('/Volumes/NO NAME/branch_dept@sharpusa.com_20240425_163126.pdf')