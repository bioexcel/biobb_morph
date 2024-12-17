[![](https://img.shields.io/github/v/tag/bioexcel/biobb_morph?label=Version)](https://GitHub.com/bioexcel/biobb_morph/tags/)

[![](https://img.shields.io/badge/OS-Unix%20%7C%20MacOS-blue)](https://github.com/bioexcel/biobb_morph)
[![](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![](https://img.shields.io/badge/Open%20Source%3f-Yes!-blue)](https://github.com/bioexcel/biobb_morph)

[![](https://readthedocs.org/projects/biobb-morph/badge/?version=latest&label=Docs)](https://biobb-morph.readthedocs.io/en/latest/?badge=latest)
[![](https://img.shields.io/website?down_message=Offline&label=Biobb%20Website&up_message=Online&url=https%3A%2F%2Fmmb.irbbarcelona.org%2Fbiobb%2F)](https://mmb.irbbarcelona.org/biobb/)
[![](https://img.shields.io/badge/Youtube-tutorials-blue?logo=youtube&logoColor=red)](https://www.youtube.com/@BioExcelCoE/search?query=biobb)
[![](https://zenodo.org/badge/DOI/10.1038/s41597-019-0177-4.svg)](https://doi.org/10.1038/s41597-019-0177-4)
[![](https://img.shields.io/endpoint?color=brightgreen&url=https%3A%2F%2Fapi.juleskreuer.eu%2Fcitation-badge.php%3Fshield%26doi%3D10.1038%2Fs41597-019-0177-4)](https://www.nature.com/articles/s41597-019-0177-4#citeas)

[![](https://docs.bioexcel.eu/biobb_morph/junit/testsbadge.svg)](https://docs.bioexcel.eu/biobb_morph/junit/report.html)
[![](https://docs.bioexcel.eu/biobb_morph/coverage/coveragebadge.svg)](https://docs.bioexcel.eu/biobb_morph/coverage/)
[![](https://docs.bioexcel.eu/biobb_morph/flake8/flake8badge.svg)](https://docs.bioexcel.eu/biobb_morph/flake8/)
[![](https://img.shields.io/github/last-commit/bioexcel/biobb_morph?label=Last%20Commit)](https://github.com/bioexcel/biobb_morph/commits/master)
[![](https://img.shields.io/github/issues/bioexcel/biobb_morph.svg?color=brightgreen&label=Issues)](https://GitHub.com/bioexcel/biobb_morph/issues/)


# biobb_morph

## Introduction
Biobb_morph is a Python library that provides tools for performing 3D morphological transformations of intervertebral disc (IVD) meshes. It enables the creation of patient-personalized 3D models by morphing a morph IVD mesh into a target shape. The library is part of the BioExcel Building Blocks (Biobb) framework, designed to facilitate interoperability and compatibility with bioinformatics tools.

For the latest API documentation, visit
[latest API documentation](http://biobb-morph.readthedocs.io/en/latest/).

## Version
v4.1.0 2024.12

## Installation

If you have no experience with anaconda, please first take a look to the [New with anaconda?](https://biobb-documentation.readthedocs.io/en/latest/first_steps.html#new-with-anaconda) section of the [official documentation](https://biobb-documentation.readthedocs.io/en/latest/).

### Download repository

Although the biobb_morph repository is available at GitHub and thus you can clone it, we strongly recommend you to [**download it compressed**](https://github.com/bioexcel/biobb_morph/archive/master.zip) and start your new project from scratch. 

### Create new conda environment

Once you have the project unzipped in your computer, please follow the next steps to create a new conda environment:

```console
cd biobb_morph-master
conda create --name biobb_morph --file conda_env/environment.yml
```

### Update environment paths

Edit **conda_env/biobb_morph.pth** with the paths to your *biobb_morph* folder. Example:

```console
/home/user_name/projects/biobb_morph/
/home/user_name/projects/biobb_morph/biobb_morph/biobb_morph
```

Copy the edited **conda_env/biobb_morph.pth** file to the site-packages folder of your environment. This folder is in */[anaconda-path]/envs/biobb_morph/lib/python3.7/site-packages*, where */[anaconda-path]* is usually */anaconda3* or */opt/conda*.

```console
cp conda_env/biobb_morph.pth /[anaconda-path]/envs/biobb_morph/lib/python3.7/site-packages
```

### Activate environment

Then, activate the recently created *biobb_morph* conda environment:

```console
conda activate biobb_morph
```

### Create repository

This morph includes some folders not standard for a biobb, such as **biobb_morph/adapters/**, **biobb_morph/notebooks/** or **conda_env/**. For the sake of having a pure biobb structure, you should uncomment the three last lines of the **.gitignore** file before creating a new git repository:

```console
biobb_morph/adapters
biobb_morph/notebooks
conda_env
```
Then, inialitize repository:

```console
git init
```

### Binary paths configuration

Additionally, it's recommendable to configure binary paths in your environment in order to ease the command line execution. More info about this subject in the [Binary path configuration](https://biobb-documentation.readthedocs.io/en/latest/execution.html#binary-path-configuration) section of the [official documentation](https://biobb-documentation.readthedocs.io/en/latest/).

## Run tests

To run tests, please execute the following instruction:

```console
pytest /path/to/biobb_morph/biobb_morph/test/unitests/test_morph/test_morph.py
```
Or, if you prefer to show the BioBB output during the test process:

```console
pytest -s /path/to/biobb_morph/biobb_morph/test/unitests/test_morph/test_morph.py
```


### Usage Example

Here is a Python code snippet demonstrating how to use the Biobb_morph package:

```
from biobb_morph.morph.morph import morphing

properties = {
    'm': 1,
    'a': 'gmsh',
    'b': 'bcpd'
}
morphing(
    input_file_path1='models/IVD_L1L2_NC0031.txt',
    input_file_path2='sources/',
    output_file_path='results/'
    properties=properties
)
```


## Documentation

[Click here to find the API Documentation example](https://biobb-morph.readthedocs.io/en/latest/morph.html) for this morph and [here for Command Line documentation](http://biobb-morph.readthedocs.io/en/latest/command_line.html).

And here you can find [the full documentation](https://biobb-documentation.readthedocs.io/en/latest/) about how to build a new **BioExcel building block** from scratch.

## Copyright & Licensing
This software has been developed in the [MMB group](http://mmb.irbbarcelona.org) at the [BSC](http://www.bsc.es/) & [IRB](https://www.irbbarcelona.org/) for the [European BioExcel](http://bioexcel.eu/), funded by the European Commission (EU H2020 [823830](http://cordis.europa.eu/projects/823830), EU H2020 [675728](http://cordis.europa.eu/projects/675728)).

* (c) 2015-2022 [Barcelona Supercomputing Center](https://www.bsc.es/)
* (c) 2015-2022 [Institute for Research in Biomedicine](https://www.irbbarcelona.org/)

Licensed under the
[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0), see the file LICENSE for details.

![](https://bioexcel.eu/wp-content/uploads/2019/04/Bioexcell_logo_1080px_transp.png "Bioexcel")
