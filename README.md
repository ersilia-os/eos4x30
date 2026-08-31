# 3D pharmacophore descriptor

The pharmacophore mapper (pmapper) identifies common 3D pharmacophores of active compounds against a specific target and uniquely encodes them with hashes suitable for fast identification of identical pharmacophores. The obtained signatures are amenable for downstream ML tasks.

This model was incorporated on 2023-11-28.Last packaged on 2026-03-20.

## Information
### Identifiers
- **Ersilia Identifier:** `eos4x30`
- **Slug:** `pmapper-3d`

### Domain
- **Task:** `Representation`
- **Subtask:** `Featurization`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
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
| feat_0000 | integer |  | Pmapper feature index 0 |
| feat_0001 | integer |  | Pmapper feature index 1 |
| feat_0002 | integer |  | Pmapper feature index 2 |
| feat_0003 | integer |  | Pmapper feature index 3 |
| feat_0004 | integer |  | Pmapper feature index 4 |
| feat_0005 | integer |  | Pmapper feature index 5 |
| feat_0006 | integer |  | Pmapper feature index 6 |
| feat_0007 | integer |  | Pmapper feature index 7 |
| feat_0008 | integer |  | Pmapper feature index 8 |
| feat_0009 | integer |  | Pmapper feature index 9 |

_10 of 2048 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos4x30](https://hub.docker.com/r/ersiliaos/eos4x30)
- **Docker Architecture:** `AMD64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos4x30.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos4x30.zip)

### Resource Consumption
- **Model Size (Mb):** `1`
- **Environment Size (Mb):** `7977`
- **Image Size (Mb):** `7918.34`

**Computational Performance (seconds):**
- 10 inputs: `40.12`
- 100 inputs: `45.7`
- 10000 inputs: `1355.18`

### References
- **Source Code**: [https://github.com/DrrDom/pmapper](https://github.com/DrrDom/pmapper)
- **Publication**: [https://doi.org/10.3390/ijms20235834](https://doi.org/10.3390/ijms20235834)
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
