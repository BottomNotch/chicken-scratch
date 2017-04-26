#!/usr/bin/python3

import argparse
import subprocess

parser = argparse.ArgumentParser(
    description="build, install, and load packages")
sub_commands = parser.add_subparsers()
hatch = sub_commands.add_parser("hatch",
                                description="build and install packages")
cull = sub_commands.add_parser("cull",
                               description="remove packages")
integrate = sub_commands.add_parser("integrate",
                                    description="load packages into the system")
isolate = sub_commands.add_parser("isolate",
                                  description="unload packages from the system")

args = parser.parse_args()
