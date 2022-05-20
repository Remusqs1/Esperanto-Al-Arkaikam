from enum import Enum
from typing import Literal

#TODO modifi por ke ĝi ankaŭ dividu je specialaj signoj kiel ", . ! ?", ĉar ili
#malfunkciigas la dividadon

def dividado(enigo):
    enigo = enigo.split(" ")
    return enigo

def kunigado(matrico):
    frazo = " "
    frazo = frazo.join(matrico)
    return frazo

def pronomaListo():
    pronomaListo = ['mi', 'vi', 'ci', 'li', 'ŝi', 'ĝi', 'ili', 'ni', 'si', 'oni']
    return pronomaListo

class VortoKlaso(Enum):
    SUBSTANTIVO = 0
    ADJEKTIVO = 1
    ADVERBO = 2,
    PREPOZICIO = 3,
    KONJUNKCIO = 4,
    ARTIKOLO = 5,
    VERBO = 7, #TODO ALDONI PLIAJN POR VERBAJN KLASOJN, TIAL KOMENCIĜAS JE 7
    AKUZATIVO = 8 #Jen ekzemplo de la antaŭa komento

def kontroliVortoKlason(vorto : str ,vortoKlaso:VortoKlaso)-> bool:
    eliro = False
    if(vortoKlaso == VortoKlaso.SUBSTANTIVO):
        if(len(vorto)>2):
            if(vorto[-1] == "o" or vorto[-2:]=="oj" or vorto[-2:]=="on" or vorto[-3:]=="ojn"):
                eliro = True
        else:
            if(vorto[-1] == "o" or vorto[-2:]=="oj"):
                eliro = True
    elif(vortoKlaso == VortoKlaso.ADJEKTIVO):
        if(len(vorto)>2):
            if(vorto[-1] == "a" or vorto[-2:]=="aj" or vorto[-2:]=="an" or vorto[-3:]=="ajn"):
                eliro = True
        else:
            if(vorto[-1] == "a" or vorto[-2:]=="aj"):
                eliro = True
    elif((vortoKlaso == VortoKlaso.ADVERBO) and (vorto[-1] == "e" or vorto[-2:]=="en")):
        eliro = True
    elif((vortoKlaso.ARTIKOLO) and (vorto == "la")):
        eliro = True
    elif((vortoKlaso ==VortoKlaso.AKUZATIVO)  and vorto[-1] == "n"):
        eliro = True
    return eliro