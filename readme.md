
# MC Fetch Gen

This program automates the process of downloading various Minecraft-related assets, including datapacks, resourcepacks, shaderpacks, and mods. It reads a JSON file that specifies the assets to be downloaded, and generates a series of shell and batch scripts based on the information. These scripts, when run, will download the specified assets into your Minecraft directory.

## Features
- **Automatic script generation**: The program creates shell and batch scripts based on a JSON configuration file.
- **Customizable**: The JSON file can be edited to specify different assets to be downloaded.
- **Cross-platform**: The generated scripts are compatible with both Windows and Unix-like systems.

## Usage
### The generated scripts depend on curl.

1. **Download the Executable**
Download the latest release from the GitHub releases section.

3. **Configure your JSON File**
Create your JSON configuration file in the same directory as the executable.

4. **Running the Executable**
Run the executable. This will generate a new directory by your configuration within the same folder. Inside the build folder, you will find shell scripts (.sh) for Unix-like systems and batch scripts (.bat) for Windows. There will also be multiple script versions depending on your **Minecraft** environment: **server**, **client**, or **full**.

5. **Script Usage**
   Place the script within the Minecraft root folder, typically **.minecraft**.
   To start downloading the assets, simply run the script.
   - On Windows, choose the **.bat** files.
   - On Linux/macOS, choose the **.sh** files.

## JSON Configuration Example

```json
{
    "version": "0.0.0-1.21-Fabric",
    "datapacks": [],
    "resourcepacks": [],
    "shaderpacks": [
        "https://cdn.modrinth.com/data/ZvMtQlho/versions/XMIeWOv9/Bliss_v2.0.4_%28Chocapic13_Shaders_edit%29.zip"
    ],
    "mods": {
        "client": [
            "https://cdn.modrinth.com/data/AANobbMI/versions/b70slbHV/sodium-fabric-0.6.0%2Bmc1.21.1.jar",
            "https://cdn.modrinth.com/data/YL57xq9U/versions/MA2sKKaG/iris-fabric-1.8.0%2Bmc1.21.1.jar"
        ],
        "server": [],
        "dual": [
            "https://cdn.modrinth.com/data/P7dR8mSH/versions/oGwyXeEI/fabric-api-0.102.0%2B1.21.jar"
        ]
    }
}
```