#!/bin/bash
pyinstaller src/main.py --onefile
rm -r .ropeproject build main.spec
mv dist build
mv build/main build/mcfg