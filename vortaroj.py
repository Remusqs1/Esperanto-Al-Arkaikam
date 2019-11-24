from iloj import *


def pronomaVortaro(enigo):

    pronomaVortaro = {'mi': 'mihi', 'vi': 'wos', 'ci': 'tu', 'li': 'lùi',
                      'ŝi': 'eshi', 'ĝi': 'eghi', 'ili': 'ilùi', 'ni': 'nos', 'si': 'sihi'}

    for ŝlosilo in pronomaVortaro:
        matrico = dividado(enigo)
        for i in range(len(matrico)):
            if(ŝlosilo == matrico[i]):
                matrico[i] = matrico[i].replace(
                    ŝlosilo, pronomaVortaro[ŝlosilo])
                enigo = kunigado(matrico)
    return (enigo)


def specialajVortoj(enigo):

    specialaVortaro = {'fraŭlo': 'scùiro', 'fraŭlino': 'damselo', 'supre': 'suprez',
                       'kvazaŭ': 'cùazaŭ', 'sub': 'sobez', 'sen': 'sonz', 'pro': 'pru',
                       'pri': 'prid', 'preskaŭ': 'presquaŭ', 'preter': 'predor', 'jam': 'yamen',
                       'ja': 'yad', 'kun': 'cum', 'laŭ': 'selez', 'mem': 'memes', 'po': 'pod',
                       'plu': 'plud', 'pli': 'plid', 'plej': 'pluy', 'nepre': 'nepred', 'eĉ': 'eche',
                       'ĵus': 'zhused', 'ju': 'yud', 'jes': 'ayest', 'jen': 'yemen', 'je': 'iyed',
                       'ktp': 'etc', 'sinjoro': 'sinyoro', 'sinjorino': 'mesiro', 't.e.': 'ite',
                       't.e': 'ite', 'tre': 'trez', 'sur': 'sobrez', 'kaj': 'ed', 'al': 'ad',
                       'aŭ': 'aù', 'ĉe': 'chez', 'ĝis': 'ghisquez', 'en': 'in', 'el': 'ex',
                       'ekster': 'extrum', 'ekde': 'ab', 'kontraŭ': 'contraŭ', 'kvankam': 'cùanquaŭ'}
    for ŝlosilo in specialaVortaro:
        matrico = dividado(enigo)
        for i in range(len(matrico)):
            if(ŝlosilo == matrico[i]):
                matrico[i] = matrico[i].replace(
                    ŝlosilo, specialaVortaro[ŝlosilo])
        enigo = kunigado(matrico)
    return (enigo)
