1. Get Status Code: get all pages with status code different to 200. You get a list with all redirect page or 4** error

2. Get noIndex: Get a csv file with all the pages that are not indexable. Check their effective indexing through GSC.

3. Get metatitle: get all metatitle longer than 75 characters

4. Get metadescript: get all metadesciption longer than 135 characters.

5. Get canonical: make sure the first part of the address to be ugual to canonical link.
In the "Check" column you can find two values: True and False.
If True, values match else you will find False.
To make custom export, use this Xpath: //link[@rel='canonical']/@href

6. Get inlinks: don't use this option. It's better to export from bulk export section.

7. get H1 null: URL list with all page without H1 tag

8. Get Response time: The file will list the pages with the response time. They will be ordered from slowest to fastest.

9. Get crawl depht: for each page you have crawl depth. More low will be the crawl depth more faster will have access to the page

10. Alternate page with proper canonical tag: 
    - from GSC, export URL with Alternate page with proper canonical tag.
    - Insert on Screaming Frog the file with "List mode"
    - After crawling, check canonical link to be correct. You can check the same way as in step 5 (canonical)
    
11. Hreflang: checks that each page of the site has its correct hreflang. 
    The final three columns will be filled with True and False. If the value is False it means that the hreflang tag does not match.