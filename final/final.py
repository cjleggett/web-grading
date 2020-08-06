import sys
import os
import subprocess
import re

if __name__ == "__main__":
    # Make sure correct number of arguments is correct
    if len(sys.argv) not in  {3, 4}:
        print("Usage: python final.py directory app_name [no_users (1/0)]")

    # Get folder from command line argument and go into the student's app
    original_folder = os.getcwd()
    folder = sys.argv[1]
    app_name = sys.argv[2]
    base_folder = f"{os.getcwd()}/{folder}"
    os.chdir(f"{base_folder}/{app_name}/")

    # Remove any current migrations for a clean slate
    print("removing current migrations...")
    subprocess.run(["rm", "-r", "migrations/"])

    # Change to base folder and make migrations
    os.chdir(base_folder)
    print("Making migrations...")
    subprocess.run(["python3", "manage.py", "makemigrations", app_name])
    subprocess.run(["python3", "manage.py", "makemigrations"])

    # Migrating
    print("Migrating...")
    subprocess.run(["python3", "manage.py", "migrate"])

    # Check if users should be added to app using the final command line argument
    try:
        skip_add = bool(int(sys.argv[3]))
    except:
        skip_add = False

    if not skip_add:
        # Inserting a file in the app that will run a command
        print("Adding manage.py command...")
        os.chdir(f"{base_folder}/{app_name}/")
        subprocess.run(["mkdir", "management"])
        os.chdir(f"{base_folder}/{app_name}/management/")
        subprocess.run(["mkdir", "commands"])
        os.chdir(original_folder)
        subprocess.run(["cp", "createusers.py", f"{folder}/{app_name}/management/commands/"])
        
        # Edit the new file to adjust to the student's app name
        with open(f"{folder}/{app_name}/management/commands/createusers.py", "r") as f:
            contents = f.read()
            new_contents = re.sub(r"APP_NAME", app_name, contents)
        with open(f"{folder}/{app_name}/management/commands/createusers.py", "w") as f:
            f.write(new_contents)

        # Adding two users to the app
        print("Adding users to the application...")
        os.chdir(base_folder)
        subprocess.run(["python3", "manage.py", "createusers"])

    # Starting the server
    print("Starting server...")
    subprocess.run(["python3", "manage.py", "runserver"])