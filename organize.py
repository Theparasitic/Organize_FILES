import os
from pathlib import Path

SUBDIRECTORIES={
    "Documents":['.pdf','.rtf','.txt','.docs'],
    "Audio":['m4a','m4b','mp3'],
    "Videos":['.mov','.mp4'],
    "Images":['.jpg','.png','.jpeg']
}

def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix==value:
                return category
    return 'other types'
    

def organizeDirectory():
    for item in os.scandir():
        if item.is_dir():
            continue
        filepath=Path(item)
        filetype=filepath.suffix.lower()
        directory=pickDirectory(filetype)
        directorypath=Path(directory)
        if directorypath.is_dir()!=True:
            directorypath.mkdir()
        filepath.rename(directorypath.joinpath(filepath))

organizeDirectory()
