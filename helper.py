import argparse
import os.path
import subprocess
import sys
import textwrap
import venv

# Current working directory
THIS_DIR = os.path.dirname(__file__)
# Virtual environment path
VENV_PATH = os.path.join(THIS_DIR, "venv")
# Pip executable path
PIP_EXE = os.path.join(VENV_PATH, "Scripts", "pip.exe")
# Python executable (in venv)
PYTHON_EXE = os.path.join(VENV_PATH, "Scripts", "python.exe")
# Requirements file
REQ_TXT = os.path.join(THIS_DIR, "requirements.txt")
# Python executable (in venv)
MAIN_FILE = os.path.join(THIS_DIR, "app.py")
# Description to display in help
DESCRIPTION = textwrap.dedent(''''\
    Junior DevOps Engineer Assignment
    --------------------------------
    This script can be used to create/clean the python environment
    and install required packages to run the server application.
    --------------------------------
    ''')


def check_files_exist(files):
    """
    Checks whether given files exist or not.

    :param files: file list to check
    :raises: FileNotFoundError if as file is not found.
    """
    for file in files:
        if not os.path.isfile(file):
            raise FileNotFoundError(f"No such file: '{file}'")


def run_subprocess(command):
    """
    Runs subprocess.
    :param command: command to run (list of str)
    :raises: ValueError if return code is not 0 (zero).

    """
    result = subprocess.call(command)
    if result:
        raise ValueError(f'Non-zero exit code from subprocess: {result}')


def create_venv():
    """
    Creates virtual environment.

    Deletes previous one if there is any.

    """
    print("Creating virtual environment...")
    builder = venv.EnvBuilder(system_site_packages=False, clear=True, with_pip=True)
    builder.create(VENV_PATH)
    print("OK")


def install_packages():
    """
    Installs all required packages define in REQ_TXT (requirement.txt).
    """
    print("Installing required packages...")
    check_files_exist([PIP_EXE, REQ_TXT])
    run_subprocess([PIP_EXE, 'install', '-r', REQ_TXT])
    print("OK")


def create_env_and_install_packages():
    """
    Create virtual environment and install packages.

    """
    create_venv()
    install_packages()


def run_server():
    """
    Runs the Flask server.

    """
    print("Running server...")
    check_files_exist([PYTHON_EXE, MAIN_FILE])
    run_subprocess([PYTHON_EXE, '-u', MAIN_FILE])


if __name__ == '__main__':
    rc = 1
    try:
        parser = argparse.ArgumentParser(description=DESCRIPTION, formatter_class=argparse.RawTextHelpFormatter)
        group = parser.add_mutually_exclusive_group()
        group.add_argument("--create", action="store_true", help="Creates the environment on %s" % VENV_PATH)
        group.add_argument("--run", action="store_true", help="Runs the server.")
        # Parse given arguments
        args = parser.parse_args()
        if args.create:
            print("WARNING: Creation deletes previously installed venv.")
            create_env_and_install_packages()
        if args.run:
            run_server()
        else:
            parser.print_help(sys.stderr)
            raise ValueError("No option given.")
        print("----------\nScript ran successfully.\n----------")
        rc = 0
    except Exception as e:
        print('----------\nError: %s\n----------' % e, file=sys.stderr)

    sys.exit(rc)
