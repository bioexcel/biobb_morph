# Biobb Morph: Morph Code for 3DSpine Meshes

The `Morph` class is designed for the production of 3DSpine meshes, from a template IVD mesh to a target, patient-personalized model. It supports various non-rigid registration modes and morphing operations to achieve optimal mesh alignment and transformation.

## Overview
The `Morph` class in `biobb_morph` library provides a set of options to process 3D spine models. It can handle non-rigid registration, rigid registration, and morphing of intervertebral disc meshes. The class offers flexibility in configuring the registration parameters, output file paths, and mesh processing options.

## Parameters
The `Morph` class accepts the following parameters:

- **input_file_path1** (str): Path to a text file with information and coordinates about the source and target models. File type: txt.
- **input_file_path2** (str): Path for the template coordinate meshes IVD file. Type: path (Files are txt and inp files).
- **output_file_path** (str): Path for the resulting template meshes for IVD. File type: output.

### Properties
- **-m** (int): Non-Rigid registration mode. Options:
  * 1: AF
  * 2: NP
  * 3: NoBEP
  * 4: CEPmorph
  * 5: All
  * 0: NONE
  * Default: 5.

- **-i** (int): Create the .inp file for specific components. Options:
  * 1: AF
  * 2: NP
  * 3: NoBEP
  * 4: All
  * 0: NONE
  * Default: 4.

- **-a** (str): Command used to call ABAQUS. If "-a gmsh", the Gmsh tool is used. Default: "abaqus".
- **-b** (str): Command used to call BCPD++. Default: "bcpd".
- **-e** (int): Check failed elements of the resulting .inp file (Abaqus required). Options:
  * 1: YES
  * 2: Iterate value of lambda
  * 0: NO
  * Default: 2.

- **-r** (int): Perform rigid registration at the beginning of the process. Options:
  * 1: YES
  * 0: NO
  * Default: 1.

- **-w** (int): Perform morphing with CEP. Options:
  * 1: YES
  * 0: NO
  * Default: 0.

- **-y** (int): Use interpolated files. Options:
  * 1: YES
  * 0: NO
  * Default: 1.

- **-f** (int): Fuse the AF and NP for the final morph. Options:
  * 1: YES
  * 0: NO
  * Default: 1.

- **-c** (int): Morph external surfaces of AF and NP (including CEP). Options:
  * 1: YES
  * 0: NO
  * Default: 1.

- **-d** (int): Check Hausdorff distance between 3D grids (Euclidean distance). Options:
  * 1: YES
  * 0: NO
  * Default: 1.

- **--CEP** (int): Perform non-rigid registration of the CEP. Options:
  * 1: YES
  * 0: NO
  * Default: 0.

- **--lambdaBeta** (str): Text file with the alpha and beta values for non-rigid registration. Default: "lambdaBeta.csv".

- **--TZ** (int): Create a Transition Zone. Options:
  * 1: YES
  * 0: NO
  * Default: None.

- **-v** (list of float): Enter a list of floats separated by spaces to represent desired movement.
  * Positive: Positive direction
  * Negative: Negative direction
  * 0: No movement
  * Default: [0, 0, 0.05].

- **-n** (float): Distance between two nodes of the mesh. Default: 0.3.

- **-t** (list of float): Translation of the AF and NP. Default: [0.0, 24.1397991, 2.94929004].

- **-p** (list of int): Plane to orthogonally project nodes of the NP to create the spline line of the perimeter. Default: [1, 1, 0].

- **-s** (float): Parameter to reduce the size of the contour of the NP. Default: 0.8.

## Usage Example
This is an example of how to use the `Morph` class in Python:

```python
from biobb_morph.morph.morph import Morph

prop = {
    'm': 1
}
morph = Morph(input_file_path1='fileIn',
              output_file_path='output_path/',
              properties=prop)

