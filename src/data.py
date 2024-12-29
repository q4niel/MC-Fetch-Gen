from typing import List
import os
import sys
import json

class Data:
    ProjectDirectory:str = ""
    Name:str = ""
    Version:str = ""

    DataPacks:List[str] = []
    ResourcePacks:List[str] = []
    ShaderPacks:List[str] = []

    AllMods:List[str] = []
    ClientMods:List[str] = []
    ServerMods:List[str] = []

    @staticmethod
    def init() -> None:
        match os.name:
            case "nt":
                Data.ProjectDirectory = (os.path.abspath(sys.argv[0]))[:-8]
            case "posix":
                Data.ProjectDirectory = (os.path.abspath(sys.argv[0]))[:-5]
            case _:
                print("Unsupported OS")

        with open(f"{Data.ProjectDirectory}/mcfg.json", "r") as file:
            data = json.load(file)
            Data.Name = data["name"]
            Data.Version = data["version"]

            Data.DataPacks = data["datapacks"]
            Data.ResourcePacks = data["resourcepacks"]
            Data.ShaderPacks = data["shaderpacks"]

            Data.ClientMods = data["mods"]["client"]
            Data.ServerMods = data["mods"]["server"]

            for mod in Data.ClientMods:
                Data.AllMods.append(mod)

            for mod in Data.ServerMods:
                Data.AllMods.append(mod)

            for mod in data["mods"]["dual"]:
                Data.ClientMods.append(mod)
                Data.ServerMods.append(mod)
                Data.AllMods.append(mod)
        return