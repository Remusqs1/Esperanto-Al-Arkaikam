### La celo de ĉi programeto estas ke uzanto enmetu frazon, ekz: Mi estas frazo,
### kaj la programo redonu tutan tradukon al Arkaikam: Mihi estams Frazom
import tkinter as tk

from funkcioj import *
from vortaroj import specialajVortoj
from iloj import *

def arkaikam():

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

#region agordoj de aplikaĵa fenestro

#Ĉefa fenestro 
fenestro = tk.Tk()
fenestro.title("Tujtradukilo el Esperanto al Arkaika Esperanto")
fenestro.geometry("750x200")
fenestro.resizable(False,False)

# Mesaĝa kadro
kadro = tk.Text(fenestro, width = 84, height = 3)
kadro.place(x=10, y=25)

teksto = tk.Label(fenestro, text = "Enigu vian frazon:")
teksto.place(x=10, y=2)

#Butono
butono = tk.Button(fenestro, text = "Traduki", command = arkaikam)
butono.place(x=330, y=85)

#Rezulta kadro
rezultaKadro = tk.Text(fenestro, state="disabled", width = 84, height = 3)
rezultaKadro.place(x=10, y=135)

traduko = tk.Label(fenestro, text = "Traduko:")
traduko.place(x=10, y=110)
#endregion

#Kopii butonoj

#Origina teksto
butonoKopii = tk.Button(fenestro, text = "Kopii", command =  lambda: kopii(kadro))
butonoKopii.place(x=700, y=25)

#tradukita teksto
butonoTraduko = tk.Button(fenestro, text = "Kopii", command =  lambda: kopii(rezultaKadro))
butonoTraduko.place(x=700, y=135)

fenestro.mainloop()
