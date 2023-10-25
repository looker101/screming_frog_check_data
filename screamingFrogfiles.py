import pandas as pd

class ScreamingFrog:
    def __init__(self, df):
        self.df = df

    # 1) ottengo status code delle pagine
    def getStatusCode(self):
        global status_code 
        mask = df["Codice di stato"] != 200
        status_code = df[mask]
        status_code.to_csv("status_code.csv", index = False)
        #return status_code

    # 2) ottengo le pagine non indicizzabili
    def getNoIndex(self):
        global noindex
        mask = df["Indicizzabilità"] == "Non indicizzabile"
        noindex = df[mask]
        noindex.to_csv("noindex.csv", index = "False")
        #return noindex

    # 3) ottengo i metatitle più lunghi di 75 caratteri
    def getMetaTitle(self):
        global title
        title = df[["Indirizzo", "Titolo 1", "Lunghezza del titolo 1"]]
        title.set_index("Indirizzo")
        mask = title["Lunghezza del titolo 1"] > 75
        meta_title = title[mask].sort_values(by = "Lunghezza del titolo 1", ascending = False)
        meta_title.to_csv("metatitle.csv", index = False)
        #return meta_title

    # 4) ottengo le metadescrizioni più lunghi di 135 caratteri
    def getMetaDescipt(self):
        global descript
        descript = df[["Indirizzo","Meta description 1", "Lunghezza della meta description 1"]]
        mask = descript["Lunghezza della meta description 1"] > 135
        descript = descript[mask].sort_values(by = "Lunghezza della meta description 1", ascending = False)
        descript.to_csv("metadescript.csv", index = False)
        #return descript

    # 5) controllo se i canonical sono corretti
    def getCanonical(self):
        global canonical
        canonical = df[["Indirizzo", "Elemento di link canonical 1"]].dropna()
        canonical["check"] = canonical["Indirizzo"] == canonical["Elemento di link canonical 1"]
        canonical.to_csv("check_canonical.csv", index = False)
        #return canonical

    # 6) controllo il numero di link per ogni pagina
    def getInlinks(self):
        global inlinks
        inlinks = df[["Indirizzo", "Link in entrata", "Link in entrata unici"]]
        inlinks = inlinks.sort_values(by = "Link in entrata", ascending = False)
        inlinks.to_csv("Inlinks.csv", index = False)
        #return inlinks

    # 7) ottengo le pagina a cui manca il tag H1
    def getH1null(self):
        h1 =  df[["Indirizzo", "H1-1"]]
        h1 = h1[h1["H1-1"].isnull()]
        #h1_1.to_csv("h1_miss.csv", index = False)
        #return h1

    # 8) ottengo tutti i file
    def getFiles(self):
        f.getStatusCode()
        f.getNoIndex()
        f.getMetaTitle()
        f.getMetaDescipt()
        f.getCanonical()
        f.getInlinks()
        f.getH1null()

    # chiedo all'utente cosa vuole controllare
    # posso anche fare in modo che vengano salvati tutti i file del programma
    def getResult(self):
        print("""Quale file vuoi salvare?
        1 - Status Code
        2 - No Index Page
        3 - Meta title
        4 - Meta description
        5 - Canonical
        6 - Numero di link x pagina
        7 - H1
        8 - Tutti i files""")
        scelta = str(input("Inserisci il numero: "))
        if scelta == "1":
            return f.getStatusCode()
        elif scelta == "2":
            return f.getNoIndex()
        elif scelta == "3":
            return f.getMetaTitle()
        elif scelta == "4":
            return f.getMetaDescipt()
        elif scelta == "5":
            return f.getCanonical()
        elif scelta == "6":
            return f.getInlinks()
        elif scelta == "7":
            return f.getH1null()
        elif scelta == "8":
            return f.getFiles()

df = pd.read_csv("interni_tutti.csv")
f = ScreamingFrog(df)

f.getResult()