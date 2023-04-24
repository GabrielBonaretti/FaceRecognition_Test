import mysql.connector
import numpy as np


def so_return():
    conexao = mysql.connector.connect(
        host='interclasse-2023.mariadb.database.azure.com',
        database='interclasse',
        user='diegos@interclasse-2023',
        password='senaimange2023'
    )

    cursor = conexao.cursor()

    comando = 'SELECT * FROM faces'
    cursor.execute(comando)
    resultado = cursor.fetchall()  # ler o banco de dados (read)  # retorna uma lista

    nomes_dos_rostos = []
    rostos_conhecidos = []
    interno = []
    
    for i in range(len(resultado)):
        interno.clear()
        nomes_dos_rostos.append(resultado[i][1])

        for j in range(len(resultado[i])):
            if j < 2:
                continue
            else:   
                interno.append(resultado[i][j])
        
        sla = np.array(interno)
        rostos_conhecidos.append(sla)

    cursor.close()
    conexao.close()

    return rostos_conhecidos, nomes_dos_rostos