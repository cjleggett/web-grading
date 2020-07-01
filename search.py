import sys
import os
import subprocess

if __name__ == "__main__":
    if len(sys.argv) > 3 or len(sys.argv) < 2:
        print("Usage: python run.py directory [initial file]")

    try:
        initial_file = sys.argv[2]
    except IndexError:
        initial_file = "index.html"

    folder = sys.argv[1]
    base_folder = os.getcwd() + "/" + folder
    os.chdir(base_folder)
    subprocess.run(["open", "-a", "Google Chrome", initial_file])
