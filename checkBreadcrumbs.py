import pandas as pd
import os

class Breadcrumbs:
    def __init__(self):
        self.breadcrumbs = None
        self.brand = None  # Definisci brand come attributo della classe

    def getFile(self):
        file_path = os.path.join(r"C:\\Users\\miche\\Desktop\\py\\GitHub\\screming_frog_check_data\\files\\", nome_file + ".csv")
        self.breadcrumbs = pd.read_csv(file_path, usecols=["Indirizzo", "Bread_HTML 1", "Bread_TEXT 1"])
        # formatto le colonne in modo da poterle confrontare
        self.breadcrumbs["Bread_HTML 1"] = self.breadcrumbs["Bread_HTML 1"].str.replace("\r\n", " ").str.replace("</span>", " ").str.replace("<span>", " ")
        self.breadcrumbs["Bread_TEXT 1"] = self.breadcrumbs["Bread_TEXT 1"].str.replace("\n", " ")
        # tolgo eventuali spazi dalle righe
        self.breadcrumbs["Bread_HTML 1"] = self.breadcrumbs["Bread_HTML 1"].str.strip()
        self.breadcrumbs.dropna(inplace=True)
        return self.breadcrumbs

    def getBrand(self):
        self.brand = str(input("Scegli il brand a cui vuoi controllare i Breadcrumbs: "))  # Assegna il valore a brand
        # se non viene inserito niente nell'input otterrò come output tutto il file
        if self.brand in marchi:
            mask = self.breadcrumbs["Bread_TEXT 1"].str.contains(self.brand, case=False)
            bread = self.breadcrumbs[mask]
            return bread
        else:
            raise NameError("Il brand inserito non esiste!")
    
    def getCheck(self):
        file["_link"] = file["Bread_HTML 1"].str.split(">").str[-1].str.strip()
        file["breadcrumb"] = file["Bread_TEXT 1"].str.split(">").str[-1].str.strip()
        file["Check"] = file["_link"] == file["breadcrumb"]
        return file
        
f = Breadcrumbs()

nome_file = str(input("Inserisci il nome del file: "))

# INSERISCI TUTTI I BRAND NELLA LISTA
marchi = [
  "Adidas Originals", "Adidas Sport", "Alexander Mcqueen", "Arnette", "Balenciaga", "Bottega Veneta", "Burberry", "Bvlgari", "Carrera", "Carrera Ducati", 
  "Chiara Ferragni", "Chloe", "David Beckham", "Dolce & Gabbana", "Gucci", "Guess", "Marc Jacobs", "Michael Kors", "Miu Miu", "Moncler", "Oakley", "Off White",
  "Persol", "Polaroid", "Prada", "Prada Linea Rossa", "Ray Ban", "Rudy Project", "Saint Laurent", "Tiffany", "Timberland", "Tom Ford", "Versace", "Vogue" 
 ]

f.getFile()
file = f.getBrand()

f.getCheck()

# ATTIVA QUESTE DUE RIGHE ED ELIMINA LA TERZA
# RIGHE COMMENTATE PER TESTARE IL PROGRAMMA SUL PC DI CASA
directory = r"C:\Users\miche\Desktop\py\GitHub\screming_frog_check_data\ok\\"
file.to_csv(directory + f.brand + '.csv', index = False)
#file.to_csv(f.brand + ".csv", index=False)
