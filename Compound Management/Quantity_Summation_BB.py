import pandas as pd
import os

# Function to aggregate barcode quantities from an Excel file
def aggregate_barcodes_from_excel(file_path):
    # Read the Excel file
    data = pd.read_excel(file_path, usecols=[0, 1], header=None, names=['Barcode', 'Quantity'])
    
    # Ensure the quantities column is of numeric type
    data['Quantity'] = pd.to_numeric(data['Quantity'], errors='coerce')
    
    # Group by barcode and sum the quantities
    result = data.groupby('Barcode')['Quantity'].sum().reset_index()
    
    # Define the path to the desktop
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'Results.xlsx')
    
    # Save the result to a new Excel file on the desktop
    result.to_excel(desktop_path, index=False)
    
    print(f"\nAggregated quantities have been saved to '{desktop_path}'")

# Specify the path to your Excel file
file_path = '/Users/kenny/Desktop/Quantity_Sum.xlsx'

# Run the function
aggregate_barcodes_from_excel(file_path)
