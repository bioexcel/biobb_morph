# BioBB MORPH Command Line Help
Generic usage:
```python
biobb_morph [-h] --config CONFIG --input_file(s) <input_file(s)> --output_file <output_file>
```
-----------------


## Morph
Morphing a morph IVD mesh to a target, creating a patient-personalized model.

### Get help
Command:
```python
biobb_morph -h 
```
    usage: morph [-h] --fileIn FILEIN [OPTIONS]
     
    Program that morphs a morph IVD mesh to a target, producing a patient-personalized model.
   
 
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
    
    required arguments:
      --input_file_path1 INPUT_FILE_PATH1
                            Path to the input file containing source and target information (required).
      --input_file_path2 INPUT_FILE_PATH2
                            Description for the sources paths.
      --output_file_path OUTPUT_FILE_PATH
                            Description for the outputs path. 
    optional arguments:
          -h, --help            show this help message and exit
          --config CONFIG       Configuration file

          -m    Non-Rigid registration mode. Options:
                          1: AF
                          2: NP
                          3: NoBEP
                          4: CEPmorph
                          5: All
                          0: NONE
                        Default: 5.

          -i    Create the .inp file for specific components. Options:
                          1: AF
                          2: NP
                          3: NoBEP
                          4: All
                          0: NONE
                        Default: 4.
          -a    Command to call ABAQUS or Gmsh. Default: "abaqus".
          -b    Command to call BCPD++. Default: "bcpd".
          -e    Check failed elements in the resulting .inp file:

                          1: YES
                          2: Iterate value of lambda
                          0: NO
                        Default: 2.

          -r    Perform rigid registration initially:
                          1: YES
                          0: NO
                        Default: 1.
          -w    Perform morphing with CEP:
                          1: YES
                          0: NO
                        Default: 0.
          -y    Use interpolated files:
                          1: YES
                          0: NO
                        Default: 1.
          -f    Fuse AF and NP for the final morph:
                          1: YES
                          0: NO
                        Default: 1.
          -c    Morph external surfaces of AF and NP (including CEP):
                          1: YES
                          0: NO
                        Default: 1.
          -d    Check Hausdorff distance between 3D grids:
                          1: YES
                          0: NO
                        Default: 1.
          --CEP Perform non-rigid registration of CEP:
                          1: YES
                          0: NO
                        Default: 0.
          --lambdaBeta  File with alpha and beta values for non-rigid registration. Default: "lambdaBeta.csv".
          --TZ      Create a Transition Zone:
                          1: YES
                          0: NO
                        Default: None.
          -v    List of floats for desired movement. Default: [0, 0, 0.05].
          -n    Distance between two nodes of the mesh. Default: 0.3.
          -t    Translation of AF and NP. Default: [0.0, 24.1397991, 2.94929004].
          -p    Plane to orthogonally project NP nodes for spline line of perimeter. Default: [1, 1, 0].
          -s    Parameter to reduce NP contour size. Default: 0.8.



### I / O Arguments


### Syntax:
`input_argument (datatype): Definition`

### Arguments:
- **fileIn (string):**  
  Path to the input file containing source and target model information.  
  *File type:* txt.  

- **sources_path (string):**  
  Path to the morph mesh IVD.  
  *File type:* path.  

- **results_path (string):**  
  Path to the resulting morph meshes for IVD.  
  *File type:* output.  

---

# Config Parameters

### Syntax:
`parameter (datatype) - (default_value): Definition`

### Parameters:

- **-morph** (int): Non-Rigid registration mode. Options:
  * 1: AF
  * 2: NP
  * 3: NoBEP
  * 4: CEPmorph
  * 5: All
  * 0: NONE
  * Default: 5.

- **-toINP** (int): Create the .inp file for specific components. Options:
  * 1: AF
  * 2: NP
  * 3: NoBEP
  * 4: All
  * 0: NONE
  * Default: 4.

- **-abaqusCommand** (str): Command used to call ABAQUS. If "-a gmsh", the Gmsh tool is used. Default: "abaqus".
- **-bcpdCommand** (str): Command used to call BCPD++. Default: "bcpd".
- **-checkFElem** (int): Check failed elements of the resulting .inp file (Abaqus required). Options:
  * 1: YES
  * 2: Iterate value of lambda
  * 0: NO
  * Default: 2.

- **-rigid** (int): Perform rigid registration at the beginning of the process. Options:
  * 1: YES
  * 0: NO
  * Default: 1.

- **-WCEP** (int): Perform morphing with CEP. Options:
  * 1: YES
  * 0: NO
  * Default: 0.

- **-interpo** (int): Use interpolated files. Options:
  * 1: YES
  * 0: NO
  * Default: 1.

- **-fusion** (int): Fuse the AF and NP for the final morph. Options:
  * 1: YES
  * 0: NO
  * Default: 1.

- **-surfRegCEP** (int): Morph external surfaces of AF and NP (including CEP). Options:
  * 1: YES
  * 0: NO
  * Default: 1.

- **-checkHaus** (int): Check Hausdorff distance between 3D grids (Euclidean distance). Options:
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

- **-movement** (list of float): Enter a list of floats separated by spaces to represent desired movement.
  * Positive: Positive direction
  * Negative: Negative direction
  * 0: No movement
  * Default: [0, 0, 0.05].

- **-nodeDistance** (float): Distance between two nodes of the mesh. Default: 0.3.

- **-moveTo** (list of float): Translation of the AF and NP. Default: [0.0, 24.1397991, 2.94929004].

- **-plane** (list of int): Plane to orthogonally project nodes of the NP to create the spline line of the perimeter. Default: [1, 1, 0].

- **-reduce_param** (float): Parameter to reduce the size of the contour of the NP. Default: 0.8.


### YAML
#### [Common config file](https://github.com/bioexcel/biobb_morph/blob/master/biobb_morph/test/data/config/config_morph.yml)
```python
properties:
    morph: 5
    toINP: 4
    abaqusCommand: 'abaqus'
    bcpdCommand: 'bcpd'
    checkFElem: 2
    rigid: 1
    WCEP: 0
    interpo: 1
    fusion: 1
    surfRegCEP: 1
    checkHaus: 1
    CEP: 0
    lambdaBeta: 'lambdaBeta.csv'
    TZ: 1
    movement: [0, 0, 0.04]
    nodeDistance: 0.4
    moveTo: [0.0, 24.1397991, 2.94929004]
    plane: [1, 1, 0]
    reduce_param: 0.8
```
#### Command line
```python
morph --fileIn models/IVD_L1L2_NC0031.txt -morph 5 -toINP 4 -a abaqus -b bcpd --CEP 0 -d 1 --lambdaBeta lambdaBeta.csv --TZ 1 -movement 0 0 0.04 -nodeDistance 0.4 -moveTo 0.0 24.1397991 2.94929004 -plane 1 1 0 -reduce_param 0.8
```
