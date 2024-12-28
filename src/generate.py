from data import Data
from typing import List

def mainHead() -> str:
    return "def main() -> None:\n"

def mainTail() -> str:
    return (
        "    return\n\n"
        "if __name__ == \"__main__\": main()"
    )

def indented(indent:int, lines:List[str]) -> str:
    final:str = ""

    for line in lines:
        for i in range(indent):
            final += " "
        final += f"{line}\n"

    return final

def generate() -> None:
    with open(f"{Data.ProjectDirectory}/gen.py", "w") as file:
        file.write(mainHead())

        file.write(indented(4, [
            "print(\"hello world\")"
        ]))

        file.write(mainTail())

    return