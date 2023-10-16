import pandas as pd

class Breadcrumbs:
    def __init__(self):
        self.breadcrumbs = None
        self.brand = None  # Definisci brand come attributo della classe

    def getFile(self):
        self.breadcrumbs = pd.read_csv("estrazione_personalizzata_tutti.csv", usecols=["Indirizzo", "html 1", "text 1"])
        # formatto le colonne in modo da poterle confrontare
        self.breadcrumbs["html 1"] = self.breadcrumbs["html 1"].str.replace("\r\n", " ").str.replace("</span>", " ").str.replace("<span>", " ")
        self.breadcrumbs["text 1"] = self.breadcrumbs["text 1"].str.replace("\n", " ")
        # tolgo eventuali spazi dalle righe
        self.breadcrumbs["html 1"] = self.breadcrumbs["html 1"].str.strip()
        self.breadcrumbs.dropna(inplace=True)
        return self.breadcrumbs

    def getBrand(self):
        self.brand = str(input("Scegli il brand a cui vuoi controllare i Breadcrumbs: "))  # Assegna il valore a brand
        mask = self.breadcrumbs["html 1"].str.contains(self.brand, case=False)
        bread = self.breadcrumbs[mask]
        return bread

f = Breadcrumbs()

f.getFile()
file = f.getBrand()
file.to_csv(f.brand + '.csv', index = False)
