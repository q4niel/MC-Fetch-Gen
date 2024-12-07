from data import Data
from typing import List

class Shell:
    @staticmethod
    def echoList(label:str, links:List[str]) -> str:
        if len(links) == 0: return ""

        string:str = f"\necho {label}:\n"
        for l in links:
            string += f"echo \"==> {l}\"\n"

        return f"{string}echo\n"

    @staticmethod
    def curlToRelativeDirectory(dir:str, links:List[str]) -> str:
        return "" if len(links) == 0 else (
            f"    mkdir ./{dir}\n"
            f"    cd ./{dir}\n"
            f"{"".join(f"    curl -L -O {l}\n" for l in links)}"
            f"    cd ..\n"
            f"\n"
        )

    @staticmethod
    def decodeRelativeDirectory(dir:str) -> str:
        decodes:str = "".join(f"\n        new=$(echo \"$new\" | sed 's/{x[0]}/{x[1]}/g')" for x in [
            ["%2B", "+"],
            ["%20", " "],
            ["%28", "("],
            ["%29", ")"]
        ])

        return (
            f"\n    for file in ./{dir}/*; do"
            f"\n        new=$(echo \"$file\")"
            f"\n{decodes}\n"
            f"\n        if [[ \"$file\" != \"$new\" ]]; then"
            f"\n            mv \"$file\" \"$new\""
            f"\n        fi"
            f"\n    done\n"
        )

    @staticmethod
    def generate (
        scriptName:str,
        datapacks:List[str] = [],
        resourcepacks:List[str] = [],
        shaderpacks:List[str] = [],
        mods:List[str] = []
    ) -> None:
        with open(f"{Data.ProjectDirectory}/{Data.Name}-{Data.Version}/{Data.Name}-{Data.Version}-{scriptName}.sh", "w") as file:
            file.write("#!/bin/bash\n")
            file.write("clear\n")
            file.write("echo This script will download the following resources:\necho\n")

            file.write(Shell.echoList("Datapacks", datapacks))
            file.write(Shell.echoList("Resourcepacks", resourcepacks))
            file.write(Shell.echoList("Shaderpacks", shaderpacks))
            file.write(Shell.echoList("Mods", mods))

            file.write("\necho \"All resources are obtained from official sources.\"\n")
            file.write("echo \"==> Do you wish to download all the listed resources?\"\n")
            file.write("echo \"==> By selecting yes, you acknowledge that you understand all downloads are provided from official sources.\"\n")
            file.write("echo \"==> [Y]es [N]o\"\n")
            file.write("read -p \"==> \" downloadInput\n")

            file.write (
                f"if [[ \"$downloadInput\" =~ ^[Yy]([Ee][Ss]?)?$ ]]; then\n"
                f"    echo Starting downloads...\n"
                f"    mkdir {Data.Name}-{Data.Version}\n"
            )

            file.write(f"    cd {Data.Name}-{Data.Version}\n")

            file.write(Shell.curlToRelativeDirectory("datapacks", datapacks))
            file.write(Shell.curlToRelativeDirectory("resourcepacks", resourcepacks))
            file.write(Shell.curlToRelativeDirectory("shaderpacks", shaderpacks))
            file.write(Shell.curlToRelativeDirectory("mods", mods))

            if len(datapacks) != 0: file.write(Shell.decodeRelativeDirectory("datapacks"))
            if len(resourcepacks) != 0: file.write(Shell.decodeRelativeDirectory("resourcepacks"))
            if len(shaderpacks) != 0: file.write(Shell.decodeRelativeDirectory("shaderpacks"))
            if len(mods) != 0: file.write(Shell.decodeRelativeDirectory("mods"))

            file.write("    cd ..\n")

            file.write("fi\n")
            file.write("echo\n")

            file.write("echo \"Delete this script file?\"\n")
            file.write("echo \"==> [Y]es [N]o\"\n")
            file.write("read -p \"==> \" deleteInput\n")

            file.write (
                "if [[ \"$deleteInput\" =~ ^[Yy]([Ee][Ss]?)?$ ]]; then\n"
                "    rm -- \"$0\"\n"
                "fi"
            )
        return

def generateScripts() -> None:
    Shell.generate (
        "Server",
        datapacks = Data.DataPacks,
        mods = Data.ServerMods
    )

    Shell.generate (
        "Client",
        resourcepacks = Data.ResourcePacks,
        shaderpacks = Data.ShaderPacks,
        mods = Data.ClientMods
    )

    Shell.generate (
        "Full",
        datapacks = Data.DataPacks,
        resourcepacks = Data.ResourcePacks,
        shaderpacks = Data.ShaderPacks,
        mods = Data.AllMods
    )

    return