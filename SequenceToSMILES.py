import os
import subprocess

# Create a virtual environment
venv_path = "/Users/kenny/Desktop/Code/venv"
subprocess.run(["python", "-m", "venv", venv_path])

# Activate the virtual environment
activate_script = os.path.join(venv_path, "bin", "activate")
subprocess.run(["source", activate_script], shell=True)

# Install RDKit in the virtual environment
subprocess.run(["pip", "install", "rdkit"])

# Deactivate the virtual environment
subprocess.run(["deactivate"], shell=True)

from rdkit import Chem

def convert_sequence_to_cyclized_smiles(sequence):
    # Convert sequence to cyclized SMILES
    mol = Chem.MolFromSequence(sequence)
    if mol is None:
        raise ValueError("Invalid sequence")

    Chem.Kekulize(mol)
    smiles = Chem.MolToSmiles(mol)

    return smiles

# Example usage
sequence = 'YOUR_SEQUENCE_HERE'
cyclized_smiles = convert_sequence_to_cyclized_smiles(sequence)
print(cyclized_smiles)
