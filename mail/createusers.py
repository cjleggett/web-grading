# Necessary imports
from django.core.management.base import BaseCommand, CommandError
from mail.models import User

# Creating a command for manage.py to run
class Command(BaseCommand):

    # Documentation for new users
    help = "Creates users with simple emails/passwords"

    # Function to be run when 'python manage.py createusers' is run
    def handle(self, *args, **options):

        # Number of users created so far
        created = 0

        # Loop through letters of the alphabet
        for name in [chr(i) for i in range(97, 97 + 26)]:

            # Try to save the user and write success message
            try:
                user = User.objects.create_user(name, f"{name}@cs50.net", name)
                user.save()
                self.stdout.write(self.style.SUCCESS(f"Successfully created user {name} with password {name} and email {name}@cs50.net"))
                created += 1
                if created == 2:
                    return
            
            # I fusername is taken, print a notice
            except:
                self.stdout.write(f"User {name} already taken. Trying again...")
            
        # Raise exception if two users couldn't be created:
        raise AssertionError("All letters already taken!")
