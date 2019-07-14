# vorto=input("Enigu frazon: ") #Tio ĉi forigeblas, nur estas por ke 'vorto' eniru en la funkcio

pronomaListo = ['mi', 'vi', 'ci', 'li', 'ŝi', 'ĝi', 'ili', 'ni', 'si']

def substantivoSingulara(matrico):
    for i in range(len(matrico)):
        if matrico[i][-1]=="o":
            index=matrico.index(matrico[i])
            Vortom=(matrico[i]+"m").capitalize() #Arkaike, substantivo estas ĉiam skribita majuskle je kia ajn kazo
            matrico.remove(matrico[i])
            matrico.insert(index, Vortom)
    return (matrico)

def substantivoPlurala(matrico):
    for i in range(len(matrico)):
        if matrico[i][-1]=="j":
            index=matrico.index(matrico[i])
            matrico[i]=matrico[i][:-1]
            Vortoy=(matrico[i]+"y").capitalize() #Arkaike, substantivo estas ĉiam skribita majuskle je kia ajn kazo
            matrico.remove(matrico[i])
            matrico.insert(index, Vortoy)
    return (matrico)

def pronomoj(matrico):
    for i in range(len(matrico)):
        index=matrico.index(matrico[i])        
        if matrico[i] in pronomaListo:
            if (matrico[i]== "mi"):
                matrico[i]="mihi"
            elif (matrico[i]== "vi"):
                matrico[i]="wos"
            elif (matrico[i]== "ci"):
                matrico[i]="tu"
            elif (matrico[i]== "li"):
                matrico[i]="lùi"
            elif (matrico[i]== "ŝi"):
                matrico[i]="eshi"
            elif (matrico[i]== "ĝi"):
                matrico[i]="eghi"
            elif (matrico[i]== "ili"):
                matrico[i]="ilùi"
            elif (matrico[i]== "ni"):
                matrico[i]="nos"
            elif (matrico[i]== "si"):
                matrico[i]="sihi"

def artikoloDifinitaForigado(matrico):
    for i in range(len(matrico)):
        if matrico[i] == "la":
            matrico.remove(matrico[i])
            return matrico

def kunigado(matrico):
    frazoT=" "
    frazoT=frazoT.join(matrico)
    print(frazoT)
    return frazoT