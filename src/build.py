import subprocess
import shutil
import os
from typing import List
from data import Data

def cmd(args:List[str], shell=False) -> bool:
    try:
        subprocess.check_output(args, text=True, shell=shell)
        return True
    except subprocess.CalledProcessError:
        return False

def cleanup() -> None:
    cwd:str = os.getcwd()

    shutil.rmtree(f"{cwd}/build/gen")
    if len(os.listdir(f"{cwd}/build")) == 0:
        shutil.rmtree(f"{cwd}/build")

    match os.name:
        case "nt":
            shutil.move(f"{cwd}/dist/gen.exe", f"{Data.ProjectDirectory}/{Data.Name}-{Data.Version}-Installer.exe")
        case "posix":
            shutil.move(f"{cwd}/dist/gen", f"{Data.ProjectDirectory}/{Data.Name}-{Data.Version}-Installer")
        case _:
            print("Unsupported OS")

    shutil.rmtree(f"{cwd}/dist")

    os.remove(f"{cwd}/gen.spec")

    os.remove(f"{Data.ProjectDirectory}/gen.py")
    return

def build() -> None:
    match os.name:
        case "nt":
            cmd(["py", "-3", "-m", "PyInstaller", f"{Data.ProjectDirectory}/gen.py", "--onefile"])
        case "posix":
            cmd(["python3", "-m", "PyInstaller", f"{Data.ProjectDirectory}/gen.py", "--onefile"])
        case _:
            print("Unsupported OS")
    cleanup()
    return