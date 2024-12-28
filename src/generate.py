from data import Data
from typing import List
import io

def imports() -> str:
    return (
        "import os\n"
        "from typing import List\n"
        "import urllib.request\n"
        "import urllib.parse\n"
        "import urllib.error\n"
        "\n"
    )

def downloadDefinition() -> str:
    return (
        "def download(url:str, dst:str) -> None:\n"
        "    try:\n"
        "        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})\n"
        "        with urllib.request.urlopen(req) as response:\n"
        "            if response.status != 200:\n"
        "                print(f\"Failed to download. Status code: {response.status}\")\n"
        "                return\n"
        "\n"
        "            filename = os.path.basename(urllib.parse.urlparse(url).path)\n"
        "            filePath = os.path.join(dst, filename)\n"
        "\n"
        "            with open(filePath, \"wb\") as file:\n"
        "                while chunk := response.read(1024):\n"
        "                    file.write(chunk)\n"
        "\n"
        "            print(f\"Downloaded {filename} successfully!\")\n"
        "\n"
        "    except urllib.error.HTTPError as e:\n"
        "        print(f\"HTTP error occurred: {e.code} - {e.reason}\")\n"
        "    except urllib.error.URLError as e:\n"
        "        print(f\"URL error occurred: {e.reason}\")\n"
        "    except Exception as e:\n"
        "        print(f\"An unexpected error occurred: {e}\")\n"
        "\n"
        "    return\n\n"
    )

def mainHead() -> str:
    return "def main() -> None:\n"

def mainTail() -> str:
    return (
        "    return\n\n"
        "if __name__ == \"__main__\": main()"
    )

def indented(indent:int, lines:List[str], prefix:str = "", suffix:str = "") -> str:
    final:str = ""

    for line in lines:
        for i in range(indent):
            final += " "
        final += f"{prefix}{line}{suffix}\n"

    return final

def writeAssetCategory(file:io.IOBase, assets:List[str], varName:str) -> None:
    if len(assets) == 0: return

    list = f"{varName}:List[str] = [\n"
    list += indented(8, assets, "\"", "\",")
    list += "    ]"

    file.write(indented(4, [
        f"os.mkdir(f\"{{os.getcwd()}}/{Data.Name}-{Data.Version}/{varName}\")",
        f"{list}",
        f"for asset in {varName}:",
        f"    download(asset, f\"{{os.getcwd()}}/{Data.Name}-{Data.Version}/{varName}\")"
    ]))
    file.write("\n")

    return

def generate() -> None:
    with open(f"{Data.ProjectDirectory}/gen.py", "w") as file:
        file.write(imports())
        file.write(downloadDefinition())
        file.write(mainHead())

        file.write(indented(4, [f"os.mkdir(f\"{{os.getcwd()}}/{Data.Name}-{Data.Version}\")\n"]))

        writeAssetCategory(file, Data.DataPacks, "datapacks")
        writeAssetCategory(file, Data.ResourcePacks, "resourcepacks")
        writeAssetCategory(file, Data.ShaderPacks, "shaderpacks")
        writeAssetCategory(file, Data.AllMods, "mods")

        file.write(indented(4, [
            f"for root, subs, files in os.walk(f\"{{os.getcwd()}}/{Data.Name}-{Data.Version}\"):",
            "    for file in files:",
            "        os.rename(f\"{root}/{file}\", f\"{root}/{urllib.parse.unquote(file)}\")\n",
        ]))

        file.write(mainTail())

    return