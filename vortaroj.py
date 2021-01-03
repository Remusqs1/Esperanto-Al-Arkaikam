from iloj import dividado, kunigado

def pronomaVortaro(enigo):

    pronomaVortaro = {'mi': 'Mihi', 'vi': 'Wos', 'ci': 'Tu', 'li': 'Lùi',
                      'ŝi': 'Eshi', 'ĝi': 'Eghi', 'ili': 'Ilùi', 'ni': 'Nos', 'si': 'Sihi'}

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
                       'ekster': 'extrum', 'ekde': 'ab', 'kontraŭ': 'contraŭ', 'kvankam': 'cùanquaŭ',
                       'ne' : 'ned'}
    for ŝlosilo in specialaVortaro:
        matrico = dividado(enigo)
        for i in range(len(matrico)):
            if(ŝlosilo == matrico[i]):
                matrico[i] = matrico[i].replace(
                    ŝlosilo, specialaVortaro[ŝlosilo])
        enigo = kunigado(matrico)
    return (enigo)
