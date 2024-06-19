import sys
from molmass import Formula
import sys

def calculate_exact_masses(molecular_formulas):
    exact_masses = []
    formulas = molecular_formulas.strip().split('\n')
    for formula in formulas:
        exact_mass = Formula(formula).isotope.mass
        exact_masses.append((formula, exact_mass))
    return exact_masses

# Input the list of molecular formulas
print("Paste or enter the list of molecular formulas (one per line). Press Ctrl+D when done.")
molecular_formulas = sys.stdin.read()

# Calculate and display exact masses
exact_masses = calculate_exact_masses(molecular_formulas)
for formula, exact_mass in exact_masses:
    print(f"{exact_mass:.4f}")
