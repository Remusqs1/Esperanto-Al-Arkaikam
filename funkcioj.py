# TODO listo kaj traduko de specialaj vortoj
from iloj import *
from vortaroj import pronomaVortaro

def AŭAnstataŭado(matrico):
    for i in range(len(matrico)):
        index = matrico.index(matrico[i])
        if matrico[i][-2:] == "aŭ":
            matrico[i] = matrico[i][:-2]
            Vortez = (matrico[i]+"ez")
            del matrico[i]
            matrico.insert(index, Vortez)
    return (matrico)

def Artikoloj(matrico):
    provizoraListo = []
    nombrilo = 0
    for i in range(len(matrico)):
        index = matrico.index(matrico[i])
        if (matrico[i] != "la"):
            if(kontroliVortoKlason(matrico[i], VortoKlaso.SUBSTANTIVO) and (matrico[i-1] != "la")):
                provizoraListo.insert(index+nombrilo, "unn")
                nombrilo+=1
            provizoraListo.append(matrico[i])
    matrico = provizoraListo
    return matrico

def Substantivo(matrico:list):
    for i in range(len(matrico)):
        index = matrico.index(matrico[i])
        if matrico[i][-1] == "o":
            # Arkaike, substantivo estas ĉiam skribita majuskle je kia ajn kazo
            Vortom = (matrico[i]+"m").capitalize()
            del matrico[i]
            matrico.insert(index, Vortom)
        elif matrico[i][-2:] == "oj":  # Same sed ne plurale
            matrico[i] = matrico[i][:-1]
            Vortoy = (matrico[i]+"y").capitalize()
            del matrico[i]
            matrico.insert(index, Vortoy)

def Adjektivo(matrico):
    for i in range(len(matrico)):
        index = matrico.index(matrico[i])
        if matrico[i][-1] == "a":
            Vortom = (matrico[i]+"m")
            del matrico[i]
            matrico.insert(index, Vortom)
        elif matrico[i][-2:] == "aj":  # Same sed ne plurale
            matrico[i] = matrico[i][:-1]
            Vortoy = (matrico[i]+"y")
            del matrico[i]
            matrico.insert(index, Vortoy)
    return (matrico)

def Akuzativo(matrico):
    for i in range(len(matrico)):
        index = matrico.index(matrico[i])
        if matrico[i][-3:] == "ojn":
            matrico[i] = matrico[i][:-2]
            # Arkaike, substantivo estas ĉiam skribita majuskle je kia ajn kazo
            Vortoyn = (matrico[i]+"yn").capitalize()
            del matrico[i]
            matrico.insert(index, Vortoyn)
        elif matrico[i][-2:] == "on":  # Same sed ne plurale
            Vorton = matrico[i].capitalize()
            del matrico[i]
            matrico.insert(index, Vorton)
        elif matrico[i][-3:] == "ajn":  # Por adjektivo plurala. Singulara resta senŝanĝe
            matrico[i] = matrico[i][:-2]
            Vortayn = (matrico[i]+"yn")
            del matrico[i]
            matrico.insert(index, Vortayn)
    return (matrico)

def Adverbo(matrico):
    for i in range(len(matrico)):
        index = matrico.index(matrico[i])
        if matrico[i][-1] == "e":
            matrico[i] = matrico[i][:-1]
            Vortoyn = (matrico[i]+"œ")
            del matrico[i]
            matrico.insert(index, Vortoyn)
    return (matrico)

def Verboj(matrico):
    pronomoj = pronomaListo()
    verbajFinaĵoj = ["as", "is", "os", "us"]  # Sen imperativo
    #Vortordo ne estas libera
    #Ci-verbon restas senŝanĝaj
    for i in range(len(matrico)):
        if matrico[i] in pronomoj:
            provizoraListo = matrico
            try:
                if matrico[i] == "mi":
                    if matrico[i+1][-2:] in verbajFinaĵoj:
                        provizoraListo[i+1] = provizoraListo[i+1][:-1]
                        Verbom = (provizoraListo[i+1]+"ms")
                        del provizoraListo[i+1]
                        provizoraListo.insert(i+1, Verbom)
                elif matrico[i] == "vi":
                    if matrico[i+1][-2:] in verbajFinaĵoj:
                        provizoraListo[i+1] = provizoraListo[i+1][:-1]
                        Verbom = (provizoraListo[i+1]+"is")
                        del provizoraListo[i+1]
                        provizoraListo.insert(i+1, Verbom)
                    elif matrico[i+1][-1:] == "u":
                        Verbom = (provizoraListo[i+1]+"y")
                        del provizoraListo[i+1]
                        provizoraListo.insert(i+1, Verbom)
                elif (matrico[i] == "ŝi" or matrico[i] == "li" or matrico[i] == "ĝi" or matrico[i] == "oni"):
                    if matrico[i+1][-2:] in verbajFinaĵoj:
                        provizoraListo[i+1] = provizoraListo[i+1][:-1]
                        Verbom = (provizoraListo[i+1]+"t")
                        del provizoraListo[i+1]
                        provizoraListo.insert(i+1, Verbom)
                elif matrico[i] == "ni":
                    if matrico[i+1][-2:] in verbajFinaĵoj:
                        provizoraListo[i+1] = provizoraListo[i+1][:-1]
                        Verbom = (provizoraListo[i+1]+"ims")
                        del provizoraListo[i+1]
                        provizoraListo.insert(i+1, Verbom)
                    elif matrico[i+1][-1:] == "u":
                        Verbom = (provizoraListo[i+1]+"y")
                        del provizoraListo[i+1]
                        provizoraListo.insert(i+1, Verbom)
                elif matrico[i] == "ili":
                    if matrico[i+1][-2:] in verbajFinaĵoj:
                        provizoraListo[i+1] = provizoraListo[i+1][:-1]
                        Verbom = (provizoraListo[i+1]+"it")
                        del provizoraListo[i+1]
                        provizoraListo.insert(i+1, Verbom)
                    elif matrico[i+1][-1:] == "u":
                        Verbom = (provizoraListo[i+1]+"y")
                        del provizoraListo[i+1]
                        provizoraListo.insert(i+1, Verbom)
                else:
                    matrico = provizoraListo
            except:
                pass
            matrico = provizoraListo
    return matrico

def prefiksigi(matrico):
    for i in range(len(matrico)):
        try:
            if matrico[i] == "ĉi":
                vorto = "is"+matrico[i+1]
                del matrico[i:i+2]
                matrico.insert(i, vorto)
            elif matrico[i] == "oni":
                vorto = "on"+matrico[i+1]
                del matrico[i:i+2]
                matrico.insert(i, vorto)
            elif matrico[i] == "al" or matrico[i] == "ad":
                if(matrico[i+1] in pronomaListo() or matrico[i+1]=="oni"):
                    vorto = "ad"+matrico[i+1]
                    del matrico[i:i+2]
                    matrico.insert(i, vorto)
        except:
            pass
    return (matrico)

def Pronomoj(matrico):
    pronomoj = pronomaListo()
    for i in range(len(matrico)):
        try:
            if matrico[i][:2] in pronomoj or matrico[i][:3] in pronomoj:
                matrico[i] = pronomaVortaro(matrico[i])
                
        except:
            pass
    return matrico