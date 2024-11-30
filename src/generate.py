from data import Data
from typing import List

def curlToDir(dir:str, link:str) -> str:
    return f"curl -L -o ./{dir}/$(basename {link}) {link}\n"

def replaceInFileName(dir:str, bad:str, good:str) -> str:
    return (
        f"\ncd ./{dir}"
        f"\nfor file in *; do"
        f"\n    if [[ \"$file\" == *\"{bad}\"* ]]; then"
        f"\n        new=$(echo \"$file\" | sed 's/{bad}/{good}/g')"
        f"\n        mv \"$file\" \"$new\""
        f"\n    fi"
        f"\ndone\n"
        f"cd .."
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
        file.write("#!/bin/bash\n\n")

        file.write("mkdir datapacks\n")
        file.write("mkdir resourcepacks\n")
        file.write("mkdir shaderpacks\n")
        file.write("mkdir mods\n\n")

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

        file.write("\nrm -- \"$0\"")
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