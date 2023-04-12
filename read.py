import mysql.connector
import numpy as np


def so_return():
    conexao = mysql.connector.connect(
        host='localhost',
        database='bdyoutube',
        user='root',
        password=''
    )

    cursor = conexao.cursor()

    comando = 'SELECT * FROM teste2'
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