import sys
import subprocess

def main():
    if len(sys.argv[1:]) == 0:
        sys.argv.append('-h')

    # check that we have poetry installed
    # check that rag is installed in poetry env
    # ragcli checks that we are in a rag project

    subprocess.run(f'poetry run ragcli {" ".join(sys.argv[1:])}', shell=True)
