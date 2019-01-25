### La celo de ĉi programeto estas ke uzanto enmetu frazon, ekz: Mi estas frazo,
### kaj la programo redonu tutan tradukon al Arkaikam: Mihi estams Frazom

from funkcioj import *

Frazo=input("Enigu vian frazon: ")
frazo=Frazo.lower()

#Dividas la vortojn de la frazo laŭ malplena spaco. Poste ĉiu ero estos legita kaj kategoriita laŭ finaĵo.
ĉeno=frazo.split(" ")
print(ĉeno)#Forigota, nune nur por vidi la ĉenon

for i in range(len(ĉeno)):

    lastaLitero=ĉeno[i][-1] #Legas la lastan literon de vorto

    #Jen funkcio por scii ĉu vorto estas substantivo aŭ ne, se jes, konjugacias arkaike
    if lastaLitero=="o":
        print(ĉeno[i] + ' estas substantivo') #ĉeno[i] estas vorto, ĉi tio forigotos
        
        #Konjugacio arkaika
        vortoAE=substantivoSingulara(ĉeno[i])
        print(ĉeno[i] + " tradukita al Arkaikam estus: " + vortoAE)
    else:
        print(ĉeno[i] + ' ne estas substantivo')