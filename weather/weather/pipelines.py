import pandas as pd
from itemadapter import ItemAdapter

class JsonExportPipeline:
    def open_spider(self, spider):
        self.data = []

    def close_spider(self, spider):
        df = pd.DataFrame(self.data)
        df.to_csv("modified.csv", index=False)
        df.to_json("dati.json", orient="records", date_format="iso", force_ascii=False)

    def process_item(self, item, spider):
        self.data.append(ItemAdapter(item).asdict())
        return item
