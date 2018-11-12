#primer decodificador
listaCeasar = ["VWDQ LV QRW ZKDW KH VHHPV.","ZHOFRPH WR JUDYLWB IDOOV.","QHAW ZHHN: UHWXUQ WR EXWW LVODQG.",
         "KH'V VWLOO LQ WKH YHQWV.","FDUOD, ZKB ZRQ'W BRX FDOO PH?","RQZDUGV DRVKLPD!",
         "PU. FDHVDULDQ ZLOO EH RXW QHAW ZHHN. PU. DWEDVK ZLOO VXEVWLWXWH."]

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

for i in listaCeasar:
    codificado = ceasar(i)
    print(codificado)

listaAtbash = [""" KZKVI QZN WRKKVI HZBH: "ZFFTSDCJSTZWHZWFS!" ""","V. KOFIRYFH GIVNYOVB.","MLG S.T. DVOOH ZKKILEVW.",
               "HLIIB, WRKKVI, YFG BLFI DVMWB RH RM ZMLGSVI XZHGOV.","GSV RMERHRYOV DRAZIW RH DZGXSRMT.",
               "YILFTSG GL BLF YB SLNVDLIP: GSV XZMWB.","SVZEB RH GSV SVZW GSZG DVZIH GSV UVA."]

# Atbash cipher

def atbash(cypherText):
    decypherText=""
    for j in cypherText:
        if 65 <= ord(j) and ord(j) <= 90:
            changed = ord(j)
            if changed < 65:
                changed = 90 + changed - (64)
                #print("in")
            decypherText = decypherText + str(chr(changed))
        else:
            decypherText = decypherText + j
    return decypherText