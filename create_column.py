# from add_face import get_rostos
from puxando_da_pasta import get_rostos
import mysql.connector
import numpy as np


def create_column_items():
    rostos_conhecidos, nomes_conhecidos = get_rostos()

    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bdyoutube"
    )

    cursor = conexao.cursor()

    comando = 'SELECT testecol FROM teste2'
    cursor.execute(comando)
    cadastrados = cursor.fetchall()
    nomes = []

    for i in range(len(cadastrados)):
        nomes.append(cadastrados[i][0])

    for i in range(len(rostos_conhecidos)):
        if nomes_conhecidos[i] in nomes:
            print("Já cadastrado")
        else:
            comando = f'INSERT INTO teste2 (testecol, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25, a26, a27, a28, a29, a30, a31, a32, a33, a34, a35, a36, a37, a38, a39, a40, a41, a42, a43, a44, a45, a46, a47, a48, a49, a50, a51, a52, a53, a54, a55, a56, a57, a58, a59, a60, a61, a62, a63, a64, a65, a66, a67, a68, a69, a70, a71, a72, a73, a74, a75, a76, a77, a78, a79, a80, a81, a82, a83, a84, a85, a86, a87, a88, a89, a90, a91, a92, a93, a94, a95, a96, a97, a98, a99, a100, a101, a102, a103, a104, a105, a106, a107, a108, a109, a110, a111, a112, a113, a114, a115, a116, a117, a118, a119, a120, a121, a122, a123, a124, a125, a126, a127, a128) VALUES ("{nomes_conhecidos[i]}", {rostos_conhecidos[i][0]},  {rostos_conhecidos[i][1]},  {rostos_conhecidos[i][2]},  {rostos_conhecidos[i][3]},  {rostos_conhecidos[i][4]},  {rostos_conhecidos[i][5]},  {rostos_conhecidos[i][6]},  {rostos_conhecidos[i][7]},  {rostos_conhecidos[i][8]},  {rostos_conhecidos[i][9]},  {rostos_conhecidos[i][10]},  {rostos_conhecidos[i][11]},  {rostos_conhecidos[i][12]},  {rostos_conhecidos[i][13]},  {rostos_conhecidos[i][14]},  {rostos_conhecidos[i][15]},  {rostos_conhecidos[i][16]},  {rostos_conhecidos[i][17]},  {rostos_conhecidos[i][18]},  {rostos_conhecidos[i][19]},  {rostos_conhecidos[i][20]},  {rostos_conhecidos[i][21]},  {rostos_conhecidos[i][22]},  {rostos_conhecidos[i][23]},  {rostos_conhecidos[i][24]},  {rostos_conhecidos[i][25]},  {rostos_conhecidos[i][26]},  {rostos_conhecidos[i][27]},  {rostos_conhecidos[i][28]},  {rostos_conhecidos[i][29]},  {rostos_conhecidos[i][30]},  {rostos_conhecidos[i][31]},  {rostos_conhecidos[i][32]},  {rostos_conhecidos[i][33]},  {rostos_conhecidos[i][34]},  {rostos_conhecidos[i][35]},  {rostos_conhecidos[i][36]},  {rostos_conhecidos[i][37]},  {rostos_conhecidos[i][38]},  {rostos_conhecidos[i][39]},  {rostos_conhecidos[i][40]},  {rostos_conhecidos[i][41]},  {rostos_conhecidos[i][42]},  {rostos_conhecidos[i][43]},  {rostos_conhecidos[i][44]},  {rostos_conhecidos[i][45]},  {rostos_conhecidos[i][46]},  {rostos_conhecidos[i][47]},  {rostos_conhecidos[i][48]},  {rostos_conhecidos[i][49]},  {rostos_conhecidos[i][50]},  {rostos_conhecidos[i][51]},  {rostos_conhecidos[i][52]},  {rostos_conhecidos[i][53]},  {rostos_conhecidos[i][54]},  {rostos_conhecidos[i][55]},  {rostos_conhecidos[i][56]},  {rostos_conhecidos[i][57]},  {rostos_conhecidos[i][58]},  {rostos_conhecidos[i][59]},  {rostos_conhecidos[i][60]},  {rostos_conhecidos[i][61]},  {rostos_conhecidos[i][62]},  {rostos_conhecidos[i][63]},  {rostos_conhecidos[i][64]},  {rostos_conhecidos[i][65]},  {rostos_conhecidos[i][66]},  {rostos_conhecidos[i][67]},  {rostos_conhecidos[i][68]},  {rostos_conhecidos[i][69]},  {rostos_conhecidos[i][70]},  {rostos_conhecidos[i][71]},  {rostos_conhecidos[i][72]},  {rostos_conhecidos[i][73]},  {rostos_conhecidos[i][74]},  {rostos_conhecidos[i][75]},  {rostos_conhecidos[i][76]},  {rostos_conhecidos[i][77]},  {rostos_conhecidos[i][78]},  {rostos_conhecidos[i][79]},  {rostos_conhecidos[i][80]},  {rostos_conhecidos[i][81]}, {rostos_conhecidos[i][82]},  {rostos_conhecidos[i][83]},  {rostos_conhecidos[i][84]},  {rostos_conhecidos[i][85]},  {rostos_conhecidos[i][86]},  {rostos_conhecidos[i][87]},  {rostos_conhecidos[i][88]},  {rostos_conhecidos[i][89]},  {rostos_conhecidos[i][90]},  {rostos_conhecidos[i][91]},  {rostos_conhecidos[i][92]},  {rostos_conhecidos[i][93]},  {rostos_conhecidos[i][94]},  {rostos_conhecidos[i][95]},  {rostos_conhecidos[i][96]},  {rostos_conhecidos[i][97]},  {rostos_conhecidos[i][98]},  {rostos_conhecidos[i][99]},  {rostos_conhecidos[i][100]},  {rostos_conhecidos[i][101]},  {rostos_conhecidos[i][102]},  {rostos_conhecidos[i][103]},  {rostos_conhecidos[i][104]},  {rostos_conhecidos[i][105]},  {rostos_conhecidos[i][106]}, {rostos_conhecidos[i][107]},  {rostos_conhecidos[i][108]},  {rostos_conhecidos[i][109]},  {rostos_conhecidos[i][110]},  {rostos_conhecidos[i][111]},  {rostos_conhecidos[i][112]},  {rostos_conhecidos[i][113]},  {rostos_conhecidos[i][114]},  {rostos_conhecidos[i][115]},  {rostos_conhecidos[i][116]},  {rostos_conhecidos[i][117]},  {rostos_conhecidos[i][118]},  {rostos_conhecidos[i][119]},  {rostos_conhecidos[i][120]},  {rostos_conhecidos[i][121]},  {rostos_conhecidos[i][122]},  {rostos_conhecidos[i][123]},  {rostos_conhecidos[i][124]},  {rostos_conhecidos[i][125]},  {rostos_conhecidos[i][126]},  {rostos_conhecidos[i][127]})'
            cursor.execute(comando)
            conexao.commit()  # edita o banco de dados (create, update, delete)

    cursor.close()
    conexao.close()
