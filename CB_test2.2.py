
import tkinter as tk
import math

# Vanligt är att skriva root = Tk (). Det här är huvudapplikationen för fönstret i programmet.
mitt_fönster = tk.Tk()
# Den har en titel och gränser och förses med fönsterhanteraren. Detta måste ske innan
# någon annan widget kan skapas.

# Huvudrubrik för programmet
mitt_fönster.title("Beräkning för cylinder")
mitt_fönster.geometry("800x800")

# tk.Fram ger klassen möjligheten att använda


class Applikation(tk.Frame):
                                                    # ramverket för tk.Frame alltså rektangulära regioner på skärmen

    # Definerar en metod med __init__ (Denna metod anropas när ett objekt av klassen skapas)
    def __init__(self, master=None):
                                                    # Alla instansmetoder har inledande argument (self)

        # Osäker hör men kan vara onödigt just för mitt behov
        super().__init__(master)
        # För att kunna anropa korrekt basklass utan att referera direkt till klassens namn,
        # har man en speciell metod, super (), som returnerar en referens till basklassen.

        # Master är en föräldrar-wid get och är valbar som parameter, default = none
        self.master = master

        # self.pack()

        # Gissning - För att kunna skapa widgets i klassen
        self.skapa_fönster()

    def skapa_fönster(self):

        # Skapar rubriker som widget
        self.minRubrik1 = tk.Label(mitt_fönster, text="Yttre Diameter (mm):")
        self.minRubrik2 = tk.Label(mitt_fönster, text="Inre Diameter (mm):")
        self.minRubrik3 = tk.Label(mitt_fönster, text="Längd (mm):")
        self.minRubrik4 = tk.Label(mitt_fönster, text="Last (N):")
        self.minRubrik5 = tk.Label(mitt_fönster, text="E-modul kPa:")
        self.minRubrik6 = tk.Label(mitt_fönster, text="Töjning (%):")
        self.minRubrik7 = tk.Label(mitt_fönster, text="Spänning (MPa):")
        self.minRubrik8 = tk.Label(mitt_fönster)
        self.minRubrik9 = tk.Label(mitt_fönster)

        # Visa den på skrämen
        self.minRubrik1.grid(row=0, column=1)
        self.minRubrik2.grid(row=1, column=1)
        self.minRubrik3.grid(row=2, column=1)
        self.minRubrik4.grid(row=3, column=1)
        self.minRubrik5.grid(row=4, column=1)
        self.minRubrik6.grid(row=0, column=5)
        self.minRubrik7.grid(row=0, column=6)

        # Definera rutan
        # Den här delen behövs göras för att kunna få inmatningen från användaren till en variabel
        # --------------------------------
        self.e1 = tk.Entry(mitt_fönster, width=15)
        self.d_2 = tk.IntVar()
        self.d_2.set(12)
        self.e1["textvariable"] = self.d_2

        # --------------------------------
        self.e2 = tk.Entry(mitt_fönster, width=15)
        self.d_1 = tk.IntVar()
        self.d_1.set(10)
        self.e2["textvariable"] = self.d_1

        self.e3 = tk.Entry(mitt_fönster, width=15)
        self.L = tk.IntVar()
        self.L.set(100)
        self.e3["textvariable"] = self.L

        self.e4 = tk.Entry(mitt_fönster, width=15)
        self.p = tk.IntVar()
        self.p.set(10000)
        self.e4["textvariable"] = self.p

        self.e5 = tk.Entry(mitt_fönster, width=15)
        self.E = tk.DoubleVar()
        self.E.set(210)
        self.e5["textvariable"] = self.E

        # Visa rutan på skärm
        self.e1.grid(row=0, column=0)
        self.e2.grid(row=1, column=0)
        self.e3.grid(row=2, column=0)
        self.e4.grid(row=3, column=0)
        self.e5.grid(row=4, column=0)

        # Knappar - Definition
        self.minKnapp = tk.Button(
            mitt_fönster, text="Beräkna", command=self.beräkning)
        self.minKnapp.grid(row=4, column=5)

    def beräkning(self):

        d_2 = self.d_2.get()
        d_1 = self.d_1.get()
        L = self.L.get()
        p = self.p.get()
        E = self.E.get()

        # Beräkningar
        A = (math.pi/4) * ((d_2**2) - (d_1**2))  # mm2
        s = round((p/A), 2)  # MPa

        # Deflektion
        delta = (p*L)/(A*(E*10**3))

        # Töjning
        töjning = round((delta/L)*100, 2)
        self.minRubrik8["text"] = str(töjning)
        self.minRubrik8.grid(row=1, column=5)
        self.minRubrik9["text"] = str(s)
        self.minRubrik9.grid(row=1, column=6)


if __name__ == "__main__":
    app = Applikation(master=mitt_fönster)
    app.mainloop()
