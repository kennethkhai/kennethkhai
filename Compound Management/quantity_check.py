import pandas as pd
import numpy as np

#Running will output the building blocks that are low in stock for a given synthesis run
# Read the input csv file
input_file = input("Enter the path to the input csv file: ")
df_input = pd.read_csv(input_file)
#Read the frequency csv file
frequency_file = input("Enter the path to the input csv file with # of uses:")
df_frequency = pd.read_csv(frequency_file)


scale = input("Enter the scale of synthesis (120 or 300 uM): ")

# Validate the scale input
while scale not in ['120', '300']:
    print("Invalid scale input. Please choose between 120 and 300.")
    scale = input("Enter the scale of synthesis (in uM) (120 or 300 uM): ")

# Convert the scale to a float value
scale = float(scale)

# Calculate the quantity needed based on frequency, scale, and molecular weight
df_input['Quantity_needed'] = df_frequency['Frequency'] * scale * df_input['Molecular_weight'] * (10 ** -6) + 0.5 * (100 * 10 ** -6) * df_input['Molecular_weight']
df_input['Enough_quantity'] = df_input['Quantity_needed'] <= df_input['Quantity_in_stock']


# Filter the building blocks that have low stock
low_stock_blocks = df_input.loc[df_input['Enough_quantity'] == False, 'Building_block_ID']

# Print the building blocks that are low in stock
print("Building blocks with low stock:")
print(low_stock_blocks)

# Save the building blocks with low stock to an Excel file
if low_stock_blocks.empty:
    print("All building blocks have enough stock.")
else:
    output_file = input("Enter the path to save the output Excel file: ")
    low_stock_blocks.to_excel(output_file, index=False)
    print("Building blocks with low stock have been saved to", output_file)