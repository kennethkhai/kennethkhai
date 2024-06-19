inputs = []  # List to store the inputs

# Take 96 inputs
for _ in range(96):
    value = input("Enter a value: ")
    inputs.append(value)

# Transfer inputs into rows of 8
rows = [inputs[i:i+8] for i in range(0, len(inputs), 8)]

# Print the rows with cell-separated values
for row in rows:
    print('\t'.join(row))