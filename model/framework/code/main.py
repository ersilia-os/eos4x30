# imports
import os
import csv
import sys
import numpy as np
import datamol as dm
import molfeat
from molfeat.trans.base import MoleculeTransformer
from molfeat.calc.pharmacophore import Pharmacophore3D


# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# run model: generate 3D conformers and compute pharmacophore features per molecule
transformer = MoleculeTransformer(featurizer=Pharmacophore3D(factory='pmapper'), dtype=float)

n_features = None
outputs = []
for smi in smiles_list:
    try:
        mol = dm.to_mol(smi)
        mol_3d = dm.conformers.generate(mol, n_confs=1, minimize_energy=True)
        feats = transformer([mol_3d])[0]
        if n_features is None:
            n_features = len(feats)
        outputs.append(feats.astype(int))
    except Exception:
        outputs.append(None)

# fill None rows with NaN once we know the feature size
if n_features is None:
    n_features = 0
outputs = [o if o is not None else np.full(n_features, float("nan")) for o in outputs]

assert len(outputs) == len(smiles_list)

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["feat_{0}".format(str(i).zfill(4)) for i in range(n_features)])
    for o in outputs:
        writer.writerow(o)
