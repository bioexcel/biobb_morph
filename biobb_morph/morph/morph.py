#!/usr/bin/env python3

#Module from BioBB basics
from __future__ import print_function
import argparse
import shutil, glob
from pathlib import PurePath
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.configuration import settings
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger

#Modules for BioBB Morph

import pandas as pd
import numpy as np
import os
import csv
from common import *
from tqdm import tqdm
import subprocess
import math
import itertools
import meshio

from statistics import *

class Morph(BiobbObject):
    """
    | biobb_template Template
    | Short description for the `template <http://templatedocumentation.org>`_ module in Restructured Text (reST) syntax. Mandatory.
    | Long description for the `template <http://templatedocumentation.org>`_ module in Restructured Text (reST) syntax. Optional.

    Args:
        input_file_path1 (str): Description for the first input file path. File type: input. `Sample file <https://urlto.sample>`_. Accepted formats: top (edam:format_3881).
        input_file_path2 (str) (Optional): Description for the second input file path (optional). File type: input. `Sample file <https://urlto.sample>`_. Accepted formats: dcd (edam:format_3878).
        output_file_path (str): Description for the output file path. File type: output. `Sample file <https://urlto.sample>`_. Accepted formats: zip (edam:format_3987).
        properties (dic):
            * **boolean_property** (*bool*) - (True) Example of boolean property.
            * **binary_path** (*str*) - ("zip") Example of executable binary property.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **sandbox_path** (*str*) - ("./") [WF property] Parent path to the sandbox directory.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_template.template.template import template

            prop = {
                'boolean_property': True
            }
            template(input_file_path1='/path/to/myTopology.top',
                    output_file_path='/path/to/newCompressedFile.zip',
                    input_file_path2='/path/to/mytrajectory.dcd',
                    properties=prop)

    Info:
        * wrapped_software:
            * name: Zip
            * version: >=3.0
            * license: BSD 3-Clause
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl
    """

    def __init__(self, input_file_path1, input_file_path2, output_file_path, properties=None, **kwargs) -> None:
        properties = properties or {}

        # 2.0 Call parent class constructor
        print (properties)
        super().__init__(properties)
        self.locals_var_dict = locals().copy()

        # Input/Output files
        self.io_dict = {
                'in': {'input_file_path1': input_file_path1, 'sources_path': input_file_path2},
                'out': {'output_file_path': output_file_path}
        }

        # Properties

        self.files = self.io_dict['in']['input_file_path1']
        self.morph = properties.get("morph", 5)
        self.toINP = properties.get("toINP", 4)
        self.abaqusCommand = properties.get("abaqusCommand", "gmsh")
        self.bcpdCommand = properties.get("bcpdCommand", "bcpd")
        self.checkFElem = properties.get("checkFElem", 2)
        self.rigid = properties.get("rigid", 1)
        self.WCEP = properties.get("WCEP", 0)
        self.interpo = properties.get("interpo", 1)
        self.fusion = properties.get("fusion", 1)
        self.surfRegCEP = properties.get("surfRegCEP", 1)
        self.checkHaus = properties.get("checkHaus", 1)
        self.regCEP = properties.get("CEP", 0)
        self.lambdaBetaFile = properties.get("lambdaBeta", "lambdaBeta.csv")
        self.CreateTZ = properties.get("TZ", 1)
        self.movement = properties.get("movement", [0, 0, 0.05])
        self.nodeDistance = properties.get("nodeDistance", 0.3)
        self.moveTo = properties.get("moveTo", [0.0, 24.1397991, 2.94929004])
        self.plane = properties.get("plane", [1, 1, 0])
        self.reduce_param = properties.get("reduce_param", 0.8)
        self.properties = properties

        # Check the properties
        self.check_properties(properties)
        # Check the arguments --> For what?
        #self.check_arguments()

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`Morph <biobb_morph.biobb_morph.Morph>` object."""

        if self.check_restart():
            return 0
        #
        self.stage_files()

        # Creating temporary folder
        self.tmp_folder = fu.create_unique_dir()
        fu.log('Creating %s temporary folder' % self.tmp_folder, self.out_log)

        #Setup paths as input arguments directly from self.io_dict
        sources_path = self.io_dict['in']['sources_path']
        results_path = self.io_dict['out']['output_file_path']
        
        print(f"Sources path: {sources_path}")
        print(f"Input file path 1: {self.io_dict['in']['input_file_path1']}")

        # Copy input_file_path1 to temporary folder
        shutil.copy(self.io_dict['in']['input_file_path1'], self.tmp_folder)

        # No need of command line parameters as instructions list
        instructions = []

        # Adding specific morphing properties

        morph_args = [
            self.io_dict['in']['input_file_path1'],
            sources_path,
            results_path,
            self.morph,
            self.WCEP,
            self.toINP,
            self.interpo,
            self.fusion,
            self.rigid,
            self.surfRegCEP,
            self.checkFElem,
            self.checkHaus,
            self.regCEP,
            self.nodeDistance,
            self.moveTo,
            self.movement,
            self.plane,
            self.reduce_param,
            self.CreateTZ,
            self.lambdaBetaFile,
            self.bcpdCommand,
            self.abaqusCommand
        ]

        #Executing the command line as a list of items (elements order will be maintained)
        
        fu.log('Executing the morph function with specified arguments', self.out_log, self.glob)
        morph(*morph_args)


        # Uncomment to check the command line
        #print(' '.join(cmd))
        # Copy files to host
        self.copy_to_host()

        # Remove temporary file(s)
        self.tmp_files.extend([
            self.stage_io_dict.get("unique_dir"),
            self.tmp_folder
        ])
        self.remove_tmp_files()

        # Check output arguments
        self.check_arguments(output_files_created=True, raise_exception=False)

        return self.return_code


def morphing(input_file_path1: str, input_file_path2: str, output_file_path: str, properties: dict = None, **kwargs) -> int:

    """Create :class:`Morph <biobb_morph.biobb_morph.Morph>` class and
    execute the :meth:`launch() <biobb_morph.biobb_morph.Morph.launch>` method."""

    return Morph(input_file_path1=input_file_path1,
                 input_file_path2=input_file_path2,
                 output_file_path=output_file_path,
                 properties=properties, **kwargs).launch()


def main():
    """Command line execution of this building block. Please check the command line documentation."""
    # argument administration
    parser = argparse.ArgumentParser(
        description="program that morph a template IVD mesh to a target, the patient-personalized model"
    )
    parser.add_argument(
        "--input_file_path1",
        help="info file that contains information about source and target",
        type=str,
        default="models/IVD_L1L2_NC0031.txt",
    )
    parser.add_argument(
        "-morph",
        metavar="",
        help="Non-Rigid registration mode. Options: 1: AF, 2: NP, 3: NoBEP, 4: CEPmorph, 5: All, 0: NONE",
        type=int,
        default=5,
    )
    parser.add_argument(
        "-toINP",
        metavar="",
        help="Create the .inp file for specific components. Options: 1: AF, 2: NP, 3: NoBEP, 4: All, 0: NONE",
        type=int,
        default=4,
    )
    parser.add_argument(
        "-abaqusCommand",
        metavar="",
        help="Command used to call ABAQUS. If '-a gmsh', the Gmsh tool is used.",
        type=str,
        default="abaqus",
    )
    parser.add_argument(
        "-bcpdCommand",
        metavar="",
        help="Command used to call BCPD++",
        type=str,
        default="bcpd",
    )
    parser.add_argument(
        "-checkFElem",
        metavar="",
        help="Check failed elements of the resulting .inp file (Abaqus required). Options: 1: YES, 2: Iterate value of lambda, 0: NO",
        type=int,
        default=2,
    )
    parser.add_argument(
        "-rigid",
        metavar="",
        help="Perform rigid registration at the beginning of the process. Options: 1: YES, 0: NO",
        type=int,
        default=1,
    )
    parser.add_argument(
        "-WCEP",
        metavar="",
        help="Perform morphing with CEP. Options: 1: YES, 0: NO",
        type=int,
        default=0,
    )
    parser.add_argument(
        "-interpo",
        metavar="",
        help="Use interpolated files. Options: 1: YES, 0: NO",
        type=int,
        default=1,
    )
    parser.add_argument(
        "-fusion",
        metavar="",
        help="Fuse the AF and NP for the final morph. Options: 1: YES, 0: NO",
        type=int,
        default=1,
    )
    parser.add_argument(
        "-surfRegCEP",
        metavar="",
        help="Morph external surfaces of AF and NP (including CEP). Options: 1: YES, 0: NO",
        type=int,
        default=1,
    )
    parser.add_argument(
        "-checkHaus",
        metavar="",
        help="Check Hausdorff distance between 3D grids (Euclidean distance). Options: 1: YES, 0: NO",
        type=int,
        default=1,
    )
    parser.add_argument(
        "--CEP",
        metavar="",
        help="Perform non-rigid registration of the CEP. Options: 1: YES, 0: NO",
        type=int,
        default=0,
    )
    parser.add_argument(
        "--lambdaBeta",
        metavar="",
        help="Text file with the alpha and beta values for non-rigid registration",
        type=str,
        default="lambdaBeta.csv",
    )
    parser.add_argument(
        "--TZ",
        metavar="",
        help="Create a Transition Zone. Options: 1: YES, 0: NO",
        type=int,
        default=1,
    )
    parser.add_argument(
        "-movement",
        nargs="+",
        type=float,
        help="Enter a list of floats separated by spaces to represent desired movement. Positive: positive direction, Negative: negative direction, 0: no movement",
        default=[0, 0, 0.05],
    )
    parser.add_argument(
        "-nodeDistance",
        metavar="",
        help="Distance between two nodes of the mesh",
        type=float,
        default=0.3,
    )
    parser.add_argument(
        "-moveTo",
        nargs="+",
        metavar="",
        help="Translation of the AF and NP",
        type=float,
        default=[0.0, 24.1397991, 2.94929004],
    )
    parser.add_argument(
        "-plane",
        nargs="+",
        metavar="",
        help="Plane to orthogonally project the nodes of the NP to create the spline line of the perimeter",
        type=int,
        default=[1, 1, 0],
    )
    parser.add_argument(
        "-reduce_param",
        metavar="",
        help="Parameter to reduce the size of the contour of the NP",
        type=float,
        default=0.8,
    )
    parser.add_argument(
        '--input_file_path2', metavar='', help='sources path', type=str, default='/sources')
    parser.add_argument(
        '--output_file_path', metavar='', help='output path', type=str, default='/results')
    parser.add_argument(
        '--config', metavar='', help='config', type=str, default='workflow.yml')

    args = parser.parse_args()
    args.config = args.config or "{}"

    properties = settings.ConfReader(config=args.config).get_prop_dic()

    #Matching to the Class constructor 
    #Specific call for building block

    morphing(input_file_path1=args.input_file_path1, input_file_path2=args.input_file_path2, output_path=args.output_path, properties=properties)


if __name__ == '__main__':
    main()

# 12. Complete documentation strings
