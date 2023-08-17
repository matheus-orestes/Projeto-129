import bs4
import time
import pandas as pd

webdriver.start()

scraped_data = []

def scrap():
    bright_star_table = soup.find("table", attrs = ("class", 'wikitable'))

    table_bobody = bright_star_table("tbody")

    table_rows = table_bobody_find_all('tr')

    for row in table_rows:
        table_cows = row.find_all("td")
        print(table_cows)

        temp_list = []

        for col_data in table_cows:
            print(col_data.text)

            data = col_data.text.strip()
            print(data)

            temp_list.append(data)


scraped_data.append(temp_list)



for i in range(0,len(scraped_data)):
    Star_names = scraped_data[i][1]
    Distance = scraped_data[i][3]
    Mass = scraped_data[i][5]
    Radius = scraped_data[i][6]
    Lum =scraped_data[i][7]

    required_data = [Star_names, Distance, Mass, Radius, Lum] 
    stars_data.append(required_data)


    headers = ['Star_name', 'Distance', 'Mass', 'Radius', Luminosity]

    # Defina o cabeçalho

    star_df_1 = pd.DataFrame(stars_data, columns-headers)


required_data.request("brown_dwarf")
required_data.find_all("brown_dwarf")
list = []
required_data.tags("tr_tags")

merge_planets_df = pd.merge(final_planet_df, on="id")

merge_planets_df.shape

merge_planets_df.collum

merge_planets_df.to_csv('merge_planets.csv')

from google.collab import files
files.download('merge_planet.csv')

