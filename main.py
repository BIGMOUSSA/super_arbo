#Moussa DIALLO, MASTER 2 DATASCIENCE DIT
from utils import git_repo_init, create_project_data_path
import os
import argparse


parser = argparse.ArgumentParser(description = "Application for folder and files creator for you data works")

parser.add_argument('path', help = 'the path to the folder')

args = parser.parse_args()

class SuperFolder :
    
    def __init__(self, mypath) -> None:
        self.mypath = mypath

    def PathCreator(self):
        create_project_data_path(self.mypath)

    def Init(self):
        git_repo_init(self.mypath)

if  __name__ == '__main__':
    given_Path = args.path
    os.makedirs(given_Path, exist_ok=True)
    DataCreator1 = SuperFolder(given_Path)
    DataCreator1.PathCreator()
    DataCreator1.Init()