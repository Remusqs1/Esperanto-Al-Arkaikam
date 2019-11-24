# TODO listo kaj traduko de specialaj vortoj
from iloj import *

def AŭAnstataŭado(matrico):
    for i in range(len(matrico)):
        index = matrico.index(matrico[i])
        if matrico[i][-2:] == "aŭ":
            matrico[i] = matrico[i][:-2]
            Vortez = (matrico[i]+"ez")
            matrico.remove(matrico[i])
            matrico.insert(index, Vortez)
    return (matrico)

def ArtikoloDifinitaForigado(matrico):
    provizoraListo = []
    for i in matrico:
        if (i != "la"):
            provizoraListo.append(i)
    matrico = provizoraListo
    return matrico

def Substantivo(matrico):
    for i in range(len(matrico)):
        index = matrico.index(matrico[i])
        if matrico[i][-1] == "o":
            # Arkaike, substantivo estas ĉiam skribita majuskle je kia ajn kazo
            Vortom = (matrico[i]+"m").capitalize()
            matrico.remove(matrico[i])
            matrico.insert(index, Vortom)
        elif matrico[i][-2:] == "oj":  # Same sed ne plurale
            matrico[i] = matrico[i][:-1]
            Vortoy = (matrico[i]+"y").capitalize()
            matrico.remove(matrico[i])
            matrico.insert(index, Vortoy)

def Adjektivo(matrico):
    for i in range(len(matrico)):
        index = matrico.index(matrico[i])
        if matrico[i][-1] == "a":
            Vortom = (matrico[i]+"m")
            matrico.remove(matrico[i])
            matrico.insert(index, Vortom)
        elif matrico[i][-2:] == "aj":  # Same sed ne plurale
            matrico[i] = matrico[i][:-1]
            Vortoy = (matrico[i]+"y")
            matrico.remove(matrico[i])
            matrico.insert(index, Vortoy)
    return (matrico)

def Akuzativo(matrico):
    for i in range(len(matrico)):
        index = matrico.index(matrico[i])
        if matrico[i][-3:] == "ojn":
            matrico[i] = matrico[i][:-2]
            # Arkaike, substantivo estas ĉiam skribita majuskle je kia ajn kazo
            Vortoyn = (matrico[i]+"yn").capitalize()
            matrico.remove(matrico[i])
            matrico.insert(index, Vortoyn)
        elif matrico[i][-2:] == "on":  # Same sed ne plurale
            Vorton = matrico[i].capitalize()
            matrico.remove(matrico[i])
            matrico.insert(index, Vorton)
        elif matrico[i][-3:] == "ajn":  # Por adjektivo plurala. Singulara resta senŝanĝe
            matrico[i] = matrico[i][:-2]
            Vortayn = (matrico[i]+"yn")
            matrico.remove(matrico[i])
            matrico.insert(index, Vortayn)
    return (matrico)

def Adverbo(matrico):
    for i in range(len(matrico)):
        index = matrico.index(matrico[i])
        if matrico[i][-1] == "e":
            matrico[i] = matrico[i][:-1]
            Vortoyn = (matrico[i]+"œ")
            matrico.remove(matrico[i])
            matrico.insert(index, Vortoyn)
    return (matrico)

def Verboj(matrico):
    pronomoj=pronomaListo()
    verbajFinaĵoj = ["as", "is", "os", "us"] #Sen imperativo
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
                        provizoraListo.remove(provizoraListo[i+1])
                        provizoraListo.insert(i+1, Verbom)
                elif matrico[i] == "vi":
                    if matrico[i+1][-2:] in verbajFinaĵoj:
                        provizoraListo[i+1] = provizoraListo[i+1][:-1]
                        Verbom = (provizoraListo[i+1]+"is")
                        provizoraListo.remove(provizoraListo[i+1])
                        provizoraListo.insert(i+1, Verbom)
                    elif matrico[i+1][-1:] == "u":
                        Verbom = (provizoraListo[i+1]+"y")
                        provizoraListo.remove(provizoraListo[i+1])
                        provizoraListo.insert(i+1, Verbom)
                elif (matrico[i] == "ŝi" or matrico[i] == "li" or matrico[i] == "ĝi"):
                    if matrico[i+1][-2:] in verbajFinaĵoj:
                        provizoraListo[i+1] = provizoraListo[i+1][:-1]
                        Verbom = (provizoraListo[i+1]+"t")
                        provizoraListo.remove(provizoraListo[i+1])
                        provizoraListo.insert(i+1, Verbom)
                elif matrico[i] == "ni":
                    if matrico[i+1][-2:] in verbajFinaĵoj:
                        provizoraListo[i+1] = provizoraListo[i+1][:-1]
                        Verbom = (provizoraListo[i+1]+"ims")
                        provizoraListo.remove(provizoraListo[i+1])
                        provizoraListo.insert(i+1, Verbom)
                    elif matrico[i+1][-1:] == "u":
                        Verbom = (provizoraListo[i+1]+"y")
                        provizoraListo.remove(provizoraListo[i+1])
                        provizoraListo.insert(i+1, Verbom)
                elif matrico[i] == "ili":
                    if matrico[i+1][-2:] in verbajFinaĵoj:
                        provizoraListo[i+1] = provizoraListo[i+1][:-1]
                        Verbom = (provizoraListo[i+1]+"it")
                        provizoraListo.remove(provizoraListo[i+1])
                        provizoraListo.insert(i+1, Verbom)
                    elif matrico[i+1][-1:] == "u":
                        Verbom = (provizoraListo[i+1]+"y")
                        provizoraListo.remove(provizoraListo[i+1])
                        provizoraListo.insert(i+1, Verbom)
                else:
                    matrico = provizoraListo
            except:
                pass
            matrico = provizoraListo
    return matrico