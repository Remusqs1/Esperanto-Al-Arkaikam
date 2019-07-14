### La celo de ĉi programeto estas ke uzanto enmetu frazon, ekz: Mi estas frazo,
### kaj la programo redonu tutan tradukon al Arkaikam: Mihi estams Frazom

from funkcioj import *

frazo=input("Enigu vian frazon: ").lower()

#Dividas la vortojn de la frazo laŭ malplena spaco. TODO Poste ĉiu ero estos legita kaj kategoriita laŭ finaĵo.
ĉeno=frazo.split(" ")

substantivoSingulara(ĉeno)

pronomoj(ĉeno) #Legas la frazeron kaj diras ĉu ĝi estas pronomo, estontece ĝi devos redoni tradukitan pronomon
#TODO pronomoj() kaj aliaj metodoj devos forigi la frazeron el la listo de vortoj "frazo"

#Forigas la difinitan artikolon "la", TODO kie enmeti cxi tion unue?
for i in range(len(ĉeno)):
    artikoloDifinitaForigado(ĉeno)

# for i in range(len(ĉeno)):

#     lastaLitero=ĉeno[i][-1] #Legas la lastan literon de vorto

#     #Jen funkcio por scii ĉu vorto estas substantivo aŭ ne, se jes, konjugacias arkaike
#     if lastaLitero=="o":
#         print(ĉeno[i] + ' estas substantivo') #ĉeno[i] estas vorto, ĉi tio forigotos
        
#         #Konjugacio arkaika
#         vortoAE=substantivoSingulara(ĉeno[i])
#         print(ĉeno[i] + " tradukita al Arkaikam estus: " + vortoAE)
#     else:
#         print(ĉeno[i] + ' ne estas substantivo') #ĉi tio forigotos