import subprocess
import os


def shuffle_library():
    os.system('clear')
    subprocess.run(
        ["mpc clear"],
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True
    )
    subprocess.run(
        ["mpc searchadd artist ''"],
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True
    )
    subprocess.run(
        ["mpc shuffle"],
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True
    )
    subprocess.run(
        ["mpc play"],
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True
    )
    os.system('clear')
