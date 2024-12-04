from data import Data
from typing import List

def echoList(label:str, links:List[str]) -> str:
    if len(links) == 0: return ""

    string:str = f"\necho {label}:\n"
    for l in links:
        string += f"echo \"==> {l}\"\n"

    return f"{string}echo\n"

def curlToDir(dir:str, link:str) -> str:
    return f"    curl -L -o ./{dir}/$(basename {link}) {link}\n"

def replaceInFileName(dir:str, bad:str, good:str) -> str:
    return (
        f"\n    cd ./{dir}"
        f"\n    for file in *; do"
        f"\n        if [[ \"$file\" == *\"{bad}\"* ]]; then"
        f"\n            new=$(echo \"$file\" | sed 's/{bad}/{good}/g')"
        f"\n            mv \"$file\" \"$new\""
        f"\n        fi"
        f"\n    done\n"
        f"    cd ..\n"
    )

def makeShell (
    name:str,
    filterDirs:List[str],
    datapacks:List[str] = [],
    resourcepacks:List[str] = [],
    shaderpacks:List[str] = [],
    mods:List[str] = []
) -> None:
    with open(f"{Data.ProjectDirectory}/{Data.Version}/{name}-{Data.Version}.sh", "w") as file:
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
        )

        if len(datapacks) != 0: file.write("    mkdir datapacks\n")
        if len(resourcepacks) != 0: file.write("    mkdir resourcepacks\n")
        if len(shaderpacks) != 0: file.write("    mkdir shaderpacks\n")
        if len(mods) != 0: file.write("    mkdir mods\n")

        for link in datapacks:
            file.write(curlToDir("datapacks", link))
        file.write("\n")

        for link in resourcepacks:
            file.write(curlToDir("resourcepacks", link))
        file.write("\n")

        for link in shaderpacks:
            file.write(curlToDir("shaderpacks", link))
        file.write("\n")

        for link in mods:
            file.write(curlToDir("mods", link))
        file.write("\n")

        for dir in filterDirs:
            file.write(replaceInFileName(dir, "%2B", "+"))
            file.write(replaceInFileName(dir, "%20", " "))
            file.write(replaceInFileName(dir, "%28", "("))
            file.write(replaceInFileName(dir, "%29", ")"))

        file.write("fi\n")
        file.write("echo\n")

        file.write("echo \"Delete this script file?\"\n")
        file.write("echo \"==> [Y]es [N]o\"\n")
        file.write("read -p \"==> \" deleteInput\n")

        file.write (
            f"if [[ \"$deleteInput\" =~ ^[Yy]([Ee][Ss]?)?$ ]]; then\n"
            f"    rm -- \"$0\"\n"
            f"fi"
        )
    return

def generateScripts() -> None:
    makeShell (
        "Server",
        ["datapacks", "mods"],
        datapacks = Data.DataPacks,
        mods = Data.ServerMods
    )

    makeShell (
        "Client",
        ["resourcepacks", "shaderpacks", "mods"],
        resourcepacks = Data.ResourcePacks,
        shaderpacks = Data.ShaderPacks,
        mods = Data.ClientMods
    )

    makeShell (
        "Full",
        ["datapacks", "resourcepacks", "shaderpacks", "mods"],
        datapacks = Data.DataPacks,
        resourcepacks = Data.ResourcePacks,
        shaderpacks = Data.ShaderPacks,
        mods = Data.AllMods
    )

    return