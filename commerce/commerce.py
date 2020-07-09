import sys
import os
import subprocess

if __name__ == "__main__":
    # Make sure correct number of arguments is correct
    if len(sys.argv) != 2:
        print("Usage: python commerce.py directory")

    # Get folder from command line argument and go into the 'auctions' app
    original_folder = os.getcwd()
    folder = sys.argv[1]
    base_folder = f"{os.getcwd()}/{folder}"
    os.chdir(f"{base_folder}/auctions/")

    # Remove any current migrations for a clean slate
    print("removing current migrations...")
    subprocess.run(["rm", "-r", "migrations/"])

    # Change to base folder and make migrations
    os.chdir(base_folder)
    print("Making migrations...")
    subprocess.run(["python3", "manage.py", "makemigrations", "auctions"])
    subprocess.run(["python3", "manage.py", "makemigrations"])

    # Migrating
    print("Migrating...")
    subprocess.run(["python3", "manage.py", "migrate"])

    # Inserting a file in the app that will run a command
    print("Adding manage.py command...")
    os.chdir(f"{base_folder}/auctions/")
    subprocess.run(["mkdir", "management"])
    os.chdir(f"{base_folder}/auctions/management/")
    subprocess.run(["mkdir", "commands"])
    os.chdir(original_folder)
    subprocess.run(["cp", "createusers.py", f"{folder}/auctions/management/commands/"])

    # Adding two users to the app
    print("Adding two users to the application...")
    os.chdir(base_folder)
    subprocess.run(["python3", "manage.py", "createusers"])

    # Starting the server
    print("Starting server...")
    subprocess.run(["python3", "manage.py", "runserver"])