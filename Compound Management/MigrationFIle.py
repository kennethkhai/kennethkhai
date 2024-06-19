import shutil

# Define the source and destination file paths
source_file_path = '/Users/kenny/Library/CloudStorage/GoogleDrive-kenneth@vilyatx.com/Shared drives/Lab Stations/OmniTasker/Barcodes/Barcodes.gsheet'
destination_file_path = '/Users/kenny/Library/CloudStorage/GoogleDrive-kenneth@vilyatx.com/Shared drives/Lab Stations/OmniTasker/Tared_Weights'

try:
    shutil.move(source_file_path, destination_file_path)
    print(f"Moved file from {source_file_path} to {destination_file_path}")
except FileNotFoundError:
    print(f"Source file not found: {source_file_path}")
except shutil.Error as e:
    print(f"Error: {e}")
