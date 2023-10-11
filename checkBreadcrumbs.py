import pandas as pd

# leggo il dataframe e creo una copia
df = pd.read_csv("Oakley_estrazione_personalizzata_tutti.csv", usecols = ["Indirizzo", "Breadcrumbs HTML 1", "Breadcrumbs Text 1"])
breadcrumbs = df.copy()

# formatto le colonne in modo da poterle confrontare
breadcrumbs["Breadcrumbs HTML 1"] = breadcrumbs["Breadcrumbs HTML 1"].str.replace("\r", " ").str.replace("\n", "")
breadcrumbs["Breadcrumbs Text 1"] = breadcrumbs["Breadcrumbs Text 1"].str.replace("\n", " ")

# rendo tutta colonna visualizzabile
#pd.set_option("display.max_colwidth", None)

# tolgo eventuali spazi dalle righe
breadcrumbs["Breadcrumbs HTML 1"] = breadcrumbs["Breadcrumbs HTML 1"].str.strip()

# creo nuova colonna con la parte della stringa che mi serve per il confronto
breadcrumbs["_Link"] = breadcrumbs["Breadcrumbs HTML 1"].str.split("Oakley").str[2]
breadcrumbs["_Text"] = breadcrumbs["Breadcrumbs Text 1"].str.split("Oakley").str[2]
breadcrumbs["_Link"] = breadcrumbs["_Link"].str.replace("</span>", " ") # elimino ulteriori parti di testo che potrebbero contaminare il confronot

# effettuo in confronto
breadcrumbs["checkBreadcrumbs"] = breadcrumbs["_Test"]  == breadcrumbs["_test1"]

