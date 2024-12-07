import sys
import os
import shutil
from data import Data
from generate import generateScripts

def makeBuildDir() -> None:
    if os.path.exists(f"{Data.ProjectDirectory}/{Data.Name}-{Data.Version}"):
        shutil.rmtree(f"{Data.ProjectDirectory}/{Data.Name}-{Data.Version}")

    os.makedirs(f"{Data.ProjectDirectory}/{Data.Name}-{Data.Version}")
    return

def main() -> None:
    if len(sys.argv) >= 2:
        if sys.argv[1] == "-version" or sys.argv[1] == "--version":
            print("MC Fetch Gen - Version: 0.1.1")
            return

    Data.init()
    makeBuildDir()
    generateScripts()
    return

if __name__ == "__main__": main()