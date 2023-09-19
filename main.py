#Mousa DIALLO MASTER 2
import os
import argparse


parser = argparse.ArgumentParser(description = "Application for folder and files creator for you data works")

parser.add_argument('path', help = 'the path to the folder')

args = parser.parse_args()

from pathlib import Path

def create_project_structure(project_root):
    # Chemin racine du projet
    #project_root = Path("data_analysis_project")

    # Répertoires de premier niveau
    data_dir = project_root / "data"
    docs_dir = project_root / "docs"
    models_dir = project_root / "models"
    notebooks_dir = project_root / "notebooks"
    reports_dir = project_root / "reports"
    src_dir = project_root / "src"
    requirement = project_root/"requirement.txt"
    # Sous-répertoires de data/
    data_cleaned_dir = data_dir / "cleaned"
    data_raw_dir = data_dir / "raw"
    data_processed_dir = data_dir / "processed"

    # Création de l'arborescence
    project_root.mkdir(exist_ok=True)
    data_dir.mkdir(exist_ok=True)
    docs_dir.mkdir(exist_ok=True)
    models_dir.mkdir(exist_ok=True)
    notebooks_dir.mkdir(exist_ok=True)
    reports_dir.mkdir(exist_ok=True)
    src_dir.mkdir(exist_ok=True)
    data_cleaned_dir.mkdir(exist_ok=True)
    data_raw_dir.mkdir(exist_ok=True)
    data_processed_dir.mkdir(exist_ok=True)

    # Création de quelques fichiers de démonstration
    main_notebook_file = notebooks_dir / "main.ipynb"
    utils_file = src_dir / "utils.py"
    process_file = src_dir / "process.py"
    train_file = src_dir / "train.py"

    main_notebook_file.touch()
    utils_file.touch()
    process_file.touch()
    train_file.touch()
    requirement.touch()

if __name__ == "__main__":
    try :
         given_Path = Path(args.path)
    except:
        given_Path = args.path
    create_project_structure(project_root=given_Path)
