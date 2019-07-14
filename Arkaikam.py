### La celo de ĉi programeto estas ke uzanto enmetu frazon, ekz: Mi estas frazo,
### kaj la programo redonu tutan tradukon al Arkaikam: Mihi estams Frazom

from funkcioj import *

frazo=input("Enigu vian frazon: ").lower()

#Dividas la vortojn de la frazo laŭ malplena spaco. TODO Poste ĉiu ero estos legita kaj kategoriita laŭ finaĵo.
ĉeno=frazo.split(" ")

#Jen funkcio por scii ĉu vorto estas substantivo aŭ ne, se jes, konjugacias arkaike
substantivoSingulara(ĉeno)

pronomoj(ĉeno) #Legas la frazeron kaj diras ĉu ĝi estas pronomo
#TODO pronomoj() kaj aliaj metodoj devos anstataŭi la frazeron en la liston de vortoj "frazo"

#Forigas la difinitan artikolon "la", TODO kie enmeti cxi tion unue?
for i in range(len(ĉeno)):
    artikoloDifinitaForigado(ĉeno)
