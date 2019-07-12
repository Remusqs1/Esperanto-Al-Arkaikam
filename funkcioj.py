# vorto=input("Enigu frazon: ") #Tio ĉi forigeblas, nur estas por ke 'vorto' eniru en la funkcio

pronomaListo = ['mi', 'vi', 'ci', 'li', 'ŝi', 'ĝi', 'ili', 'ni', 'si']

def substantivoSingulara(vorto):
    Vorto=vorto.capitalize()#Arkaike, substantivo estas ĉiam skribita majuskle je kia ajn kazo
    Vorto=Vorto+"m"

    return (Vorto)

# substantivoSingulara(vorto)

def pronomoj(vorto):
    for i in range(len(vorto)):
        if vorto[i] in pronomaListo:
            print (vorto[i] + ' estas pronomo')
        else:
            print (vorto[i] + ' NE estas pronomo')

def artikoloDifinitaForigado(vorto):
    for i in range(len(vorto)):
        if vorto[i] == "la":
            print (vorto[i] + ' estas difinita artikolo')
            vorto.remove(vorto[i])
            return print ("Listo: " + str(vorto))

       
