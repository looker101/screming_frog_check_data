import pandas as pd

def getHreflang():
    global file
    df = pd.read_csv("hreflang_tutti.csv", usecols = ["Indirizzo","Occorrenze", "HTML hreflang 1 URL", "HTML hreflang 2 URL", "HTML hreflang 3 URL"] ,low_memory = False)
    df["Default"] = df["HTML hreflang 1 URL"].str.split("com/").str[1] #creo la colonna relativa all'inglese mantenendo la seconda parte dell'url (dopo "/com" in poi)
    df["ITA"] = df["HTML hreflang 2 URL"].str.split("/it/").str[1] #creo la colonna relativa all'italiano mantenendo la seconda parte dell'url (dopo "/it/" in poi)
    df["FRA"] = df["HTML hreflang 3 URL"].str.split("/fr/").str[1] #creo la colonna relativa al francese mantenendo la seconda parte dell'url (dopo "/fr/" in poi)
    df["EN -> IT"] = df["Default"] == df["ITA"] #confronto en con it
    df["EN -> FR"] = df["Default"] == df["FRA"] #confronto en con fr 
    df["IT -> FR"] = df["ITA"] == df["FRA"] #confronta it con fr
    df.to_csv("hreflang_check.csv", index = False)
    #return df.head(2)

#getHreflang()