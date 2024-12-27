#!/bin/bash
projDir=$(dirname $(dirname "$(realpath "$0")"))
pyinstaller $projDir/src/main.py --onefile
rm -r $projDir/.ropeproject $projDir/main.spec $projDir/build/main
mv $projDir/dist $projDir/build/out
mv $projDir/build/out/main $projDir/build/out/mcfg