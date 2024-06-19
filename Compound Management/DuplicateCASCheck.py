import pandas as pd

# Read the CSV file
df = pd.read_csv('/Users/kenny/Desktop/Code/Test_Duplicates.csv')
# Find duplicate entries in the 'CAS' column
duplicates = df[df['CAS'].notna()].duplicated(subset='CAS', keep=False)

# If there are duplicates, print them
if duplicates.any():
    print("There are duplicate entries in the 'CAS' column.")
    print(df[duplicates])
else:
    print("There are no duplicate entries in the 'CAS' column.")
duplicates = df.duplicated(subset='CAS', keep=False)

# If there are duplicates, print them
if duplicates.any():
    print("There are duplicate entries in the 'CAS' column.")
    print(df[duplicates])
else:
    print("There are no duplicate entries in the 'CAS' column.")