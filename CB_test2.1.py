#Bytt strategi och anvant klasser 

import tkinter as tk

mitt_fonster = tk.Tk ()                             # Vanligt ar att skriva root = Tk (). Det har ar huvudapplikationen for fonstret i programmet. 
                                                    # Den har en titel och granser och forses med fonsterhanteraren. Detta måste ske innan 
                                                    # någon annan widget kan skapas. 

mitt_fonster.title("Berakning for cylinder")        # Huvudrubrik for programmet 

class Applikation(tk.Frame):                        # tk.Fram ger klassen mojligheten att anvanda
                                                    # ramverket for tk.Frame alltså rektangulara regioner på skarmen

    def __init__(self, master=None):                # Definerar en metod med __init__ (Denna metod anropas nar ett objekt av klassen skapas)
                                                    # Alla instansmetoder har inledande argument (self) 
                                        

        super().__init__(master)                    # Osaker hor men kan vara onodigt just for mitt behov
                                                    # For att kunna anropa korrekt basklass utan att referera direkt till klassens namn, 
                                                    # har man en speciell metod, super (), som returnerar en referens till basklassen.

        self.master = master                        # Master ar en foraldrar-widget och ar valbar som parameter, default = none

        #self.pack()

        self.skapa_fonster()                        # Gissning - For att kunna skapa widgets i klassen

 

    def skapa_fonster(self):

        # Skapar rubriker som widget

        self.minRubrik1 = tk.Label(mitt_fonster, text="Yttre Diameter (mm):")

        self.minRubrik2 = tk.Label(mitt_fonster, text="Inre Diameter (mm):")

        self.minRubrik3 = tk.Label(mitt_fonster, text="Langd (mm):")

        self.minRubrik4 = tk.Label(mitt_fonster, text="Last (N):")

        self.minRubrik5 = tk.Label(mitt_fonster, text="E-modul kPa:")

        self.minRubrik6 = tk.Label(mitt_fonster, text="Tojning (%):")

        self.minRubrik7 = tk.Label(mitt_fonster, text="Spanning (MPa):")

        self.minRubrik8 = tk.Label(mitt_fonster)
    
        self.minRubrik9 = tk.Label(mitt_fonster)

        

        # Visa den på skramen

        self.minRubrik1.grid(row=1, column=0)

        self.minRubrik2.grid(row=1, column=1)

        self.minRubrik3.grid(row=1, column=2)

        self.minRubrik4.grid(row=1, column=3)

        self.minRubrik5.grid(row=1, column=4)

        self.minRubrik6.grid(row=1, column=5)

        self.minRubrik7.grid(row=1, column=6)


        # Definera rutan

        # Den har delen behovs goras for att kunna få inmatningen från anvandaren till en variabel 
        # --------------------------------
        self.e1 = tk.Entry(mitt_fonster)

        self.d_2 = tk.IntVar()

        self.d_2.set(12)

        self.e1["textvariable"] = self.d_2

        # --------------------------------

        self.e2 = tk.Entry(mitt_fonster)

        self.d_1 = tk.IntVar()

        self.d_1.set(10)

        self.e2["textvariable"] = self.d_1

        self.e3 = tk.Entry(mitt_fonster)

        self.L = tk.IntVar()

        self.L.set(100)

        self.e3["textvariable"] = self.L

        self.e4 = tk.Entry(mitt_fonster)

        self.p = tk.IntVar()

        self.p.set(10000)

        self.e4["textvariable"] = self.p

        self.e5 = tk.Entry(mitt_fonster)

        self.E = tk.DoubleVar()

        self.E.set(210)

        self.e5["textvariable"] = self.E

        # Visa rutan på skarm

        self.e1.grid(row=0, column=0)

        self.e2.grid(row=0, column=1)

        self.e3.grid(row=0, column=2)

        self.e4.grid(row=0, column=3)

        self.e5.grid(row=0, column=4)

        # Knappar - Definition

        self.minKnapp = tk.Button(mitt_fonster, text="Utfor berakning", command=self.berakning)

        self.minKnapp.grid (row = 4, column = 5)       


    def berakning(self):

        d_2 = self.d_2.get()

        d_1 = self.d_1.get()

        L = self.L.get()

        p = self.p.get()

        E = self.E.get()

        # Berakningar
        A = (3.14/4) * ((d_2**2) - (d_1**2))  # mm2
        s = (p/A)  # MPa

        # Deflektion
        delta = (p*L)/(A*(E*10**3))

        # Tojning
        tojning = (delta/L)*100

        self.minRubrik8["text"] = str(tojning)
        self.minRubrik8.grid(row =0,column =5)

        self.minRubrik9["text"] = str(s)
        self.minRubrik9.grid(row =0,column =6)

        

app = Applikation(master=mitt_fonster)
app.mainloop()