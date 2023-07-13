import tkinter as tk
from iloj import kopii

def krei_gui(arkaikam_revoko):
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

    def traduki():
        arkaikam_revoko(kadro, rezultaKadro)

    #Butono
    butono = tk.Button(fenestro, text = "Traduki", command = traduki)
    butono.place(x=330, y=85)

    #Rezulta kadro
    rezultaKadro = tk.Text(fenestro, state="disabled", width = 84, height = 3)
    rezultaKadro.place(x=10, y=135)

    traduko = tk.Label(fenestro, text = "Traduko:")
    traduko.place(x=10, y=110)

    #Kopii butonoj

    #Origina teksto
    butonoKopii = tk.Button(fenestro, text = "Kopii", command =  lambda: kopii(kadro))
    butonoKopii.place(x=700, y=25)

    #tradukita teksto
    butonoTraduko = tk.Button(fenestro, text = "Kopii", command =  lambda: kopii(rezultaKadro))
    butonoTraduko.place(x=700, y=135)

    fenestro.mainloop()