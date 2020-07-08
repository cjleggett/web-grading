# CS50 Web Grading Tools

A set of tools meant to help a small bit in the grading process for CS50's web course

## Project 0: Search

### Purpose

Opens a file from within a folder using Google Chrome.

### Usage

```bash
python search.py <directory_name> [file name]
```

If no file name is included, a default of `index.html` will be provided.

## Project 1: Wiki

### Purpose

Clears out and remakes migrations before running the server

### Usage

```bash
python wiki.py <directory_name>
```

It is assumed that within `<directory_name>`, there is a `manage.py` file and an app called `encyclopedia`.