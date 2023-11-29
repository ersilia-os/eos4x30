# 3D pharmacophore descriptor

The pharmacophore mapper (pmapper) identifies common 3D pharmacophores of active compounds against a specific target and uniquely encodes them with hashes suitable for fast identification of identical pharmacophores. The obtained signatures are amenable for downstream ML tasks.

## Identifiers

* EOS model ID: `eos4x30`
* Slug: `pmapper-3d`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Representation`
* Output: `Descriptor`
* Output Type: `Integer`
* Output Shape: `List`
* Interpretation: vector representation of pharmacophores

## References

* [Publication](https://www.mdpi.com/1422-0067/20/23/5834)
* [Source Code](https://github.com/DrrDom/pmapper)
* Ersilia contributor: [GemmaTuron](https://github.com/GemmaTuron)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos4x30)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos4x30.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos4x30) (AMD64, ARM64)

## Citation

If you use this model, please cite the [original authors](https://www.mdpi.com/1422-0067/20/23/5834) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a BSD-3.0 license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!