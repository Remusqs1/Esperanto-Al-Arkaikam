### La celo de ĉi programeto estas ke uzanto enmetu frazon, ekz: Mi estas frazo,
### kaj la programo redonu tutan tradukon al Arkaikam: Mihi estams Frazom

from funkcioj import *

frazo=input("Enigu vian frazon: ").lower()

#Dividas la vortojn de la frazo laŭ malplena spaco. TODO Poste ĉiu ero estos legita kaj kategoriita laŭ finaĵo.
ĉeno=frazo.split(" ")

#Jen funkcio por scii ĉu vorto estas substantivo aŭ ne, se jes, konjugacias arkaike
substantivoSingulara(ĉeno)
substantivoPlurala(ĉeno) #ĉu vorto estas substantivo kaj plurala
akuzativoPlurala(ĉeno) #ĉu vorto estas substantivo azukativa singulara aŭ plurala
AŭŜanĝo(ĉeno) #Ŝanĝo de vortoj kiuj finiĝas je -aŭ per -ez

pronomoj(ĉeno) #Legas la frazeron kaj diras ĉu ĝi estas pronomo
#TODO pronomoj() kaj aliaj metodoj devos anstataŭi la frazeron en la liston de vortoj "frazo"

#Forigas la difinitan artikolon "la", TODO kie enmeti cxi tion unue?
artikoloDifinitaForigado(ĉeno)

#Ĉi tiu funkcio nepre devas esti la lasta. Ĝi kunigas la frazerojn kaj redonas tradukitan frazon
kunigado(ĉeno)
