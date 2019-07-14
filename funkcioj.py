pronomaListo = ['mi', 'vi', 'ci', 'li', 'ŝi', 'ĝi', 'ili', 'ni', 'si']

# TODO listo kaj traduko de specialaj vortoj

def AŭŜanĝo(matrico):
    for i in range(len(matrico)):
        index=matrico.index(matrico[i])
        if matrico[i][-2:]=="aŭ":
            matrico[i]=matrico[i][:-2]
            Vortez=(matrico[i]+"ez")
            matrico.remove(matrico[i])
            matrico.insert(index, Vortez)
    return (matrico)

def Substantivo(matrico):
    for i in range(len(matrico)):
        index=matrico.index(matrico[i])
        if matrico[i][-1]=="o":
            Vortom=(matrico[i]+"m").capitalize() #Arkaike, substantivo estas ĉiam skribita majuskle je kia ajn kazo
            matrico.remove(matrico[i])
            matrico.insert(index, Vortom)
        elif matrico[i][-2:]=="oj": #Same sed ne plurale
            matrico[i]=matrico[i][:-1]
            Vortoy=(matrico[i]+"y").capitalize() 
            matrico.remove(matrico[i])
            matrico.insert(index, Vortoy)            

def Adjektivo(matrico):
    for i in range(len(matrico)):
        index=matrico.index(matrico[i])
        if matrico[i][-1]=="a":
            Vortom=(matrico[i]+"m")
            matrico.remove(matrico[i])
            matrico.insert(index, Vortom)
        elif matrico[i][-2:]=="aj": #Same sed ne plurale
            matrico[i]=matrico[i][:-1]
            Vortoy=(matrico[i]+"y")
            matrico.remove(matrico[i])
            matrico.insert(index, Vortoy)            
    return (matrico)

def Akuzativo(matrico):
    for i in range(len(matrico)):
        index=matrico.index(matrico[i])
        if matrico[i][-3:]=="ojn":
            matrico[i]=matrico[i][:-2]
            Vortoyn=(matrico[i]+"yn").capitalize() #Arkaike, substantivo estas ĉiam skribita majuskle je kia ajn kazo
            matrico.remove(matrico[i])
            matrico.insert(index, Vortoyn)
        elif matrico[i][-2:]=="on": #Same sed ne plurale
            Vorton=matrico[i].capitalize()
            matrico.remove(matrico[i])
            matrico.insert(index, Vorton)
        elif matrico[i][-3:]=="ajn": #Por adjektivo plurala. Singulara resta senŝanĝe
            matrico[i]=matrico[i][:-2]
            Vortayn=(matrico[i]+"yn")
            matrico.remove(matrico[i])
            matrico.insert(index, Vortayn)
    return (matrico)

def Adverbo(matrico):
    for i in range(len(matrico)):
        index=matrico.index(matrico[i])
        if matrico[i][-1]=="e":
            matrico[i]=matrico[i][:-1]
            Vortoyn=(matrico[i]+"œ")
            matrico.remove(matrico[i])
            matrico.insert(index, Vortoyn)
    return (matrico)    

def Pronomoj(matrico):
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

def ArtikoloDifinitaForigado(matrico):
    for i in range(len(matrico)):
        if matrico[i] == "la":
            matrico.remove(matrico[i])
            return matrico

def Kunigado(matrico):
    frazoT=" "
    frazoT=frazoT.join(matrico)
    print(frazoT)
    return frazoT