import pandas as pd

# setto il file con le colonne che mi servono per effettuare il controllo dei redirect
df = pd.read_csv("interni_tutti.csv", usecols = ["Indirizzo", "URL redirect", "Codice di stato"])
pd.set_option("display.max_columns", None)

# filtro per codice di stato tutte le URL divere da 200 e creo un nuovo df
mask = df["Codice di stato"] != 200
_301 = df[mask]

# creo una colonna con la seconda parte dell'URL della colonna "Indirizzo"
_301["Address1"] = _301["Indirizzo"].str.split().str[1]

# creo un'altra cartella dove toglo https://lookeronline.com/products e https://lookeronline.com/collections dalla colonna dei redirect
_301["redirect_ok"] = _301["URL redirect"].str.replace("https://lookeronline.com/products", " ").str("https://lookeronline.com/collections", " ")

# elimino eventuali spazi dalle colonne che ho appena creato
_301["Check"] = _301["Check"].str.strip()
_301["redirect"] = _301["redirect"].str.strip()

# faccio il confronto tra la colonna "Check" e "redirect"
_301["MIMMO"] = _301["Check"] == _301["redirect"]

# creo e salvo file relativo alle url che hanno confronto False
mask = _301["MIMMO"] == False
falso = _301[mask]

falso.to_csv("redirect_falso.csv", index = False)

# creo e salvo file relativo alle url che hanno confronto True
mask = _301["MIMMO"] == True
vero = _301[mask]

vero.to_csv("redirect_vero.csv", index = False)