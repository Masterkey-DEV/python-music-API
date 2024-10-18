from fastapi import FastAPI
from services.songs_services import Music

music_services = Music()
app = FastAPI()


@app.get("/")
def Root():
    return {"message": "bienvenido a mi app"}


@app.get("/music")
def get_all_songs():
    return music_services.get_music()


@app.get("/music/{name}")
def get_song(name):
    return music_services.get_song_by_name(name)
