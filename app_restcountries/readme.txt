requirements:  
            1. pip install requests,
            2. pip install djangorestframework

database:
        sqlite3


search parameter:
                name. ex: Bangladesh


urls:
    1. api/countries/    -------- will fetch and save the data to database
    2. api/listcountries/ -------- return a list of countries
    3. api/details/Bangladesh   -------Bangladesh as example of country name ---- details of a country
    4. api/createcountry/       -------- create a new entry of a country
    5. api/update/Bangladesh    --------- Update a country
    6. api/delete/Bangladesh   ---------  delete a country
    7. api/borders/Bangladesh     ------   returns neighbours of a country
    8. api/search/Bangladesh         ----  search country by name