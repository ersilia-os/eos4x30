# 3D pharmacophore descriptor

The pharmacophore mapper (pmapper) identifies common 3D pharmacophores of active compounds against a specific target and uniquely encodes them with hashes suitable for fast identification of identical pharmacophores. The obtained signatures are amenable for downstream ML tasks.

This model was incorporated on 2023-11-28.

## Information
### Identifiers
- **Ersilia Identifier:** `eos4x30`
- **Slug:** `pmapper-3d`

### Domain
- **Task:** `Representation`
- **Subtask:** `Featurization`
- **Biomedical Area:** `Any`
- **Target Organism:** `Not Applicable`
- **Tags:** `Descriptor`, `Fingerprint`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `2048`
- **Output Consistency:** `Fixed`
- **Interpretation:** Vector representation of pharmacophores

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| dim_0000 | integer |  | Pmapper dimension index 0 |
| dim_0001 | integer |  | Pmapper dimension index 1 |
| dim_0002 | integer |  | Pmapper dimension index 2 |
| dim_0003 | integer |  | Pmapper dimension index 3 |
| dim_0004 | integer |  | Pmapper dimension index 4 |
| dim_0005 | integer |  | Pmapper dimension index 5 |
| dim_0006 | integer |  | Pmapper dimension index 6 |
| dim_0007 | integer |  | Pmapper dimension index 7 |
| dim_0008 | integer |  | Pmapper dimension index 8 |
| dim_0009 | integer |  | Pmapper dimension index 9 |

_10 of 2048 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos4x30](https://hub.docker.com/r/ersiliaos/eos4x30)
- **Docker Architecture:** `AMD64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos4x30.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos4x30.zip)

### Resource Consumption


### References
- **Source Code**: [https://github.com/DrrDom/pmapper](https://github.com/DrrDom/pmapper)
- **Publication**: [https://www.mdpi.com/1422-0067/20/23/5834](https://www.mdpi.com/1422-0067/20/23/5834)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2019`
- **Ersilia Contributor:** [GemmaTuron](https://github.com/GemmaTuron)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [BSD-3-Clause](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos4x30
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos4x30
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
