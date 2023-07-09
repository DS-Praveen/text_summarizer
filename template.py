import os
from pathlib import Path
import logging

logging.basicConfig(level= logging.INFO, format= '[%(asctime)s]:  %(message)s:')

project_name = "TextSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb"

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok = True)
        logging.info(f"Creating directory {filedir} for the file {filename}")
    else:
        logging.info(f"{filedir} ... already exists")

    if (not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        with open(filename, 'w') as f:
            pass
            logging.info(f"Creating the empty file {filename}")
    else:
        logging.info(f"... {filename} ... already exists")


