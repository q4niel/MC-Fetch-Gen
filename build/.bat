@echo off
for %%i in (%~dp0..) do set "projDir=%%~fi"
py -3 -m PyInstaller %projDir%\src\main.py --onefile
del "%projDir%\main.spec"
rmdir /s /q "%projDir%\build\main"
move %projDir%\dist %projDir%\build\out
ren "%projDir%\build\out\main.exe" "mcfg.exe"