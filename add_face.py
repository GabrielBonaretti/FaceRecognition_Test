import face_recognition as fr
import mysql.connector
import numpy as np


def reconhece_face(url_foto):
    foto = fr.load_image_file(url_foto)
    rostos = fr.face_encodings(foto)
    if len(rostos) > 0:
        return True, rostos

    return False, []


def get_rostos():
    rostos_conhecidos = []
    nomes_dos_rostos = []

    gabriel = reconhece_face("./img/gabriel.jpg")
    if gabriel[0]:
        nomes_dos_rostos.append("gabriel")
        rostos_conhecidos.append(gabriel[1][0])
    
    diegoC = reconhece_face("./img/diegoC.jpeg")
    if diegoC[0]:
        nomes_dos_rostos.append("diegoC")
        rostos_conhecidos.append(diegoC[1][0])

    angelo = reconhece_face("./img/Angelo.jpeg")
    if angelo[0]:
        nomes_dos_rostos.append("angelo")
        rostos_conhecidos.append(angelo[1][0])

    kadu = reconhece_face("./img/Kadu.jpeg")
    if kadu[0]:
        nomes_dos_rostos.append("kadu")
        rostos_conhecidos.append(kadu[1][0])

    return rostos_conhecidos, nomes_dos_rostos


