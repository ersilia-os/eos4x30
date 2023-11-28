# imports
import os
import csv
import sys
import datamol as dm
import molfeat
from molfeat.trans.base import MoleculeTransformer
from molfeat.calc.pharmacophore import Pharmacophore3D


# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

# my model
def my_model(smiles):
    mols = [dm.to_mol(s) for s in smiles]
    molecules_with_3D = [dm.conformers.generate(m, n_confs=1, minimize_energy=True) for m in mols]
    transformer = MoleculeTransformer(featurizer=Pharmacophore3D(factory='pmapper'), dtype=float)    
    features = transformer(molecules_with_3D) 
    return features


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
    writer.writerow(["pmapper-{}".format(i) for i in range(outputs.shape[1])])  # header
    for o in outputs:
        writer.writerow(o)
