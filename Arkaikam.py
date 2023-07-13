### La celo de ĉi programeto estas ke uzanto enmetu frazon, ekz: Mi estas frazo,
### kaj la programo redonu tutan tradukon al Arkaikam: Mihi estams Frazom
import tkinter as tk
from vidInterfaco import krei_gui
from funkcioj import *
from vortaroj import specialajVortoj
from iloj import *

def arkaikam(kadro, rezultaKadro):

    #TODO nuntempe ne uzu interpunkcion
    frazo = kadro.get("1.0",'end-1c').strip().lower()
    frazo = specialajVortoj(frazo)

    #Dividas la vortojn de la frazo laŭ malplena spaco. TODO Poste ĉiu ero estos legita kaj kategoriita laŭ finaĵo.
    ĉeno = dividado(frazo)
    ĉeno = Artikoloj(ĉeno)
    ĉeno = Verboj(ĉeno)
    #Jen funkcio por scii ĉu vorto estas substantivo aŭ ne, se jes, konjugacias arkaike kaj majuskligas
    Substantivo(ĉeno)
    Adjektivo(ĉeno)
    Adverbo(ĉeno)
    Akuzativo(ĉeno)
    AŭAnstataŭado(ĉeno)  # Ŝanĝo de vortoj kiuj finiĝas je -aŭ per -ez
    prefiksigi(ĉeno)  # Prefiksigas vortojn. Nepre ĉi tiu metodo estu unu el la lastaj

    #Ĝi kunigas la frazerojn kaj redonas tradukitan frazon
    frazo = Pronomoj(ĉeno)  # Legas la frazon kaj tradukas la pronomojn
    frazo = kunigado(ĉeno)

    #Montras la rezulton en rezultaKadro
    rezultaKadro.configure(state="normal")
    rezultaKadro.delete(1.0, tk.END)
    rezultaKadro.insert(tk.END, frazo)
    rezultaKadro.configure(state="disabled")

if __name__ == "__main__":
    krei_gui(lambda kadro, rezultaKadro: arkaikam(kadro, rezultaKadro))
