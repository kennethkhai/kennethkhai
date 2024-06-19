def create_pyramid(rows):
    for i in range(rows):
        print(' ' * (rows - i - 1) + '*' * (2 * i + 1))

# Example usage
num_rows = 5
create_pyramid(num_rows)