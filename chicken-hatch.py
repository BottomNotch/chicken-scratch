#!/usr/bin/python3

import argparse
import subprocess

parser = argparse.ArgumentParser(
    description="build, install, and load packages")
sub_commands = parser.add_subparsers()

#the four main operations
hatch = sub_commands.add_parser("hatch",
                                description="build and install packages")
cull = sub_commands.add_parser("cull",
                               description="remove packages")
integrate = sub_commands.add_parser("integrate",
                                    description="load packages into the system")
isolate = sub_commands.add_parser("isolate",
                                  description="unload packages from the system")

#hatch arguments
hatch.add_argument("-n", "--name", required=True,
                   help="name of package to install")
hatch.add_argument("-v", "--package-version", required=True,
                   help="version of package to be installed")
source_location = hatch.add_mutually_exclusive_group(required=True)
source_location.add_argument("-t", "--tar", metavar="ARCHIVE",
                             help="use tar to extract source from an archive")
source_location.add_argument("-x", "--extract-only", metavar="ARCHIVE",
                             help=("use tar to extract source from an archive "
                                  "and don't compile the package"))
source_location.add_argument("-d", "--source-directory", metavar="DIRECTORY",
                             help=("build package from it's source is the "
                             "given directory"))
args = parser.parse_args()
