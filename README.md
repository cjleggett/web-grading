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

* Purpose: Clears out and remakes migrations, then creates two users with simple usernames/passwords (eg: `a` and `a`) so the grader does not have to create users using the register page.
* Usage: It is assumed that within `<directory_name>`, there is a `manage.py` file and an app called `auctions`. It is also assumed that both files in the `commerce` directory (`commerce.py` and `createusers.py`) are included in the directory in which the command is run.

```bash
python commerce.py <directory_name>
```
