import pandas as pd

def alternateCanonical():
    df = pd.read_csv("canonical_tutti.csv")
    df = df[["Indirizzo", "Elemento di link canonical 1"]]
    df.set_index("Indirizzo", inplace = True)
    df["Canonical"] = df["Elemento di link canonical 1"].str.split("?").str[0]
    df["Check"] = df["Elemento di link canonical 1"] == df["Canonical"]
    df.to_csv("checkCanonical.csv")
    #return df

alternateCanonical()