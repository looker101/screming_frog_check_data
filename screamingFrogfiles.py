import pandas as pd
import alternate_canonical

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
        noindex.to_csv("noindex.csv", index = False)
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
        h1.to_csv("h1_miss.csv", index = False)
        #return h1

    # 8) ottengo tutte le pagine scansionate con il relativo tempo di risposta | sotto 2sec è buono!
    def getResponseTime(self):
        response = df[["Indirizzo", "Tempo di risposta"]]
        response = response.sort_values(by = "Tempo di risposta", ascending = False)
        response.to_csv("tempoRisposta.csv", index = False)
        return response

    # 9) ottengo il livello di scansione delle pagine
    def getCrawlDepth(self):
        crawl_depth = df.dropna(subset=["Livello di scansione"])
        crawl_depth = crawl_depth[["Indirizzo", "Livello di scansione"]]
        crawl_depth.to_csv("livello_di_scansione.csv", index = False)
        return crawl_depth

    # 10) ottengo tutti i file
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
        8 - Tempo di Risposta
        9 - Livello di scansione
        10 - Alternate Page with proper canonical tag (Per questa opzione è necessario scaricare il file "canonical_tutti")
        11 - Tutti i files""")
        choice = str(input("Inserisci il numero: "))
        if choice == "1":
            return f.getStatusCode()
        elif choice == "2":
            return f.getNoIndex()
        elif choice == "3":
            return f.getMetaTitle()
        elif choice == "4":
            return f.getMetaDescipt()
        elif choice == "5":
            return f.getCanonical()
        elif choice == "6":
            return f.getInlinks()
        elif choice == "7":
            return f.getH1null()
        elif choice == "8":
            return f.getResponseTime()
        elif choice == "9":
            return f.getCrawlDepth()
        elif choice == "11":
            return f.getFiles()
        elif choice == "10":
            alternate_canonical.alternateCanonical()
        else:
            print("Il valore inserito non è valido!")


df = pd.read_csv("interni_tutti.csv", low_memory=False)
f = ScreamingFrog(df)

f.getResult()