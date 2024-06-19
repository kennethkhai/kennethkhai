from rdkit import Chem
from rdkit.Chem import AllChem

# Read the SDF file
suppl = Chem.SDMolSupplier('/Users/kenny/Downloads/selected_VYA-1004_ExpA_192set_crude.sdf')

# Create a new SDF writer
writer = Chem.SDWriter('/Users/kenny/Downloads/selected_VYA-1004_ExpA_192set_crude.sdf')

# Iterate over the molecules in the SDF file
for mol in suppl:
    if mol is not None:
        # Perform structure cleanup
        mol = Chem.RemoveHs(mol)
        mol = Chem.AddHs(mol)
        mol = Chem.AssignStereochemistry(mol, force=True, cleanIt=True)
        AllChem.EmbedMolecule(mol, useRandomCoords=True)
        AllChem.UFFOptimizeMolecule(mol)

        # Write the cleaned molecule to the output SDF file
        writer.write(mol)

# Close the SDF writer
writer.close()