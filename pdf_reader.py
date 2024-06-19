import tabula

def parse_pdf_to_csv(input_pdf, output_csv):
    # Read the PDF as a DataFrame
    df = tabula.read_pdf(input_pdf, pages='all')

    # Write the DataFrame to a CSV file
    df.to_csv(output_csv, index=False)

# Usage example
parse_pdf_to_csv('/Volumes/NO NAME/branch_dept@sharpusa.com_20240425_163126.pdf', '/Volumes/NO NAME/branch_dept@sharpusa.com_20240425_163126.csv')