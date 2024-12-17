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
- **m (int) - 5:**  
  Non-Rigid registration mode.  

- **i (int) - 4:**  
  Create the `.inp` file for specific components.  

- **a (string) - "abaqus":**  
  Command to call ABAQUS or Gmsh.  

- **b (string) - "bcpd":**  
  Command to call BCPD++.  

- **e (int) - 2:**  
  Check failed elements in the resulting `.inp` file.  

- **r (int) - 1:**  
  Perform rigid registration initially.  

- **w (int) - 0:**  
  Morphing with CEP.  

- **y (int) - 1:**  
  Use interpolated files.  

- **f (int) - 1:**  
  Fuse AF and NP for the final morph.  

- **c (int) - 1:**  
  Morph external surfaces of AF, NP (including CEP).  

- **d (int) - 1:**  
  Check Hausdorff distance between 3D grids.  

- **CEP (int) - 0:**  
  Perform non-rigid registration of CEP.  

- **lambdaBeta (string) - "lambdaBeta.csv":**  
  File with alpha, beta values.  

- **TZ (int) - None:**  
  Create Transition Zone.  

- **v (list[float]) - [0, 0, 0.05]:**  
  Desired movement list.  

- **n (float) - 0.3:**  
  Distance between two nodes of the mesh.  

- **t (list[float]) - [0.0, 24.1397991, 2.94929004]:**  
  Translation of AF, NP.  

- **p (list[int]) - [1, 1, 0]:**  
  Plane for NP spline perimeter.  

- **s (float) - 0.8:**  
  Reduce NP contour size.  

### YAML
#### [Common config file](https://github.com/bioexcel/biobb_morph/blob/master/biobb_morph/test/data/config/config_morph.yml)
```python
properties:
    m: 5
    i: 4
    a: 'abaqus'
    b: 'bcpd'
    e: 2
    r: 1
    w: 0
    y: 1
    f: 1
    c: 1
    d: 1
    CEP: 0
    lambdaBeta: 'lambdaBeta.csv'
    TZ: 1
    v: [0, 0, 0.04]
    n: 0.4
    t: [0.0, 24.1397991, 2.94929004]
    p: [1, 1, 0]
    s: 0.8
```
#### Command line
```python
morph --fileIn models/IVD_L1L2_NC0031.txt -m 1 -i 4 -a abaqus -b bcpd --CEP 1 -d 1 --lambdaBeta lambdaBeta.csv --TZ 1
```
