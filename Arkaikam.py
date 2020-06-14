### La celo de ĉi programeto estas ke uzanto enmetu frazon, ekz: Mi estas frazo,
### kaj la programo redonu tutan tradukon al Arkaikam: Mihi estams Frazom
from funkcioj import *
from vortaroj import *
from iloj import *

#TODO nuntempe ne uzu interpunkcion
frazo = input("Enigu vian frazon: ").lower()
frazo = specialajVortoj(frazo)

#Dividas la vortojn de la frazo laŭ malplena spaco. TODO Poste ĉiu ero estos legita kaj kategoriita laŭ finaĵo.
ĉeno = dividado(frazo)
ĉeno = ArtikoloDifinitaForigado(ĉeno)
ĉeno = Verboj(ĉeno)
#Jen funkcio por scii ĉu vorto estas substantivo aŭ ne, se jes, konjugacias arkaike kaj majuskligas
Substantivo(ĉeno)
Adjektivo(ĉeno)
Adverbo(ĉeno)
Akuzativo(ĉeno)
AŭAnstataŭado(ĉeno)  # Ŝanĝo de vortoj kiuj finiĝas je -aŭ per -ez
prefiksigi(ĉeno)  # Prefiksigas vortojn. Nepre ĉi tiu metodo estu unu el la lastaj

#Ĝi kunigas la frazerojn kaj redonas tradukitan frazon
frazo = kunigado(ĉeno)
frazo = pronomaVortaro(frazo)  # Legas la frazon kaj tradukas la pronomojn

print(frazo)
