# intenstazione per creare il DF relativo alla sitemap
import pandas as pd

df = pd.read_csv("filname.csv", usecols=[
  "Indirizzo", "Codice di stato", "Indicizzabilità", "Titolo 1", "Lunghezza del titolo 1", "Meta description 1", 
  "Lunghezza della meta description 1", "H1-1", "H2-1", "Elemento di link canonical 1", "Conteggio delle parole", "Conteggio delle frasi", "Leggibilità", 
  "Rapporto di testo", "Livello di scansione", "Link in entrata", "Link in entrata unici", "Link in uscita", 
  "Link in uscita unici", "Tempo di risposta", "Indirizzo URL codificato"
], index_col="Indirizzo")
pd.set_option("display.max_columns", None)
pd.set_option("display.max_colwidth", None)
df.head()
