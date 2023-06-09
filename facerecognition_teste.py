import numpy as np
import face_recognition as fr
import cv2
from read import so_return
from teste import api

video_capture = cv2.VideoCapture(0)

count = 0
nome_teste = ""

while True:
    rostos_conhecidos, nomes_dos_rostos = so_return()

    ret, frame = video_capture.read()

    localizacao_dos_rostos = fr.face_locations(frame)
    rosto_desconhecidos = fr.face_encodings(frame, localizacao_dos_rostos)

    for (top, right, bottom, left), rosto_desconhecido in zip(localizacao_dos_rostos, rosto_desconhecidos):
        resultados = fr.compare_faces(rostos_conhecidos, rosto_desconhecido)

        face_distances = fr.face_distance(rostos_conhecidos, rosto_desconhecido)

        melhor_id = np.argmin(face_distances)

        for i in range(len(resultados)):
            contador = 0
            if resultados[i]:
                contador += 1

        if contador > 1:
            count = 0
            nome = "Desconhecido"

        if resultados[melhor_id]:
            nome = nomes_dos_rostos[melhor_id]
            if nome == nome_teste:
                count += 1
            else:
                count = 0

            nome_teste = nome
        else:
            count = 0
            nome = "Desconhecido"

        # Ao redor do rosto
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.imshow('Webcam_facerecognition', frame)

        print(count)
        if count == 10:
            api(nome_face=nome)
            print(nome)
            count = 0

    rostos_conhecidos.clear()
    nomes_dos_rostos.clear()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
