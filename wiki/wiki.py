import sys
import os
import subprocess

if __name__ == "__main__":
    # Make sure correct number of arguments is correct
    if len(sys.argv) != 2:
        print("Usage: python wiki.py directory")

    # Get folder from command line argument and go into the 'encyclopedia' app
    folder = sys.argv[1]
    base_folder = f"{os.getcwd()}/{folder}"
    os.chdir(f"{base_folder}/encyclopedia/")

    # Remove any current migrations for a clean slate
    print("removing current migrations...")
    subprocess.run(["rm", "-r", "migrations/"])

    # Change to base folder and make migrations
    os.chdir(base_folder)
    print("Making migrations...")
    subprocess.run(["python3", "manage.py", "makemigrations", "encyclopedia"])

    # Migrating
    print("Migrating...")
    subprocess.run(["python3", "manage.py", "migrate"])

    # Starting the server
    print("Starting server...")
    subprocess.run(["python3", "manage.py", "runserver"])