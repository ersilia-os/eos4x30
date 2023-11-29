# imports
import os
import csv
import sys
from pmapper.pharmacophore import Pharmacophore as P
from rdkit import Chem
from rdkit.Chem import AllChem
from pprint import pprint


# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

# my model
def my_model(smiles):
    mols = [Chem.MolFromSmiles(smi) for smi in smiles]
    mols = [Chem.AddHs(mol) for mol in mols]
    fps_list = []
    for mol in mols:
        p = P()
        AllChem.EmbedMolecule(mol, randomSeed=42)
        p.load_from_mol(mol)
        b = p.get_fp(min_features=4, max_features=4)
        fps = [1 if i in b else 0 for i in range(2048)]
        fps_list += [fps]
    return fps_list

# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# run model
outputs = my_model(smiles_list)

#check input and output have the same lenght
input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["pmapper-{}".format(i) for i in range(2048)])  # header
    for o in outputs:
        writer.writerow(o)