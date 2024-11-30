from typing import List
import sys
import json

class Data:
    ProjectDirectory:str = (sys.argv[0])[:-5]
    Version:str = ""

    DataPacks:List[str] = []
    ResourcePacks:List[str] = []
    ShaderPacks:List[str] = []

    AllMods:List[str] = []
    ClientMods:List[str] = []
    ServerMods:List[str] = []

    @staticmethod
    def init() -> None:
        with open(f"{Data.ProjectDirectory}/mcfg.json", "r") as file:
            data = json.load(file)
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