import os
import shutil
from data import Data
from generate import generateScripts

def makeBuildDir() -> None:
    if os.path.exists(f"{Data.ProjectDirectory}/{Data.Version}"):
        shutil.rmtree(f"{Data.ProjectDirectory}/{Data.Version}")

    os.makedirs(f"{Data.ProjectDirectory}/{Data.Version}")
    return

def main() -> None:
    Data.init()
    makeBuildDir()
    generateScripts()
    return

if __name__ == "__main__": main()