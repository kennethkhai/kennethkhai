import glob

# Path to the directory containing the .sdf files
directory = '/Users/kenny/Desktop/Testing/Combined SDF'

# Output file name
output_file = '/Users/kenny/Desktop/Testing/Combined SDF/KRAS_MERGE.sdf'

# Get a list of all .sdf files in the directory
sdf_files = glob.glob(directory + '/*.sdf')

# Open the output file in append mode
with open(output_file, 'a') as output:
    # Iterate over each .sdf file
    for sdf_file in sdf_files:
        # Open the current .sdf file
        with open(sdf_file, 'r') as input_file:
            # Read the contents of the .sdf file
            sdf_data = input_file.read()
            # Write the contents to the output file
            output.write(sdf_data)