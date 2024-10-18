import os
from fastapi import HTTPException
from fastapi.responses import JSONResponse, FileResponse, StreamingResponse

music_path = "./music"


def song_stream(song_path):
    with open(song_path, mode="rb") as file:
        yield from file


class Music:

    @staticmethod
    def get_music():
        try:
            music_list = [
                song for song in os.listdir(music_path) if song.endswith(".mp3")
            ]
            return JSONResponse(content={"songs": music_list}, status_code=200)
        except Exception as e:
            print(f"error al acceder las canciones {e}")
            raise HTTPException(
                status_code=500, detail="error al acceder a las canciones"
            )

    @staticmethod
    def get_song_by_name(name):
        try:
            song = [
                song
                for song in os.listdir(music_path)
                if song.endswith(".mp3") and song.split(".")[0] == name
            ]
            if song:
                song_path = f"{music_path}/{str(song[0])}"
                return StreamingResponse(
                    song_stream(song_path), media_type="audio/mpeg", status_code=200
                )
            else:
                return HTTPException(status_code=404, detail="song not found")
        except Exception as e:
            print(f"erro al obtener la cancion por nombre {e}")
