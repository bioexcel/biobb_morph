#!/usr/bin/env python3

import time
import argparse
import os
import sys
import shutil
from pathlib import Path, PurePath


#from biobb_morph import biobb_morph
from biobb_morph import morph
from biobb_morph.morph import common
from biobb_morph.morph import morph
from biobb_morph.morph.morph import morphing
from biobb_common.configuration import settings
from biobb_common.tools import file_utils as fu


def prep_output(destination, source):
    wdir = PurePath(source).parents[3]
    output_dir = os.path.join(wdir, destination)
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)
    #print (wdir, output_dir)
    #print (source)
    #print (wdir, source, destination)
    #print (wdir, weights_dir)
    #print (source)
    shutil.copytree(source, output_dir)
    if os.path.isdir(weights_dir):
        print ("File copied.")
    else:
        print ("Some error.")



def main(config, system=None):
    start_time= time.time()
    #conf = settings.ConfReader(args.config_path)
    #print (conf)
    #global_log, _ = fu.get_logs(path=conf.get_working_dir_path(), light_format=True)
    #global_prop = conf.get_prop_dic(global_log=global_log)
    #global_paths = conf.get_paths_dic()
    conf = settings.ConfReader(config, system)
    global_log, _ = fu.get_logs(path=conf.get_working_dir_path(), light_format=True)
    global_prop = conf.get_prop_dic(global_log=global_log)
    global_paths = conf.get_paths_dic()
    
    #global_log.info("step1_morphing: paths and prop {} ".format(global_prop["step1_morphing"]))
    
    input_file_path1 = global_paths["step1_morphing"]["input_file_path1"]
    global_log.info("step1_morphing: input {}".format(global_paths["step1_morphing"]))

    global_log.info("step1_morphing: Running 3D Meshes")
    morph.morphing(**global_paths["step1_morphing"], properties=global_prop["step1_morphing"])

    elapsed_time = time.time() - start_time
    global_log.info('')
    global_log.info('')
    global_log.info('Execution successful: ')
    global_log.info('  Workflow_path: %s' % conf.get_working_dir_path())
    global_log.info('  Config File: %s' % args.config_path)
    if args.system:
        global_log.info('  System: %s' % system)
    global_log.info('')
    global_log.info('Elapsed time: %.1f minutes' % (elapsed_time/60))
    global_log.info('')

    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Based on the official BioBB tutorial")
    parser.add_argument('--config', required=True)
    parser.add_argument('--system', required=False)
    #parser.add_argument('--output_file_path', dest='output_file_path', required=False)
    args = parser.parse_args()
    main(args.config, args.system)
