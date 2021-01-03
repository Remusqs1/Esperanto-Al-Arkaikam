from iloj import dividado, kunigado

def pronomaVortaro(enigo):

    #Ne majuskliĝas #TODO krei kodon por anstataŭi ĉi tiu vortaron
    pronomaVortaro = {'mi': 'mihi', 'miam': 'miham', 'miay': 'mihaym', 'min': 'mihin', 'mian': 'mihan', 'miayn': 'mihayn', 'mies': 'mihes',
                      'ci': 'tu', 'ciam': 'tuam', 'ciay': 'tuay', 'cin': 'tuin', 'cian': 'tuan', 'ciayn': 'tuayn', 'cies': 'tues',
                      'vi': 'wos', 'viam': 'wosam', 'viay': 'wosay', 'vin': 'wosin', 'vian': 'wosan', 'viayn': 'wosayn', 'vies': 'woses',
                      'li': 'lùi', 'liam': 'lùiam', 'liay': 'lùiay', 'lin': 'lùin', 'lian': 'lùian', 'liayn': 'lùiayn', 'lies': 'lùies',
                      'ŝi': 'eshi', 'ŝiam': 'eshiam', 'ŝiay': 'eshiay', 'ŝin': 'eshin', 'ŝian': 'eshian', 'ŝiayn': 'eshiayn', 'ŝies': 'eshies',
                      'ĝi': 'eghi', 'ĝiam': 'eghiam', 'ĝiay': 'eghiay', 'ĝin': 'eghin', 'ĝian': 'eghian', 'ĝiayn': 'eghiayn', 'ĝies': 'eghies',
                      'ili': 'ilùi', 'iliam': 'ilùiam', 'iliay': 'ilùiay', 'ilin': 'ilùin', 'ilian': 'ilùian', 'iliayn': 'ilùiayn', 'ilies': 'ilùies',
                      'ni': 'nos', 'niam': 'nosam', 'niay': 'nosay', 'nin': 'nosin', 'nian': 'nosan', 'niayn': 'nosayn', 'nies': 'noses',
                      'si': 'sihi', 'siam': 'siham', 'siay': 'sihay', 'sin': 'sihin', 'sian': 'sihan', 'siayn': 'sihayn', 'sies': 'sihes',}

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
