1. Get Status Code: otterrai un file csv con tutte la pagine che hanno uno status code diverso da 200. Ovvero tutte pagine che hanno subito un redirect o che hanno un errore di tipo 400 o 500.

2. Get noIndex: ottieni un file csv con tutte le pagine che non sono indicizzabili. Controlla la loro effettiva indicizzazione tramite GSC.

3. Get metatitle: ottieni umn file csv con tutti i meta title piu lunghi di 75 caratteri.

4. Get metadescript: ottieni un file csv con tutte le metadesciption piu lunghe di 135 caratteri.

5. Get canonical: controlla che la prima parte dell'indirizzo sia uguale al canonical della pagina stessa. Nella colonna "Check" del file csv avrai "True" in caso     i due valori corrispondono, in caso contrario "False".
    Per effettuare un'esportazione personalizzata, puoi utilizzare questo Xpath: //link[@rel='canonical']/@href

6. Get inlinks: Non utilizzare questa opzione. Meglio esportare i link direttamente dell'esportazione di massa

7. get H1 null: nel file ci sarà li lista con tutte le pagine a cui manca il tag H1.

8. Get Response time: nel file saranno elencate le pagine con il tempo di risposta. Saranno ordinate da quella piu lenta a quella piu veloce.

9. Get crawl depht: per ogni pagina avrai il livello di scansione. Piu basso è il livello di scansione, piu velocemente il crawler avrà accesso a quella pagina.

10. Alternate page with proper canonical tag: 
    - esporta da GSC l'elenco con le pagine interessate
    - inserisci il file su screaming frog in modalità "list"
    - dopo la scansione, controlla che il tag canonical sia corretto. Puoi controllare nello stesso modo del punto 5 (canonical)

11. Hreflang: controlla che ogni pagina del sito abbia il suo corretto hreflang. 
    Le tre colonne finali saranno riempite con True e False. Se il valore è  False vuol dire che il tag hreflang non corrisponde.
    Per effettuare un'esportazione personalizzata del tag hreflang puoi utilizzare questo Xpath: (//*[@hreflang])/@hreflang
