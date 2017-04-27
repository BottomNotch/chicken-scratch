import subprocess

def extract(tarbell):
#    returncode = 0
    try:
        subprocess.run(["tar", "-xvf", tarbell], check=True)
    except subprocess.CalledProcessError as e:
        returncode = e.returncode
        print("error: tar exited with code " + str(returncode))

    return returncode
