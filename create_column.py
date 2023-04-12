from add_face import get_rostos
import mysql.connector
import numpy as np

def create_column_items():
    rostos_conhecidos = get_rostos()

    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bdyoutube"
    )

    cursor = conexao.cursor()

    rostos_conhecidos = get_rostos()
    print(rostos_conhecidos)

    # comando = f'INSERT INTO teste (testecol,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128) VALUES ("{rostos_conhecidos[0]}", {rostos_conhecidos[1][0][0]},  {rostos_conhecidos[1][0][1]},  {rostos_conhecidos[1][0][2]},  {rostos_conhecidos[1][0][3]},  {rostos_conhecidos[1][0][4]},  {rostos_conhecidos[1][0][5]},  {rostos_conhecidos[1][0][6]},  {rostos_conhecidos[1][0][7]},  {rostos_conhecidos[1][0][8]},  {rostos_conhecidos[1][0][9]},  {rostos_conhecidos[1][0][10]},  {rostos_conhecidos[1][0][11]},  {rostos_conhecidos[1][0][12]},  {rostos_conhecidos[1][0][13]},  {rostos_conhecidos[1][0][14]},  {rostos_conhecidos[1][0][15]},  {rostos_conhecidos[1][0][16]},  {rostos_conhecidos[1][0][17]},  {rostos_conhecidos[1][0][18]},  {rostos_conhecidos[1][0][19]},  {rostos_conhecidos[1][0][20]},  {rostos_conhecidos[1][0][21]},  {rostos_conhecidos[1][0][22]},  {rostos_conhecidos[1][0][23]},  {rostos_conhecidos[1][0][24]},  {rostos_conhecidos[1][0][25]},  {rostos_conhecidos[1][0][26]},  {rostos_conhecidos[1][0][27]},  {rostos_conhecidos[1][0][28]},  {rostos_conhecidos[1][0][29]},  {rostos_conhecidos[1][0][30]},  {rostos_conhecidos[1][0][31]},  {rostos_conhecidos[1][0][32]},  {rostos_conhecidos[1][0][33]},  {rostos_conhecidos[1][0][34]},  {rostos_conhecidos[1][0][35]},  {rostos_conhecidos[1][0][36]},  {rostos_conhecidos[1][0][37]},  {rostos_conhecidos[1][0][38]},  {rostos_conhecidos[1][0][39]},  {rostos_conhecidos[1][0][40]},  {rostos_conhecidos[1][0][41]},  {rostos_conhecidos[1][0][42]},  {rostos_conhecidos[1][0][43]},  {rostos_conhecidos[1][0][44]},  {rostos_conhecidos[1][0][45]},  {rostos_conhecidos[1][0][46]},  {rostos_conhecidos[1][0][47]},  {rostos_conhecidos[1][0][48]},  {rostos_conhecidos[1][0][49]},  {rostos_conhecidos[1][0][50]},  {rostos_conhecidos[1][0][51]},  {rostos_conhecidos[1][0][52]},  {rostos_conhecidos[1][0][53]},  {rostos_conhecidos[1][0][54]},  {rostos_conhecidos[1][0][55]},  {rostos_conhecidos[1][0][56]},  {rostos_conhecidos[1][0][57]},  {rostos_conhecidos[1][0][58]},  {rostos_conhecidos[1][0][59]},  {rostos_conhecidos[1][0][60]},  {rostos_conhecidos[1][0][61]},  {rostos_conhecidos[1][0][62]},  {rostos_conhecidos[1][0][63]},  {rostos_conhecidos[1][0][64]},  {rostos_conhecidos[1][0][65]},  {rostos_conhecidos[1][0][66]},  {rostos_conhecidos[1][0][67]},  {rostos_conhecidos[1][0][68]},  {rostos_conhecidos[1][0][69]},  {rostos_conhecidos[1][0][70]},  {rostos_conhecidos[1][0][71]},  {rostos_conhecidos[1][0][72]},  {rostos_conhecidos[1][0][73]},  {rostos_conhecidos[1][0][74]},  {rostos_conhecidos[1][0][75]},  {rostos_conhecidos[1][0][76]},  {rostos_conhecidos[1][0][77]},  {rostos_conhecidos[1][0][78]},  {rostos_conhecidos[1][0][79]},  {rostos_conhecidos[1][0][80]},  {rostos_conhecidos[1][0][81]},  {rostos_conhecidos[1][0][82]},  {rostos_conhecidos[1][0][83]},  {rostos_conhecidos[1][0][84]},  {rostos_conhecidos[1][0][85]},  {rostos_conhecidos[1][0][86]},  {rostos_conhecidos[1][0][87]},  {rostos_conhecidos[1][0][88]},  {rostos_conhecidos[1][0][89]},  {rostos_conhecidos[1][0][90]},  {rostos_conhecidos[1][0][91]},  {rostos_conhecidos[1][0][92]},  {rostos_conhecidos[1][0][93]},  {rostos_conhecidos[1][0][94]},  {rostos_conhecidos[1][0][95]},  {rostos_conhecidos[1][0][96]},  {rostos_conhecidos[1][0][97]},  {rostos_conhecidos[1][0][98]},  {rostos_conhecidos[1][0][99]},  {rostos_conhecidos[1][0][100]},  {rostos_conhecidos[1][0][101]},  {rostos_conhecidos[1][0][102]},  {rostos_conhecidos[1][0][103]},  {rostos_conhecidos[1][0][104]},  {rostos_conhecidos[1][0][105]},  {rostos_conhecidos[1][0][106]},  {rostos_conhecidos[1][0][107]},  {rostos_conhecidos[1][0][108]},  {rostos_conhecidos[1][0][109]},  {rostos_conhecidos[1][0][110]},  {rostos_conhecidos[1][0][111]},  {rostos_conhecidos[1][0][112]},  {rostos_conhecidos[1][0][113]},  {rostos_conhecidos[1][0][114]},  {rostos_conhecidos[1][0][115]},  {rostos_conhecidos[1][0][116]},  {rostos_conhecidos[1][0][117]},  {rostos_conhecidos[1][0][118]},  {rostos_conhecidos[1][0][119]},  {rostos_conhecidos[1][0][120]},  {rostos_conhecidos[1][0][121]},  {rostos_conhecidos[1][0][122]},  {rostos_conhecidos[1][0][123]},  {rostos_conhecidos[1][0][124]},  {rostos_conhecidos[1][0][125]},  {rostos_conhecidos[1][0][126]},  {rostos_conhecidos[1][0][127]})'
    comando = f'INSERT INTO teste2 (testecol, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25, a26, a27, a28, a29, a30, a31, a32, a33, a34, a35, a36, a37, a38, a39, a40, a41, a42, a43, a44, a45, a46, a47, a48, a49, a50, a51, a52, a53, a54, a55, a56, a57, a58, a59, a60, a61, a62, a63, a64, a65, a66, a67, a68, a69, a70, a71, a72, a73, a74, a75, a76, a77, a78, a79, a80, a81, a82, a83, a84, a85, a86, a87, a88, a89, a90, a91, a92, a93, a94, a95, a96, a97, a98, a99, a100, a101, a102, a103, a104, a105, a106, a107, a108, a109, a110, a111, a112, a113, a114, a115, a116, a117, a118, a119, a120, a121, a122, a123, a124, a125, a126, a127, a128) VALUES ("{rostos_conhecidos[0]}", {rostos_conhecidos[1][0]},  {rostos_conhecidos[1][1]},  {rostos_conhecidos[1][2]},  {rostos_conhecidos[1][3]},  {rostos_conhecidos[1][4]},  {rostos_conhecidos[1][5]},  {rostos_conhecidos[1][6]},  {rostos_conhecidos[1][7]},  {rostos_conhecidos[1][8]},  {rostos_conhecidos[1][9]},  {rostos_conhecidos[1][10]},  {rostos_conhecidos[1][11]},  {rostos_conhecidos[1][12]},  {rostos_conhecidos[1][13]},  {rostos_conhecidos[1][14]},  {rostos_conhecidos[1][15]},  {rostos_conhecidos[1][16]},  {rostos_conhecidos[1][17]},  {rostos_conhecidos[1][18]},  {rostos_conhecidos[1][19]},  {rostos_conhecidos[1][20]},  {rostos_conhecidos[1][21]},  {rostos_conhecidos[1][22]},  {rostos_conhecidos[1][23]},  {rostos_conhecidos[1][24]},  {rostos_conhecidos[1][25]},  {rostos_conhecidos[1][26]},  {rostos_conhecidos[1][27]},  {rostos_conhecidos[1][28]},  {rostos_conhecidos[1][29]},  {rostos_conhecidos[1][30]},  {rostos_conhecidos[1][31]},  {rostos_conhecidos[1][32]},  {rostos_conhecidos[1][33]},  {rostos_conhecidos[1][34]},  {rostos_conhecidos[1][35]},  {rostos_conhecidos[1][36]},  {rostos_conhecidos[1][37]},  {rostos_conhecidos[1][38]},  {rostos_conhecidos[1][39]},  {rostos_conhecidos[1][40]},  {rostos_conhecidos[1][41]},  {rostos_conhecidos[1][42]},  {rostos_conhecidos[1][43]},  {rostos_conhecidos[1][44]},  {rostos_conhecidos[1][45]},  {rostos_conhecidos[1][46]},  {rostos_conhecidos[1][47]},  {rostos_conhecidos[1][48]},  {rostos_conhecidos[1][49]},  {rostos_conhecidos[1][50]},  {rostos_conhecidos[1][51]},  {rostos_conhecidos[1][52]},  {rostos_conhecidos[1][53]},  {rostos_conhecidos[1][54]},  {rostos_conhecidos[1][55]},  {rostos_conhecidos[1][56]},  {rostos_conhecidos[1][57]},  {rostos_conhecidos[1][58]},  {rostos_conhecidos[1][59]},  {rostos_conhecidos[1][60]},  {rostos_conhecidos[1][61]},  {rostos_conhecidos[1][62]},  {rostos_conhecidos[1][63]},  {rostos_conhecidos[1][64]},  {rostos_conhecidos[1][65]},  {rostos_conhecidos[1][66]},  {rostos_conhecidos[1][67]},  {rostos_conhecidos[1][68]},  {rostos_conhecidos[1][69]},  {rostos_conhecidos[1][70]},  {rostos_conhecidos[1][71]},  {rostos_conhecidos[1][72]},  {rostos_conhecidos[1][73]},  {rostos_conhecidos[1][74]},  {rostos_conhecidos[1][75]},  {rostos_conhecidos[1][76]},  {rostos_conhecidos[1][77]},  {rostos_conhecidos[1][78]},  {rostos_conhecidos[1][79]},  {rostos_conhecidos[1][80]},  {rostos_conhecidos[1][81]}, {rostos_conhecidos[1][82]},  {rostos_conhecidos[1][83]},  {rostos_conhecidos[1][84]},  {rostos_conhecidos[1][85]},  {rostos_conhecidos[1][86]},  {rostos_conhecidos[1][87]},  {rostos_conhecidos[1][88]},  {rostos_conhecidos[1][89]},  {rostos_conhecidos[1][90]},  {rostos_conhecidos[1][91]},  {rostos_conhecidos[1][92]},  {rostos_conhecidos[1][93]},  {rostos_conhecidos[1][94]},  {rostos_conhecidos[1][95]},  {rostos_conhecidos[1][96]},  {rostos_conhecidos[1][97]},  {rostos_conhecidos[1][98]},  {rostos_conhecidos[1][99]},  {rostos_conhecidos[1][100]},  {rostos_conhecidos[1][101]},  {rostos_conhecidos[1][102]},  {rostos_conhecidos[1][103]},  {rostos_conhecidos[1][104]},  {rostos_conhecidos[1][105]},  {rostos_conhecidos[1][106]}, {rostos_conhecidos[1][107]},  {rostos_conhecidos[1][108]},  {rostos_conhecidos[1][109]},  {rostos_conhecidos[1][110]},  {rostos_conhecidos[1][111]},  {rostos_conhecidos[1][112]},  {rostos_conhecidos[1][113]},  {rostos_conhecidos[1][114]},  {rostos_conhecidos[1][115]},  {rostos_conhecidos[1][116]},  {rostos_conhecidos[1][117]},  {rostos_conhecidos[1][118]},  {rostos_conhecidos[1][119]},  {rostos_conhecidos[1][120]},  {rostos_conhecidos[1][121]},  {rostos_conhecidos[1][122]},  {rostos_conhecidos[1][123]},  {rostos_conhecidos[1][124]},  {rostos_conhecidos[1][125]},  {rostos_conhecidos[1][126]},  {rostos_conhecidos[1][127]})'
    
    cursor.execute(comando)
    conexao.commit()  # edita o banco de dados (create, update, delete)

    cursor.close()
    conexao.close()


create_column_items()