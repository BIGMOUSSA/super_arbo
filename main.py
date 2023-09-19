from utils import git_repo_init, create_project_data_path
import os

class SuperFolder :
    
    def __init__(self, mypath) -> None:
        self.mypath = mypath

    def PathCreator(self):
        create_project_data_path(self.mypath)

    def Init(self):
        git_repo_init(self.mypath)

if  __name__ == '__main__':
    #os.mkdir("testFolderPath3")

    testPath = "test_m1"
    os.makedirs(testPath, exist_ok=True)
    DataCreator1 = SuperFolder(testPath)
    DataCreator1.PathCreator()
    DataCreator1.Init()