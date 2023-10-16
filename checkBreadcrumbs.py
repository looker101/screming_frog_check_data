import pandas as pd

class Breadcrumbs:
    def __init__(self):
        self.breadcrumbs = None
        
    def getFile(self):
        self.breadcrumbs = pd.read_csv("amq_Balenciaga_bottega.csv", usecols = ["Indirizzo", "Bread_HTML 1", "Bread_TEXT 1"])
        # formatto le colonne in modo da poterle confrontare
        self.breadcrumbs["Bread_HTML 1"] = self.breadcrumbs["Bread_HTML 1"].str.replace("\r\n", " ").str.replace("</span>", " ").str.replace("<span>", " ")
        self.breadcrumbs["Bread_TEXT 1"] = self.breadcrumbs["Bread_TEXT 1"].str.replace("\n", " ")
        # tolgo eventuali spazi dalle righe
        self.breadcrumbs["Bread_HTML 1"] = self.breadcrumbs["Bread_HTML 1"].str.strip()
        self.breadcrumbs.dropna(inplace = True)
        return self.breadcrumbs
    
    def getBrand(self):
        brand = str(input("Scegli il brand a cui vuoi controllare i Breadcrumbs: "))
        mask = self.breadcrumbs["Bread_HTML 1"].str.contains(brand, case = False)
        bread = self.breadcrumbs[mask]
        return bread
                
f = Breadcrumbs()

f.getFile()
print(f.getBrand())