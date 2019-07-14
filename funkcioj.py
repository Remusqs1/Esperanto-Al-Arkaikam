# vorto=input("Enigu frazon: ") #Tio ĉi forigeblas, nur estas por ke 'vorto' eniru en la funkcio

pronomaListo = ['mi', 'vi', 'ci', 'li', 'ŝi', 'ĝi', 'ili', 'ni', 'si']

def substantivoSingulara(matrico):
    for i in range(len(matrico)):
        if matrico[i][-1]=="o":
            index=matrico.index(matrico[i])
            Ĉenom=(matrico[i]+"m").capitalize() #Arkaike, substantivo estas ĉiam skribita majuskle je kia ajn kazo
            matrico.remove(matrico[i])
            matrico.insert(index, Ĉenom)
    print(matrico)#Forigota
    return (matrico)

def pronomoj(vorto):
    #TODO anstataŭi la pronomon en la liston
    for i in range(len(vorto)):
        if vorto[i] in pronomaListo:
            if (vorto[i]== "mi"):
                vorto[i]="mihi"
            elif (vorto[i]== "vi"):
                vorto[i]="wos"
            elif (vorto[i]== "ci"):
                vorto[i]="tu"
            elif (vorto[i]== "li"):
                vorto[i]="lùi"
            elif (vorto[i]== "ŝi"):
                vorto[i]="eshi"
            elif (vorto[i]== "ĝi"):
                vorto[i]="eghi"
            elif (vorto[i]== "ili"):
                vorto[i]="ilùi"
            elif (vorto[i]== "ni"):
                vorto[i]="nos"
            elif (vorto[i]== "si"):
                vorto[i]="sihi"
            print (vorto[i] + ' estas pronomo')
        else:
            print (vorto[i] + ' NE estas pronomo')

def artikoloDifinitaForigado(vorto):
    for i in range(len(vorto)):
        if vorto[i] == "la":
            print (vorto[i] + ' estas difinita artikolo')
            vorto.remove(vorto[i])
            return print ("Listo: " + str(vorto))

       
