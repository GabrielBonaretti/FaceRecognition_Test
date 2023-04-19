import face_recognition as fr
import os

file_folder = './dload'


def reconhece_face(url_foto):
    foto = fr.load_image_file(url_foto)
    rostos = fr.face_encodings(foto)
    if len(rostos) > 0:
        return True, rostos

    return False, []


def get_rostos():
    rostos_conhecidos = []
    nomes_dos_rostos = []

    for file_name in os.listdir(file_folder):
        nome_certo = file_name.replace(".", " ").split()[0]
        nome = reconhece_face(file_folder + "/" + file_name)
        if nome[0]:
            with open(os.path.join(file_folder, file_name), mode='rb'):
                nomes_dos_rostos.append(nome_certo)
                rostos_conhecidos.append(nome[1][0])

    return rostos_conhecidos, nomes_dos_rostos
