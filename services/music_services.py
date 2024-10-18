""" 
importancion de dependecias
- fastapi
- os
- shutil
para manejo de archivos de musica
"""

import os
import shutil
from fastapi import UploadFile


class Music:
    "inicializo la clase music con el path de la carpeta de musica y musica"

    def __init__(self, music_url="./music"):
        self.music_url = music_url
        self.music = self.get_music()

    def get_music(self):
        """
        devuelve la lista de musicas en la carpeta de musica
        """
        return [music for music in os.listdir(self.music_url) if music.endswith(".mp3")]

    def get_music_by_name(self, music_name):
        """
        si la musica existe en la carpeta de musica, devuelve la lista de musicas
        """
        return [music for music in self.music if music == music_name]

    def create_music(self, music_file: UploadFile):
        """
        si la musica no existe en la carpeta de musica, la copia
        """
        if music_file.filename not in self.music and music_file.filename.endswith(
            ".mp3"
        ):
            file_path = os.path.join(self.music_url, music_file.filename)
            with open(file_path, "wb+") as f:
                shutil.copyfileobj(music_file.file, f)
                self.music.append(music_file.filename)
            return True
        else:
            return False

    def delete_music(self, music_name):
        """
        si la musica existe en la carpeta de musica, la borra
        """
        if music_name in self.music:
            os.remove(os.path.join(self.music_url, music_name))
            self.music.remove(music_name)
            return True
        else:
            return False
