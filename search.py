# Necessary imports
import sys
import os
import subprocess

if __name__ == "__main__":

    # Make sure correct number of arguments is correct
    if len(sys.argv) > 3 or len(sys.argv) < 2:
        print("Usage: python run.py directory [initial file]")

    try:
        # Get file from command line argument
        initial_file = sys.argv[2]
    except IndexError:
        # If no file specified, use index.html
        initial_file = "index.html"

    # Get folder from command line argument
    folder = sys.argv[1]

    # Change directory into student's folder
    base_folder = os.getcwd() + "/" + folder
    os.chdir(base_folder)

    # Open the specified file in Google Chrome
    subprocess.run(["open", "-a", "Google Chrome", initial_file])
