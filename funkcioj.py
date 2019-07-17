# TODO listo kaj traduko de specialaj vortoj

def SpecialajŜanĝoj(matrico):
    #Havi liston estas pli rimedo-efika
    specialaListo = ['fraŭlo', "fraŭlino", "ktp", "sinjoro", "sinjorino", "t.e.", "tre", "sur", "kaj",
     "al", "aŭ", "ĉe", "ĝis", "en", "el", "ekster", "ekde", "eĉ", "ĵus", "ju", "jes", "jen", "je","jam",
     "ja", "kun", "laŭ", "mem", "po", "plu", "pli", "plej", "nepre", "supre", "sub", "sen", "pro", "pri",
     "preskaŭ", "preter", "kontraŭ", "kvankam", "kvazaŭ"]

    for i in range(len(matrico)):
        if matrico[i] in specialaListo:
            if (matrico[i]== "fraŭlo"):
                matrico[i]="scùiro"
            elif (matrico[i]== "fraŭlino"):
                matrico[i]="damselo"
            elif (matrico[i]== "supre"):
                matrico[i]="kvazaŭ"
            elif (matrico[i]== "cùazaŭ"):
                matrico[i]="suprez"
            elif (matrico[i]== "sub"):
                matrico[i]="sobez"
            elif (matrico[i]== "sen"):
                matrico[i]="sonz"
            elif (matrico[i]== "pro"):
                matrico[i]="pru"
            elif (matrico[i]== "pri"):
                matrico[i]="prid"
            elif (matrico[i]== "preskaŭ"):
                matrico[i]="presquaŭ"
            elif (matrico[i]== "preter"):
                matrico[i]="predor"
            elif (matrico[i]== "jam"):
                matrico[i]="yamen"
            elif (matrico[i]== "ja"):
                matrico[i]="yad"
            elif (matrico[i]== "kun"):
                matrico[i]="cum"
            elif (matrico[i]== "laŭ"):
                matrico[i]="selez"
            elif (matrico[i]== "mem"):
                matrico[i]="memes"
            elif (matrico[i]== "po"):
                matrico[i]="pod"
            elif (matrico[i]== "plu"):
                matrico[i]="plud"
            elif (matrico[i]== "pli"):
                matrico[i]="plid"
            elif (matrico[i]== "plej"):
                matrico[i]="pluy"
            elif (matrico[i]== "nepre"):
                matrico[i]="nepred"
            elif (matrico[i]== "eĉ"):
                matrico[i]="eche"
            elif (matrico[i]== "ĵus"):
                matrico[i]="zhused"
            elif (matrico[i]== "ju"):
                matrico[i]="yud"
            elif (matrico[i]== "jes"):
                matrico[i]="ayest"
            elif (matrico[i]== "jen"):
                matrico[i]="yemen"
            elif (matrico[i]== "je"):
                matrico[i]="iyed"            
            elif (matrico[i]== "ktp"):
                matrico[i]="etc"
            elif (matrico[i]== "sinjoro"):
                matrico[i]="sinyoro"
            elif (matrico[i]== "sinjorino"):
                matrico[i]="mesiro"
            elif (matrico[i]== "t.e." or matrico[i]== "t.e"):
                matrico[i]="ite"
            elif (matrico[i]== "tre"):
                matrico[i]="trez"
            elif (matrico[i]== "sur"):
                matrico[i]="sobrez"
            elif (matrico[i]== "kaj"):
                matrico[i]="ed"
            elif (matrico[i]== "al"):
                matrico[i]="ad"
            elif (matrico[i]== "aŭ"):
                matrico[i]="aù"
            elif (matrico[i]== "ĉe"):
                matrico[i]="chez"
            elif (matrico[i]== "ĝis"):
                matrico[i]="ghisquez"
            elif (matrico[i]== "en"):
                matrico[i]="in"
            elif (matrico[i]== "el"):
                matrico[i]="ex"
            elif (matrico[i]== "ekster"):
                matrico[i]="extrum"
            elif (matrico[i]== "ekde"):
                matrico[i]="ab"
            elif (matrico[i]== "kontraŭ"):
                matrico[i]="contraŭ"
            elif (matrico[i]== "kvankam"):
                matrico[i]="cùanquaŭ"
    return (matrico)

def AŭAnstataŭado(matrico):
    for i in range(len(matrico)):
        index=matrico.index(matrico[i])
        if matrico[i][-2:]=="aŭ":
            matrico[i]=matrico[i][:-2]
            Vortez=(matrico[i]+"ez")
            matrico.remove(matrico[i])
            matrico.insert(index, Vortez)
    return (matrico)

def ArtikoloDifinitaForigado(matrico):
    provizoraListo=[]
    for i in matrico:
        if (i != "la"):
            provizoraListo.append(i)
    matrico = provizoraListo
    return matrico
            
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
    pronomaListo = ['mi', 'vi', 'ci', 'li', 'ŝi', 'ĝi', 'ili', 'ni', 'si']
    for i in range(len(matrico)):
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


def Verboj(matrico):
    #TODO Nur funkcias la unua fojo po pronomo, la vortordo ne estas libera
    for i in range(len(matrico)):
        provizoraListo = matrico        
        index = provizoraListo.index(provizoraListo[i])
        if matrico[i] == "mi":
            if matrico[index+1][-2:] == "as":
                provizoraListo[index+1] = provizoraListo[index+1][:-1]
                Verbom = (provizoraListo[index+1]+"ms")
                provizoraListo.remove(provizoraListo[index+1])
                provizoraListo.insert(index+1, Verbom)
        if matrico[i] == "vi":
            if matrico[index+1][-2:] == "as":
                provizoraListo[index+1] = provizoraListo[index+1][:-1]
                Verbom = (provizoraListo[index+1]+"is")
                provizoraListo.remove(provizoraListo[index+1])
                provizoraListo.insert(index+1, Verbom)
    matrico=provizoraListo
    return matrico 

    #Provi, for i in matrico, novaListo=[]---> if true--> sxangxi kaj append al nL, else nur append al nL ---> matrico = nL

    #Provo solvi, ne funkciis, sed eble la solvo iras en cxi tiu vojo
    # provizoraListo = matrico    
    # for i in matrico:
    #     index = provizoraListo.index(i)
    #     if i == "mi":
    #         if matrico[index+1][-2:] == "as":
    #             provizoraListo[index+1] = provizoraListo[index+1][:-1]
    #             Verbom = (provizoraListo[index+1]+"ms")
    #             provizoraListo.remove(provizoraListo[index+1])
    #             provizoraListo.insert(index+1, Verbom)
    #     matrico = provizoraListo
    # return matrico    

def Kunigado(matrico):
    frazoT=" "
    frazoT=frazoT.join(matrico)
    print(frazoT)
    return frazoT
