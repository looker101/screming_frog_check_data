#    🐸 Screaming Frog check data 🐸
## On this repository, after Screaming frog crawling, you can find a few methods to analyze some sections of websites. 

1. Get Status Code: get all pages with status code different to 200. You get a list with all redirect pages or 4** error

2. Get noIndex: Get a csv file with all the pages that are not indexable. Check their effective indexing through GSC.

3. Get metatitle: get all metatitle longer than 75 characters

4. Get metadescript: get all metadesciption longer than 135 characters.

5. Get canonical: make sure the first part of the address is ugual to the canonical link.
In the "Check" column you can find two values: True and False.
If True, values match otherwise, you will find False.
To make a custom export, use this Xpath: //link[@rel='canonical']/@href

6. Get inlinks: don't use this option. It's better to export from the bulk export section.

7. get H1 null: URL list with all page without H1 tag

8. Get Response time: The file will list the pages with the response time. They will be ordered from slowest to fastest.

9. Get crawl depth: for each page, you have crawl depth. Lower will be the crawl depth, faster will have access to the page

10. Alternate page with proper canonical tag: 
    - from GSC, export URL with Alternate page with proper canonical tag.
    - Insert Screaming Frog the file with "List mode"
    - After crawling, check the canonical link to be correct. You can check the same way as in step 5 (canonical)
    
11. Hreflang: checks that each page of the site has its correct Hreflang. 
    The final three columns will be filled with True and False. If the value is False it means that the hreflang tag does not match.
    To make custom export, use this Xpath: (//*[@hreflang])/@hreflang
