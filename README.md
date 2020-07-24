# CS50 Web Grading Tools

A set of tools meant to help a small bit in the grading process for CS50's web course

## Project 0: Search

* Purpose: Opens a file from within a folder using Google Chrome.
* Usage: If no file name is included, a default of `index.html` will be provided.

```bash
python search.py <directory_name> [file name]
```

## Project 1: Wiki

* Purpose: Clears out and remakes migrations before running the server
* Usage: It is assumed that within `<directory_name>`, there is a `manage.py` file and an app called `encyclopedia`.

```bash
python wiki.py <directory_name>
```

## Project 2: Commerce

* Purpose: Clears out and remakes migrations, then creates three users with simple usernames/passwords, one of which is a superuser, so the grader does not have to create users using the register page.
* Usage: It is assumed that within `<directory_name>`, there is a `manage.py` file and an app called `auctions`. It is also assumed that both files in the `commerce` directory (`commerce.py` and `createusers.py`) are included in the directory in which the command is run.

```bash
python commerce.py <directory_name>
```

## Project 3: Mail

* Purpose: Clears out and remakes migrations, then creates three users with simple usernames/passwords so the grader does not have to create users using the register page. No superuser is created here, as admin setup is not a requirement.
* Usage: It is assumed that within `<directory_name>`, there is a `manage.py` file and an app called `mail`. It is also assumed that both files in the `mail` directory (`mail.py` and `createusers.py`) are included in the directory in which the command is run.
* Note: Here the username must be the same as the email

```bash
python mail.py <directory_name>
```
