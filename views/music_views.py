"""
importancion de dependecias
- APIRouter
- File
- UploadFile
- HTTPException
- JSONResponse
- music_service

"""

from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from services.music_services import Music

router = APIRouter()

music_service = Music()


@router.get("/music")
async def read_music():
    """
    Devuelve la lista de canciones en la carpeta de música.
    """
    return music_service.get_music()


@router.get("/music/{music_name}")
async def read_music_by_name(music_name: str):
    """
    Si la canción existe en la carpeta de música, devuelve la canción con ese nombre.
    """
    result = music_service.get_music_by_name(music_name)
    if result:
        return result
    raise HTTPException(status_code=404, detail="Music not found")


@router.post("/music")
async def create_music(music_file: UploadFile = File(...)):
    """
    Si la canción no existe en la carpeta de música, la copia.
    """
    if music_service.create_music(music_file):
        return JSONResponse(content={"message": "Music added successfully"})
    else:
        raise HTTPException(status_code=400, detail="Music already exists")


@router.delete("/music/{music_name}")
async def delete_music(music_name: str):
    """
    Busca la canción y si existe en la carpeta de música, la borra.
    """
    if music_service.delete_music(music_name):
        return JSONResponse(content={"message": "Music deleted"})
    else:
        raise HTTPException(status_code=400, detail="Music does not exist")
