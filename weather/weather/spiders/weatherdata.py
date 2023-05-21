import json
import scrapy
import pandas as pd
from datetime import datetime, timedelta


class WeatherdataSpider(scrapy.Spider):
    name = "weatherdata"
    allowed_domains = ["videscentrs.lvgmc.lv"]

    # Šie ir "endpointi" kas kalpo kā pilsētu lokācijas
    location_codes = ["P28", "P75", "P52", "P63", "P32", "P77", "P62", "P11", "P13", "P58", "P14", "P25", "P67", "P17",
                      "P54", "P23",
                      "P76", "P31", "P12", "P59", "P38", "P42", "P70", "P51", "P19", "P34", "P5", "P3", "P68", "P44",
                      "P37", "P18",
                      "P24", "P15", "P53", "P1488", "P769", "P313"]

    start_urls = [f"https://videscentrs.lvgmc.lv/data/weather_forecast_for_location_hourly?punkts={code}" for code in
                  location_codes]

    def parse(self, response):
        data = json.loads(response.text)
        df = pd.DataFrame(data)

        # Pārdēvējam kolonnu
        df.rename(columns={"nosaukums": "pilseta"}, inplace=True)

        # Konvertējam to lielo integeri uz datetime
        df["laiks"] = pd.to_datetime(df["laiks"], format="%Y%m%d%H%M")

        now = datetime.now()
        tomorrow = now + timedelta(days=1)

        # Parādīt tikai rītdienas laikapstākļu datus
        df = df[(df["laiks"].dt.date == tomorrow.date())]

        # Sakārtot kolonnas pareizā secībā priekš json
        df = df[["pilseta", "spiediens", "temperatura", "veja_atrums", "veja_virziens", "brazmas", "nokrisni_1h",
                 "relativais_mitrums", "sajutu_temperatura", "sniegs", "makoni", "nokrisnu_varbutiba", "uvi_indekss"]]

        # Saglabājam CSV failu priekš sevis
        df.to_csv("modified.csv", index=False)

        # Saglabājam JSON failu
        df.to_json("dati.json", orient="records", date_format="iso", force_ascii=False)

        for record in df.to_dict('records'):
            yield record


# scrapy crawl weatherdata
