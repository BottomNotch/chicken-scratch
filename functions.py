import subprocess
from pathlib import Path
import os

def extract(tarbell):
    try:
        subprocess.run(["tar", "-xvf", tarbell], check=True)
    except subprocess.CalledProcessError as e:
        returncode = e.returncode
        print("error: tar exited with code " + str(returncode))

    return returncode

def build(source_root : Path, seperate_build_dir : bool, config_command : list,
          config_only : bool, build_command : list):

    #some packages require building in a directory other than the source's root
    if(separate_build_dir):
        build_dir = Path(source_root / "build")
    else:
        build_dir = source_root

    #make sure the build directory exist beore making it the working directory
    if(build_dir.exists()):
        os.chdir(build_dir)
    else:
        print("build directory doesn't exist")
        return 1

    #configure the source
    try:
        subprocess.run(config_command)
    except subprocess.CalledProcessError as e:
        print("error: " + str(config_command[0]) +
              " exited " + str(e.returncode))
        return 2

    print("source configuration succesfull")

    #build source (unless config_only is true)
    if(not config_only):
        try:
            subprocces.run(build_command)
        except subprocess.CalledProcessError as e:
            print("error: " + str(build_command[0]) +
                  "exited " + str(e.returncode))
            return 3
        print("build successfull")
    return 0
