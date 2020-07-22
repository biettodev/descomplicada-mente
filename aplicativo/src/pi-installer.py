import PyInstaller.__main__
import os

#-i assets/icons/icone-logo.ico
PyInstaller.__main__.run([
    "main.py",
    "-y",
    "-i=assets/icons/icone-logo.ico" ])
    
