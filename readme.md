
# MC Fetch Gen
This program automates the process of downloading various Minecraft-related assets, including datapacks, resourcepacks, shaderpacks, and mods.
It reads a JSON file that specifies the assets to be downloaded, and generates an installer program for this collection of assets.

## Features
- **Installer generation**: The program creates a binary installer based on a JSON configuration file.
- **Customizable**: The JSON file can be edited to specify different assets to be downloaded.

## Dependencies
This program relies on **Python 3** and **PyInstaller** to build the generated installers.
You will need to install these dependencies in order to build the installer yourself.

## Usage
1. **Download the Executable**:<br>
Download the latest release from the GitHub releases section.

3. **Configure your JSON File**:<br>
Create your JSON configuration file in the same directory as the executable.<br>
Name it **mcfg.json**.

4. **Running the Executable**:<br>
Run the executable.
This will generate a new directory by your configuration within the current working directory.
Inside the build folder, you will find your custom asset installer.

5. **Script Usage**
    - The installer will create a new directory in the current working directory.
    - The new directory will contain all the downloaded assets including **datapacks**, **shaderpacks**, **resourcepacks**, and **mods**.
    ```
    /Example-XXX-XXX/
        ├── datapacks/
        ├── shaderpacks/
        ├── resourcepacks/
        ├── mods/
    ```

## JSON Configuration Example

```json
{
    "name": "Example",
    "version": "0.0.0",
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