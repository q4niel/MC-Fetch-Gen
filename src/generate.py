from data import Data
from typing import List

def echoList(label:str, links:List[str]) -> str:
    if len(links) == 0: return ""

    string:str = f"\necho {label}:\n"
    for l in links:
        string += f"echo \"==> {l}\"\n"

    return f"{string}echo\n"

def curlToRelativeDirectory(dir:str, links:List[str]) -> str:
    return "" if len(links) == 0 else (
        f"    mkdir ./{dir}\n"
        f"{"".join(f"    curl -L -o ./{dir}/$(basename {l}) {l}\n" for l in links)}"
        f"\n"
    )

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

def makeShell (
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

        file.write(echoList("Datapacks", datapacks))
        file.write(echoList("Resourcepacks", resourcepacks))
        file.write(echoList("Shaderpacks", shaderpacks))
        file.write(echoList("Mods", mods))

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

        file.write(curlToRelativeDirectory("datapacks", datapacks))
        file.write(curlToRelativeDirectory("resourcepacks", resourcepacks))
        file.write(curlToRelativeDirectory("shaderpacks", shaderpacks))
        file.write(curlToRelativeDirectory("mods", mods))

        if len(datapacks) != 0: file.write(decodeRelativeDirectory("datapacks"))
        if len(resourcepacks) != 0: file.write(decodeRelativeDirectory("resourcepacks"))
        if len(shaderpacks) != 0: file.write(decodeRelativeDirectory("shaderpacks"))
        if len(mods) != 0: file.write(decodeRelativeDirectory("mods"))

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
    makeShell (
        "Server",
        datapacks = Data.DataPacks,
        mods = Data.ServerMods
    )

    makeShell (
        "Client",
        resourcepacks = Data.ResourcePacks,
        shaderpacks = Data.ShaderPacks,
        mods = Data.ClientMods
    )

    makeShell (
        "Full",
        datapacks = Data.DataPacks,
        resourcepacks = Data.ResourcePacks,
        shaderpacks = Data.ShaderPacks,
        mods = Data.AllMods
    )

    return