# Make sure that the Interpreter is Python 3.11.5 ('base':conda)
from molmass import Formula

def calculate_exact_mass_from_formula(molecular_formula):
    try:
        # Calculate the exact mass using the molmass library
        exact_mass = Formula(molecular_formula).isotope.mass
        return exact_mass
    except Exception as e:
        return str(e)

# Input the molecular formula as a string in Hill notation
molecular_formula = "C40H40N4O5ClF"  # Example: a valid formula

# Calculate and print the exact mass
exact_mass = calculate_exact_mass_from_formula(molecular_formula)
if isinstance(exact_mass, float):
    print(f"The exact mass of the molecule is {exact_mass:.4f} Da")
else:
    print(f"Error: {exact_mass}")
