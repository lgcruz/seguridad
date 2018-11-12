#primer decodificador
listaCeasarS1 = ["VWDQ LV QRW ZKDW KH VHHPV.","ZHOFRPH WR JUDYLWB IDOOV.","QHAW ZHHN: UHWXUQ WR EXWW LVODQG.",
         "KH'V VWLOO LQ WKH YHQWV.","FDUOD, ZKB ZRQ'W BRX FDOO PH?","RQZDUGV DRVKLPD!",
         "PU. FDHVDULDQ ZLOO EH RXW QHAW ZHHN. PU. DWEDVK ZLOO VXEVWLWXWH.",
         "SXEHUWB LV WKH JUHDWHVW PBVWHUB RI DOO DOVR: JR RXWVLGH DQG PDNH IULHQGV.","OLHV ","PBVWHUB VKDFN","SLWW",
         "OAUVG","EWTUG AQW OCTKNAP","ELOO LV ZDWFKLQJ"]

# ceasar cypher
def ceasar(cypherText):
    decypherText=""
    for j in cypherText:
        if 65 <= ord(j) and ord(j) <= 90:
            changed = ord(j) - 3
            if changed < 65:
                changed = 90 + changed - (64)
                #print("in")
            decypherText = decypherText + str(chr(changed))
        else:
            decypherText = decypherText + j
    return decypherText
print("\t\t\t-----First Season-------")
print("\t\t-----CAESAR-------")
for i in listaCeasarS1:
    codificado = ceasar(i)
    print(codificado)

listaAtbashS1 = [""" KZKVI QZN WRKKVI HZBH: "ZFFTSDCJSTZWHZWFS!" ""","V. KOFIRYFH GIVNYOVB.","MLG S.T. DVOOH ZKKILEVW.",
               "HLIIB, WRKKVI, YFG BLFI DVMWB RH RM ZMLGSVI XZHGOV.","GSV RMERHRYOV DRAZIW RH DZGXSRMT.",
               "YILFTSG GL BLF YB SLNVDLIP: GSV XZMWB.","SVZEB RH GSV SVZW GSZG DVZIH GSV UVA."]

# Atbash cipher

def atbash(cypherText):
    decypherText=""
    for j in cypherText:
        if 65 <= ord(j) and ord(j) <= 90:
            changed = ord(j)
            if changed <= 77:
                changed = 78 - changed + 77
            else:
                changed = 77 - changed + 78
            decypherText = decypherText + str(chr(changed))
        else:
            decypherText = decypherText + j
    return decypherText
print("\t\t-----CAESAR-------")
for i in listaAtbashS1:
    code = atbash(i)
    print(code)

listaA1Z26S1 = [""" 14-5-24-20 21-16: "6-15-15-20-2-15-20 20-23-15: 7-18-21-14-11-12-5'19 7-18-5-22-5-14-7-5." """,
              "22-9-22-1-14 12-15-19 16-1-20-15-19 4-5 12-1 16-9-19-3-9-14-1.",
              "2-21-20 23-8-15 19-20-15-12-5 20-8-5 3-1-16-5-18-19?","8-1-16-16-25 14-15-23, 1-18-9-5-12?",
              "9-20 23-15-18-11-19 6-15-18 16-9-9-9-9-9-9-9-9-9-9-9-9-9-9-9-9-9-7-19!",
              "20-15 2-5 3-15-14-20-9-14-21-5-4...","18-5-22-5-18-19-5 20-8-5 3-9-16-8-5-18-19"]

# A1Z26
def A1Z26(cypherText):
    decypherText=""
    #print(cypherText)
    cypherText = cypherText.split(" ")
    for j in cypherText:
        #print(j+" = j")
        j = j.split("-")
        for k in j:

            if k.isnumeric():
                #print(int(k)+64," = k")
                decypherText = decypherText + chr(int(k)+64)
            else:
                texto = ""
                number = ""
                bandera = 0
                for i in k:
                    if i.isnumeric():
                        number = number + i
                        #print(chr(int(number)+64)," = num ",end="")
                        #texto = texto + "."
                    else:
                        if len(number) > 0 and bandera == 0:

                            texto = texto + chr(int(number)+64)
                            number = ""

                        texto = texto + i
                    if len(number) and k[-1]==i and chr(int(number)+64) not in texto:
                        texto = texto + chr(int(number)+64) 
                    #print(i+" = i ",end="")
                    #print(texto+" = text ")
                decypherText = decypherText + texto
        decypherText = decypherText + " "
    return decypherText

print("\t\t-----A1Z26-------")
for i in listaA1Z26S1:
    code = A1Z26(i)
    print(code)

listaCombinada = ["5-19-23-6-21-16 18-9-6 4-16-19 22-12-15-10-20-19-25-19"]

print("\t\t-----Combined-------")
code = A1Z26(listaCombinada[0])
code = atbash(code)
code = ceasar(code)
print(code)
