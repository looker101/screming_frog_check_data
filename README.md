1. Get Status Code: otterrai un file csv con tutte la pagine che hanno uno status code diverso da 200. Ovvero tutte pagine che hanno subio un redirect o che hanno un errore di tipo 400 o 500.

2. Get noIndex: ottieni un file csv con tutte le pagine che non sono indicizzabili. Controlla la loro effetttiva indicizzazione tramite GSC.

3. Get metatitle: get all metatitle longer than 75 characters

4. Get metadescript: get all metadesciption longer than 135 characters.

5. Get canonical: controlla che la prima parte dell'indirizzo sia uguale al canonical della pagina stessa. Nella colonna "Check" del file csv avrai "True" in caso i due valori corrispondono, in caso contrario "False".
Per effettuare un'esportazione personalizzata utilizza questo Xpath: //link[@rel='canonical']/@href

6. Get inlinks: don't use this option. It's better to export from bulk export section.

7. get H1 null: URL list with all page without H1 tag

8. Get Response time: The file will list the pages with the response time. They will be ordered from slowest to fastest.

9. Get crawl depht: for each page you have crawl depth. More low will be the crawl depth more faster will have access to the page

10. Alternate page with proper canonical tag: 
    - esporta da GSC l'elenco con le pagine interessate
    - inserisci il file su screaming frog in modalità "list"
    - dopo la scansione, controlla che il tag canonical sia corretto. Puoi controllare nello stesso modo del punto 5 (canonical)

11. Hreflang: controlla che ogni pagina del sito abbia il suo corretto hreflang. 
    Le tre colonne finali saranno riempite con True e False. Se il valore è  False vuol dire che il tag hreflang non corrisponde.