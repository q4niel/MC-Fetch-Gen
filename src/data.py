from typing import List
import sys
import json

class Data:
    ProjectDirectory:str = (sys.argv[0])[:-5]
    Version:str = ""
    Client:List[str] = []
    Server:List[str] = []
    Both:List[str] = []

    @staticmethod
    def init() -> None:
        with open(f"{Data.ProjectDirectory}/mcfg.json", "r") as file:
            data = json.load(file)
            Data.Version = data["version"]
            Data.Client = data["client"]
            Data.Server = data["server"]
            Data.Both = data["both"]
        return