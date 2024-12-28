import sys
from data import Data
from generate import generate
from build import build

def main() -> None:
    if len(sys.argv) >= 2:
        if sys.argv[1] == "--version":
            print("MC Fetch Gen - Version: 0.2.0")
            return

    Data.init()
    generate()
    build()
    return

if __name__ == "__main__": main()