import pandas as pd

df = pd.read_csv("hreflang_tutti_prodotti.csv")

def getHreflang():
    global hreflang
    hreflang = df[["Indirizzo","Occorrenze", "HTML hreflang 1 URL", "HTML hreflang 2 URL", "HTML hreflang 3 URL"]]
    #splitto tutte tre le occorrenze in modo da avere solo product/..
    hreflang["Default"] = hreflang["HTML hreflang 1 URL"].str.split("com/").str[1]
    hreflang["ITA"] = hreflang["HTML hreflang 2 URL"].str.split("/it/").str[1]
    hreflang["FRA"] = hreflang["HTML hreflang 3 URL"].str.split("/fr/").str[1]
    hreflang["EN -> IT"] = hreflang["Default"] == hreflang["ITA"]
    hreflang["EN -> FR"] = hreflang["Default"] == hreflang["FRA"]
    hreflang["IT -> FR"] = hreflang["ITA"] == hreflang["FRA"]
    hreflang.to_csv("hreflang_check.csv", index=False)
    return hreflang

getHreflang()