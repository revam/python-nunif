@echo off

call "%~dp0setenv.bat"
pushd "%NUNIF_DIR%" && start "" pythonw -m iw3.player.gui && popd
exit /b 0
