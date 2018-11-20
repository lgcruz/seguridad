import numpy as np


def caesarDeCipher(texto):
    abcdario=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    resultado=""
    for letra in texto:
        if(letra not in abcdario):
            resultado+=letra
        else:
            indice = abcdario.index(letra)
            resultado+=abcdario[indice-3]

    return resultado

def atbashDeCipher(texto):
    abcdario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z"]
    resultado=""
    for letra in texto:
        if (letra not in abcdario):
            resultado += letra
        else:
            indice = abcdario.index(letra)
            resultado+= abcdario[len(abcdario)-indice-1]
    return resultado

def A1Z26DeCipher(texto):
    abcdario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z"]

    resultado=""

    palabras = texto.split(" ")
    for palabra in palabras:
        temporal = ""
        for i in range(len(palabra)):
            char = palabra[i]
            if(char.isdigit()):
                temporal+=char
            elif(char=="-"):
                numero = int(temporal)
                resultado+=abcdario[numero-1]
                temporal=""
            else:
                if(len(temporal)>0):
                    numero = int(temporal)
                    resultado += abcdario[numero - 1]
                resultado += char
                temporal = ""

            if(i==len(palabra)-1 and char.isdigit()):
                numero = int(temporal)
                resultado += abcdario[numero - 1]
                temporal = ""
        resultado+=" "
    return resultado

def combinedDeCipherWithoutVigener(texto):
    decifrado1= A1Z26DeCipher(texto)
    decifrado2= atbashDeCipher(decifrado1)
    decifrado3= caesarDeCipher(decifrado2)
    return decifrado3


#primer decodificador
listaCeasarS1 = ["VWDQ LV QRW ZKDW KH VHHPV.","ZHOFRPH WR JUDYLWB IDOOV.","QHAW ZHHN: UHWXUQ WR EXWW LVODQG.",
         "KH'V VWLOO LQ WKH YHQWV.","FDUOD, ZKB ZRQ'W BRX FDOO PH?","RQZDUGV DRVKLPD!",
         "PU. FDHVDULDQ ZLOO EH RXW QHAW ZHHN. PU. DWEDVK ZLOO VXEVWLWXWH.",
         "SXEHUWB LV WKH JUHDWHVW PBVWHUB RI DOO DOVR: JR RXWVLGH DQG PDNH IULHQGV.","OLHV ","PBVWHUB VKDFN","SLWW",
         "OAUVG","EWTUG AQW OCTKNAP","ELOO LV ZDWFKLQJ"]

# ceasar cypher
def caesar(cypherText):
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
print("\n\t\t\t\t\t-----First Season-------")
print("\n\t\t\t\t-----CAESAR-------")
for i in listaCeasarS1:
    codificado = caesar(i)
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
print("\n\t\t\t\t-----ATBASH-------")
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

print("\n\t\t\t\t-----A1Z26-------")
for i in listaA1Z26S1:
    code = A1Z26(i)
    print(code)

listaCombinada = ["5-19-23-6-21-16 18-9-6 4-16-19 22-12-15-10-20-19-25-19"]

print("\n\t\t\t\t-----Combined-------")
def combined1(texto):
    code = A1Z26(texto)
    code = atbash(code)
    code = caesar(code)
    return code

code = combined1(listaCombinada[0])
print(code)

chapters_decoded={
    "0":"STAN IS NOT WHAT HE SEEMS",
    "1":"WELCOME TO GRAVITY FALLS.",
    "2":"NEXT WEEK: RETURN TO BUTT ISLAND.",
    "3":"HE'S STILL IN THE VENTS.",
    "4":"CARLA, WHY WON'T YOU CALL ME?",
    "5":"ONWARDS AOSHIMA!",
    "6":"MR. CAESARIAN WILL BE OUT NEXT WEEK. MR. ATBASH WILL SUBSTITUTE.",
    "7":"PAPER JAM DIPPER SAYS: \"AUUGHWXQHGADSADUH!\"",
    "8":"E. PLURIBUS TREMBLEY.",
    "9":"NOT H.G. WELLS APPROVED.",
    "10":"SORRY, DIPPER, BUT YOUR WENDY IS IN ANOTHER CASTLE.",
    "11":"THE INVISIBLE WIZARD IS WATCHING.",
    "12":"BROUGHT TO YOU BY HOMEWORK: THE CANDY.",
    "13":"HEAVY IS THE HEAD THAT WEARS THE FEZ.",
    "14":"NEXT UP: \"FOOTBOT TWO: GRUNKLE'S GREVENGE.\"",
    "15":"VIVAN LOS PATOS DE LA PISCINA.",
    "16":["PUBERTY IS THE GREATEST MYSTERY OF ALL ALSO: GO OUTSIDE AND MAKE FRIENDS.","BUT WHO STOLE THE CAPERS?"],
    "17":"HAPPY NOW, ARIEL?",
    "18":["LIES","IT WORKS FOR PIIIIIIIIIIIIIIIIIGS!"],
    "19":["MYSTERY SHACK","PITT","MYSTE","CURSE YOU MARILYN","TO BE CONTINUED...","LIAR MONSTER SNAPPY DRESSER."],
    "20":["BILL IS WATCHING","REVERSE THE CIPHERS","DON'T EAT HIM!","THE PORTAL WHEN COMPLETED WILL OPEN A GATEWAY TO "
        "INFINITE NEW WORLDS AND HERALD A NEW ERA IN MANKINDâ€™S UNDERSTANDING OF THE UNIVERSE. PLUS, IT WILL PROBABLY "
        "GET GIRLS TO START TALKING TO ME FINALLY.","SEARCH FOR THE BLINDEYE"],
    "s1":["THE DAR","FROM THE FIRST UNTIL THE LAST SEARCH THE"],
    "s2":"I WAS SO",
    "s3":"BLIND HE L",
    "s4":["NEAR","THEM ALL WELCOME TO GRAVITY FALLS"],
    "s5":["KNESS IS","CODES OF CREDITS PAST ONE MEANS ONE SO SEARCH"],
    "s6":"IED TO ME",
    "21":["SEARCH FOR THE...","FLAG","WHY IS WENDY SO PERFECT","WATCH OUT","KILL ME PLEASE","WELCOME BACK",
          "THE MAN DOWNSTAIRS IS VERY CLEVER","CAN HE HIDE HIS PLANS FOREVER?"],
    "22":["PUT ALL SIX PIECES TOGETHER!","ICE ICE BABY","AM I ME? IS HE ME?","WHAT KIND OF DISASTER INDEED",
          "IMPROPER USE OF MACHINERY COULD","LEAD TO UTTER CATASTROPHE"],
    "23":["REMEMBER BIG HENRY","OLD MAN SLEEPING ON THE GREEN","CAN'T HELP BUT WONDER WHAT HE'S SEEN"],
    "24":["PURE ENERGY, NOT SKIN AND BONE","RISING LIKE THE SHEPARD TONE","WIDDLE","SHIFTER","WHATEVS","BEARO",
          "WE'VE ALL HAD SOME FUN TONIGHT, BUT LET'S NOT FORGET WHO THE REAL \"PUPPET MASTERS\" ARE: REPTOIDS "
          "WHO HAVE INFILTRATED OUR GOVERNMENT","NO PUPPET STRINGS CAN HOLD ME DOWN","SO PATIENTLY I WATCH THIS TOWN",
          "ABNORMAL SOON WILL BE THE NORM","ENJOY THE CALM BEFORE THE STORM"],
    "25":["STAN IS NOT WHAT HE SEEMS","SPACEJAMTWO","ANTHYDING CAN HADPLEN","WINNING HEARTS BY DAYLIGHT",
          "POSSESSING ROBOTS BY MOONLIGHT","HER EMOTIONAL BAGGAGE IS A REAL FRIGHT","SHE HAS THE ONE NAME GIFFANY"],
    "26":["CHECK OUT DR. WADDLESâ€™ LATEST BOOK: \"A BRIEF HISTORY OF OINK OINK OINK OINK OINK\"","ALL ANIMATION",
          "IS BLACK MAGIC"],
    "27":["IF MY SUSPICIONS ARE CORRECT, THIS IS THE WORK OF FIDDLEFORD. DOES HE REALLY HAVE TO GO TO SUCH GREAT "
          "LENGTHS TO FORGET?","BILL CIPHER! TRIANGLE!","IGNORANCE IS BLISS. BUT BLISS IS BORING.","GIDEON'S TANTRUMS, "
          "MISSPELLED TATTOOS,","SHANDRA'S REJECTIONS, SOCIETY'S VIEWS,","A FEAR OF WITCHES, A LIFE OF REGRET,",
          "THESE ARE THE THINGS THAT THEY TRY TO FORGET."],
    "28":["DON'T DO THE TIME CRIME IF YOU CAN'T DO THE TIME TIME.","JOIN THE TIME PARADOX AVOIDANCE ENFORCEMENT "
          "SQUADRON!","GREAT HOURS!","SOLID BENEFITS!","SIGN UP YESTERDAY!"],
    "29":["I EAT KIDS.","AT THE PLAY OR AT THE FAIR,","I ALWAYS SEE THEM STANDING THERE.","DRESSED IN BLACK THEY'RE ON "
          "MY LAWN,","BUT WHEN I TURN MY HEAD THEY'RE GONE."],
    "30":["NEXT UP ON UTBAHC: DID ALIENS WRITE THE CONSTITUTION? CRAWDADS IN TIARAS! AND FLORIDA: THE SHOW.",
          "STANISNOTWHATHESEEMS","STANISNOTWHATHESEEMS","STANISNOTWHATHESEEMS"],
    "31":["MY COMPASS GOES HAYWIRE THE CLOSER I GET TO THEM. DOES THIS MEAN WHAT I THINK IT DOES? THE ANSWER MAY BE "
          "UNDERGROUND.","GUVAMENT","THE ORIGINAL MYSTERY TWINS","THIRTY YEARS AND NOW HE'S BACK",
          "THE MYSTERY IN THE MYSTERY SHACK"],
    "32":["BACKUPSMORE UNIVERSITY: YOU TRIED","A STUBBORN TOUGH NEW JERSEY NATIVE","FILBRICK WASNâ€™T TOO CREATIVE",
          "HAVING TWINS WAS NOT HIS PLAN","SO HE JUST SHRUGGED AND NAMED BOTH STAN","BILL CIPHER TRIANGLE"],
    "33":["EXCELSI-WHATEVER!","FUN AND GAMES ARE GREAT DISTRACTIONS","BUT SMALL THINGS CAN HAVE CHAIN REACTIONS"],
    "34":["GIIIIIIIIIIIIIIIIIIIIIITTTTT 'EM!","BE WARY OF WHOM YOU BELITTLE","BIG PROBLEMS CAN START OUT WIDDLE"],
    "35":["BLACK & WHITE","THINK LIARON; AP; ESN; R; M; S; D__TE; PYR","IT STARTED WITH BAD DREAMS WHICH BECAME "
          "NIGHTMARES. I WAS FOOLISH, I WANTED ANSWERS, I PAINTED THE SYMBOLS, I SAID THE WORDS: WHEN GRAVITY FALLS AND "
          "THE EARTH BECOMES SKY FEAR THE BEAST WITH JUST ONE EYE.","A SIMPLE MAN WITH EAGER EARS MAY TRUST THE "
          "WHISPERS THAT HE HEARS","IN CIPHER'S GAME HE NEEDS A PAWN","BE SURE TO KNOW WHICH SIDE YOU'RE ON"],
    "36":["SOOS, LIKE A NOBLE GOLDEN RETRIEVER, EVENTUALLY FOUND HIS WAY HOMEWARD, AND BEFRIENDED A TALKING BULLDOG AND "
          "SASSY CAT ALONG THE WAY","CARLA MCCORKLE RETURNED ALL HIS FLOWERS","MARILYN DIVORCED HIM AFTER ONLY SIX "
          "HOURS","BEATRICE SLAPPED HIM FOR BEING A CAD","OLD GOLDIE'S THE BEST GIRLFRIEND STAN EVER HAD"],
    "37":["PROBABILITY DRIVE ENGINE","PROBE ATORIUM","BLERG BLOTH AND BEYOND USED THATENS HALF PRICE","SPECIMEN HAS "
          "ESCAPED IS CHANGING FORMS","DID YOU MISS ME?","THE PROPHECY SEEMED FAR AWAY","BUT FINALLY WE'VE REACHED THE "
          "DAY.","GIVE UP THE PAST. EMBRACE THE STRANGE.","EVERYTHING YOU CARE ABOUT WILL CHANGE."],
    "38":["IT WILL TAKE 1,000 YEARS FOR TIME BABY'S MOLECULES TO RECONSTITUTE, AND WHEN HE'S BACK, HE'S GOING TO BE "
          "VERY CRANKY.","GAME IS OVER, AND I WON","NOW IT'S TIME TO START THE FUN","I ALWAYS LOVE CORRUPTING LIVES",
          "NOW LET'S SEE WHICH PINES SURVIVES"],
    "39":["CRAZ AND XYLER WENT ON TO RUN THE LEGAL DEPARTMENT AT A MAJOR CHILDREN'S TELEVISION NETWORK","WHEN ONE GETS "
          "TRAPPED INSIDE THE PAST","DREAMS CAN TURN TO NIGHTMARES FAST"],
    "40":["SOOS LATER FORCED MCGUCKET TO WATCH ALL 900 HOURS OF NEON CRISIS MECHABOT BOY: REVELATIONS","TEN SYMBOLS "
          "PLACED AROUND A WHEEL","HAND IN HAND THEY'LL BOND THE SEAL","BUT BREAK THE CHAIN, AND PAY THE COST",
          "THE PROPHECY WILL ALL BE LOST"],
    "41":["SECRETS LOST AND STATUES FOUND BEYOND THE RUSTY GATES","GOODBYE GRAVITY FALLS","FADED PICTURES BLEACHED BY "
          "SUN","THE TALE'S TOLD, THE SUMMER'S DONE","IN MEMORIES THE PINES STILL PLAY","ON A SUNNY SUMMER'S DAY"]
}

def shift(lista, desfase):
    return lista[desfase:] + lista[:desfase]


def insertString(texto,caracter,ubicacion):
    textoN= texto[:ubicacion]+caracter+texto[ubicacion:]
    return textoN

def vigenere(texto,key):
    abcdario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z"]
    matriz=[]
    for i in range(len(abcdario)):
        matriz.append(shift(abcdario,i))
    M=np.array(matriz)
    clave=key
    while len(key)<len(texto):
        key+=clave
    contador=0
    key = key.replace(" ","")
    for letra in texto:
        if(letra not in abcdario):
            key=insertString(key,letra,contador)
        contador+=1



    resultado=""
    for i in range(len(texto)):
        if(texto[i] not in abcdario):
            resultado+=texto[i]
        else:
            columna=abcdario.index(key[i])
            for j in range(len(abcdario)):
                if( M[j,columna] == texto[i]):
                    fila=j
            resultado+=abcdario[fila]

    return resultado

def number(cypherText,dicc_Epi):
    decypherText=""
    #print(cypherText)

    cypherText =cypherText.replace("][", "-")
    cypherText =cypherText.replace("] [", "-")
    cypherText = cypherText.replace("[", "")
    cypherText =cypherText.replace("]", "")
    cypherText = cypherText.replace(" ", ",")
    #print(cypherText)
    episode = ""
    numero = ""
    for i in range(len(cypherText)):
        if cypherText[i].isnumeric():
            numero=numero+cypherText[i]
            if len(cypherText)-1==i:
                #print("numero = "+numero)
                decypherText = decypherText + episode[int(numero) - 1]
                #print(episode[int(numero) - 1])
        elif len(numero)>0:
            #print("numero = "+numero)
            if cypherText[i] == ")":
                episode = dicc_Epi[numero]
                if isinstance(episode, list):
                    episode = episode[-1]
                episode = clean_string(episode)
            else:

                #print(episode[int(numero)-1])
                decypherText = decypherText + episode[int(numero) - 1]
                if cypherText[i]=="-":
                    decypherText = decypherText + " "
            numero = ""

    return decypherText

def clean_string(string):
    result = ""
    for i in string:
        if i.isalpha():
            result = result + i
    #print("limpio "+result)
    return result

print("\n\t\t\t\t\t------Shorts-------")
number_short=[ "[1)14] [2)5,24 3)3] [5)7,9]","[6)33,40,46 9)1,18] [10)32,33][39","11)4,12,18] [12)8,9][17,18]",
               "[13) 8,9,10] [14,17,22","[14)21,30,32 15)13,20][22 16)20","[17)6,12 20) 3,4]"]
caesar_short=["IURP WKH ILUVW XQWLO WKH ODVW VHDUFK WKH","FRGHV RI FUHGLWV SDVW RQH PHDQV RQH VR VHDUFK",
              "WKHP DOO ZHOFRPH WR JUDYLWB IDOOV"]

print("\n\t\t\t\t-----CAESAR-------")
for i in caesar_short:
    code = caesar(i)
    print(code,end=" ")
print("\n\t\t\t\t-----NUMBER-------")
for i in number_short:
    code = number(i,chapters_decoded)
    print(code,end=" ")

print("\n\n\t\t\t\t\t-----Second Season-------")
combined2_list = ["5-19-23-6-21-16 18-9-6 4-16-19... ","4-16-19 11-23-10 20-9-1-10-5-4-23-15-6-5 15-5 2-19-6-25 21-12-19-2-19-6",
                  "21-23-10 16-19 16-15-20-19 16-15-5 8-12-23-10-5 18-9-6-19-2-19-6?","15-11-8-6-9-8-19-6 3-5-19 9-18 11-23-21-16-15-10-19-6-25 21-9-3-12-20",
                  "12-19-23-20 4-9 3-4-4-19-6 21-23-4-23-5-4-6-9-8-16-19","9-12-20 11-23-10 5-12-19-19-8-15-10-17 9-10 4-16-19 17-6-19-19-10",
                  "21-23-10'4 16-19-12-8 22-3-4 1-9-10-20-19-6 1-16-23-4 16-19'5 5-19-19-10","10-9 8-3-8-8-19-4 5-4-6-15-10-17-5 21-23-10 16-9-12-20 11-19 20-9-1-10",
                  "5-9 8-23-4-15-19-10-4-12-25 15 1-23-4-21-16 4-16-15-5 4-9-1-10","23-22-10-9-6-11-23-12 5-9-9-10 1-15-12-12 22-19 4-16-19 10-9-6-11",
                  "19-10-14-9-25 4-16-19 21-23-12-11 22-19-18-9-6-19 4-16-19 5-4-9-6-11","1-15-10-10-15-10-17 16-19-23-6-4-5 22-25 20-23-25-12-15-17-16-4",
                  "8-9-5-5-19-5-5-15-10-17 6-9-22-9-4-5 22-25 11-9-9-10-12-15-17-16-4","16-19-6 19-11-9-4-15-9-10-23-12 22-23-17-17-23-17-19 15-5 23 6-19-23-12 18-6-15-17-16-4",
                  "5-16-19 16-23-5 4-16-19 9-10-19 10-23-11-19 17-15-18-18-23-10-25","23-12-12 23-10-15-11-23-4-15-9-10",
                  "15-5 22-12-23-21-13 11-23-17-15-21","17-15-20-19-9-10’5 4-23-10-4-6-3-11-5, 11-15-5-5-8-19-12-12-19-20 4-23-4-4-9-9-5,",
                  "5-16-23-10-20-6-23’5 6-19-14-19-21-4-15-9-10-5, 5-9-21-15-19-4-25’5 2-15-19-1-5,","23 18-19-23-6 9-18 1-15-4-21-16-19-5, 23 12-15-18-19 9-18 6-19-17-6-19-4,",
                  "4-16-19-5-19 23-6-19 4-16-19 4-16-15-10-17-5 4-16-23-4 4-16-19-25 4-6-25 4-9 18-9-6-17-19-4",
                  "14-9-15-10 4-16-19 4-15-11-19 8-23-6-23-20-9-26 23-2-9-15-20-23-10-21-19 19-10-18-9-6-21-19-11-19-10-4 5-7-3-23-20-6-9-10!",
                  "17-6-19-23-4 16-9-3-6-5!","5-9-12-15-20 22-19-10-19-18-15-4-5!","5-15-17-10 3-8 25-19-5-4-19-6-20-23-25!",
                  "23-4 4-16-19 8-12-23-25 9-6 23-4 4-16-19 18-23-15-6,","15 23-12-1-23-25-5 5-19-19 4-16-19-11 5-4-23-10-20-15-10-17 4-16-19-6-19",
                  "20-6-19-5-5-19-20 15-10 22-12-23-21-13 4-16-19-25'6-19 9-10 11-25 12-23-1-10,","22-3-4 1-16-19-10 15 4-3-6-10 11-25 16-19-23-20 4-16-19-25'6-19 17-9-10-19",
                  "5-4-23-10-15-5-10-9-4-1-16-23-4-16-19-5-19-19-11-5","5-4-23-10-15-5-10-9-4-1-16-23-4-16-19-5-19-19-11-5",
                  "5-4-23-10-15-5-10-9-4-1-16-23-4-16-19-5-19-19-11-5","4-16-15-6-4-25 25-19-23-6-5 23-10-20 10-9-1 16-19’5 22-23-21-13",
                  "4-16-19 11-25-5-4-19-6-25 15-10 4-16-19 11-25-5-4-19-6-25 5-16-23-21-13","23 5-4-3-22-22-9-6-10 4-9-3-17-16 10-19-1 14-19-6-5-19-25 10-23-4-15-2-19",
                  "18-15-12-22-6-15-21-13 1-23-5-10'4 4-9-9 21-6-19-23-4-15-2-19","16-23-2-15-10-17 4-1-15-10-5 1-23-5 10-9-4 16-15-5 8-12-23-10",
                  "5-9 16-19 14-3-5-4 5-16-6-3-17-17-19-20 23-10-20 10-23-11-19-20 22-9-4-16 5-4-23-10","18-3-10 23-10-20 17-23-11-19-5 23-6-19 17-6-19-23-4 20-15-5-4-6-23-21-4-15-9-10-5",
                  "22-3-4 5-11-23-12-12 4-16-15-10-17-5 21-23-10 16-23-2-19 21-16-23-15-10 6-19-23-21-4-15-9-10-5",
                  "22-19 1-23-6-25 9-18 1-16-9-11 25-9-3 22-19-12-15-4-4-12-19","22-15-17 8-6-9-22-12-19-11-5 21-23-10 5-4-23-6-4 9-3-4 1-15-20-20-12-19",
                  "15-10 21-15-8-16-19-6'5 17-23-11-19 16-19 10-19-19-20-5 23 8-23-1-10","22-19 5-3-6-19 4-9 13-10-9-1 1-16-15-21-16 5-15-20-19 25-9-3'6-19 9-10",
                  "21-23-6-12-23 11-21-21-9-6-13-12-19 6-19-4-3-6-10-19-20 23-12-12 16-15-5 18-12-9-1-19-6-5",
                  "11-23-6-15-12-25-10 20-15-2-9-6-21-19-20 16-15-11 23-18-4-19-6 9-10-12-25 5-15-26 16-9-3-6-5",
                  "22-19-23-4-6-15-21-19 5-12-23-8-8-19-20 16-15-11 18-9-6 22-19-15-10-17 23 21-23-20",
                  "9-12-20 17-9-12-20-15-19'5 4-16-19 22-19-5-4 17-15-6-12-18-6-15-19-10-20 5-4-23-10 19-2-19-6 16-23-20",
                  "4-16-19 8-6-9-8-16-19-21-25 5-19-19-11-19-20 18-23-6 23-1-23-25","22-3-4 18-15-10-23-12-12-25 1-19'2-19 6-19-23-21-16-19-20 4-16-19 20-23-25.",
                  "17-15-2-19 3-8 4-16-19 8-23-5-4. 19-11-22-6-23-21-19 4-16-19 5-4-6-23-10-17-19.",
                  "19-2-19-6-25-4-16-15-10-17 25-9-3 21-23-6-19 23-22-9-3-4 1-15-12-12 21-16-23-10-17-19.",
                  "17-23-11-19 15-5 9-2-19-6, 23-10-20 15 1-9-10","10-9-1 15-4'5 4-15-11-19 4-9 5-4-23-6-4 4-16-19 18-3-10",
                  "15 23-12-1-23-25-5 12-9-2-19 21-9-6-6-3-8-4-15-10-17 12-15-2-19-5","10-9-1 12-19-4'5 5-19-19 1-16-15-21-16 8-15-10-19-5 5-3-6-2-15-2-19-5",
                  "1-16-19-10 9-10-19 17-19-4-5 4-6-23-8-8-19-20 15-10-5-15-20-19 4-16-19 8-23-5-4","20-6-19-23-11-5 21-23-10 4-3-6-10 4-9 10-15-17-16-4-11-23-6-19-5 18-23-5-4",
                  "4-19-10 5-25-11-22-9-5 8-12-23-21-19-20 23-6-9-3-10-20 23 1-16-19-19-12","16-23-10-20 15-10 16-23-10-20 4-16-19-25'12-12 22-9-10-20 4-16-19 5-19-23-12",
                  "22-3-4 22-6-19-23-13 4-16-19 21-16-23-15-10, 23-10-20 8-23-25 4-16-19 21-9-5-4","4-16-19 8-6-9-8-16-19-21-25 1-15-12-12 23-12-12 22-19 12-9-5-4",
                  "18-23-20-19-20 8-15-21-4-3-6-19-5 22-12-19-23-21-16-19-20 22-25 5-3-10","4-16-19 4-23-12-19'5 4-9-12-20, 4-16-19 5-3-11-11-19-6'5 20-9-10-19",
                  "15-10 11-19-11-9-6-15-19-5 4-16-19 8-15-10-19-5 5-4-15-12-12 8-12-23-25","9-10 23 5-3-10-10-25 5-3-11-11-19-6'5 20-23-25"]

print("\n\t\t\t\t-----Combined-------")
for i in combined2_list:
    code = combined1(i)
    print(code)
print("\n\t\t\t\t-----A1Z26-------")
A1Z26_list2 = ["6-12-1-7"]

print(A1Z26(A1Z26_list2[0]))

print("\n\t\t\t\t-----CAESAR-------")

caesar_list2 = ["TEV FP TBKAV PL MBOCBZQ","ZDWFK RXW","NLOO PH SOHDVH","ZLGGOH","VKLIWHU","ZKDWHYV","EHDUR",
                "VWDQ LV QRW ZKDW KH VHHPV","JXYDPHQW"]

def caesar2(cypherText):
    decypherText=""
    for j in cypherText:
        if 65 <= ord(j) and ord(j) <= 90:
            changed = ord(j) + 3
            if changed > 90:
                changed = 64 + changed - (90)
                #print("in")
            decypherText = decypherText + str(chr(changed))
        else:
            decypherText = decypherText + j
    return decypherText

n = 1
for i in caesar_list2:
    if n == 1:
        code = caesar2(i)
        n+=1
    else:
        code = caesar(i)
    print(code)


vigenere_list = [["SMOFZQA JDFV","WIDDLE"],["OOIY DMEV VN IBWRKAMW BRUWLL","SHIFTER"],["NLMXQWWN IIZ LZFNF","WHATEVS"],
                 ["YM’KL ECN PPK WFOM UBR KQVXNLK, DCI SIK’U VDA JFTOTA AYQ BWL VVCT \"EBTGGB BHWKGZH\" HVV: TMEASZFA LOS YCDT PRWKTIYEKGL DBV XQDTYRDGVI",
                  "CIPHER"],["BRTYMEMNX QBR HRRQPEE","BEARO"],["PVREK BIG QF. JCDQZRF’ ZNVEFH OBCX: \"C BEWRS VVUTBFL BT BKNX CVAY BKNX CVAY BKNX\"",
                  "NONCANON"],["MXNGVEECW MW SLAWW. SUL FPZSK MW SOJMRX.","ERASE"],["FOC'T FW MVV VIBE EZBAV KF NOW KTB'K FO IHG BBAV VIBE.",
                  "CAPACITOR"],["O SAM KVGS.","GOATANDAPIG"],["PYOL YS QH LLFDJW: UAH DNCVFW ZTCKW XKG WFFWWKNLLMRP? WISAGCXJ AR WKUISW! DPX WDSUKXR: LLH UBFO.",
                  "CURSED"],["LAR ZPUHTFTY XWEUPJR GHGZT","STNLYMBL"],["TIZOLHAJSIW CKMMWZPMKQ: GLY KJQBH","SIXER"],
                 ["VXFQLKB-AYRTHHEJ!","RADMASTER"],["CWZSQVQBEWZSQVQBEWZSQVQMPHKD 'MZ!","WORKINIT"],
                 ["S UPYTYH DIP GAVO QETHI MCBK OHK XEXJB VRW YOUWCHIA VRSV OQ LRDIA","SCHMENDRICK"],
                 ["VCDH, PZNS P CSSOS VDPUHB GTXILSKTV, VYSCIYROZN USLQR WXW NDM WDQVZOGS, EEG PTUVZHBSTH R WOAZMEJ PJAPURU PCH JDGHN GRW OADRX WVT LEP",
                  "DOPPER"],["ETX CPI ASTD GI?","BLUE BOOK"],["KB HTMT IHOV 1,000 AMLCT NDY XZOM MLCG'H TSCGKFWFA IV VVEWYDUQIBXV, CVO HIMC OI'J DINV, IM'H NSZPO EZ CM KLVP EZLYLG",
                  "CILLBIPHER"],["FZPO YSU BQSHZ LTLY FR LV UCC IFJ CIYHO LTEYWKQWUW II P KFASJ JKQASPJE'W LLOMKXQNFR FLWEDGI","DIPPYFRESH"],
                 ["KVOU VTKSE XVREOW DQTMJKGD MF KNLJH CVE 900 YCHJZ OH XXFB PJPSKC FVQUSIOV LHP: FRNLLCDBFBF","SHACKTRON"],
                 ["ZMFUIGV PSHP IGK AGTAYAG TRMNE VVGSQW KLE JOJXU GIMWZ","HIDDEN DEEP WITHIN THE WOODS A BURIED TREASURE WAITS"],
                 ["GLCOPRP GOOGWMJ FXZWG","AXOLOTL"]]
print("\n\t\t\t\t-----Vigenere-------")
for i in vigenere_list:
    code = vigenere(i[0],i[1])
    print(code)

atbash_lista2 = ["KFIV VMVITB, MLG HPRM ZMW YLMV","IRHRMT ORPV GSV HSVKZIW GLMV","YROO XRKSVI! GIRZMTOV!",
                 "YROO XRKSVI GIRZMTOV"]
print("\n\t\t\t\t-----ATBASH-------")
for i in atbash_lista2:
    code = atbash(i)
    print(code)

print("\n\t\t\t\t-----BINARY-------")

binario_lista2 =["01010000011101010111010000100000011000010110110001101100001000000111001101101001011110000010000001110"
                 "00001101001011001010110001101100101011100110010000001110100011011110110011101100101011101000110100001"
                 "1001010111001000100001","0101001101010000010000010100001101000101010010100100000101001101010101000101"
                 "011101001111"]

def binary(cypherText):
    n = int(cypherText, 2)
    n = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
    return n


for i in binario_lista2:
    code = binary(i)
    print(code)