import pandas as pd
pd.set_option("display.max_colwidth", None)

class CheckRedirect:
    def __init__(self):
        self.df = None

    def readFile(self):
        self.df = pd.read_csv("interni_tutti.csv", usecols = ["Indirizzo", "URL redirect", "Codice di stato"])
        return self.df

    def getStatusError(self):
        mask = self.df["Codice di stato"] == 301
        _301 = self.df[mask]
        _301.to_csv("301Status.csv", index = False)

redirect_checker = CheckRedirect()

redirect_checker.readFile()
redirect_checker.getStatusError()