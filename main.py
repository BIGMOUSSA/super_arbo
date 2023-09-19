from utils import git_repo_init, create_project_data_path
import os
import argparse


parser = argparse.ArgumentParser(description = "Application for folder and files creator for you data works")

parser.add_argument('path', help = 'the path to the folder')

args = parser.parse_args()

from pathlib import Path

def create_project_structure():
    # Chemin racine du projet
    project_root = Path("data_analysis_project")

    # Répertoires de premier niveau
    data_dir = project_root / "data"
    docs_dir = project_root / "docs"
    models_dir = project_root / "models"
    notebooks_dir = project_root / "notebooks"
    reports_dir = project_root / "reports"
    src_dir = project_root / "src"

    # Sous-répertoires de data/
    data_cleaned_dir = data_dir / "cleaned"
    data_raw_dir = data_dir / "raw"

    # Création de l'arborescence
    project_root.mkdir()
    data_dir.mkdir()
    docs_dir.mkdir()
    models_dir.mkdir()
    notebooks_dir.mkdir()
    reports_dir.mkdir()
    src_dir.mkdir()
    data_cleaned_dir.mkdir()
    data_raw_dir.mkdir()

    # Création de quelques fichiers de démonstration
    main_notebook_file = notebooks_dir / "main_notebook.ipynb"
    utils_file = src_dir / "utils.py"

    main_notebook_file.touch()
    utils_file.touch()

if __name__ == "__main__":
    given_Path = args.path
    create_project_structure()
