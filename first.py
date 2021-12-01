import json
import xml.etree.ElementTree as ET
from urllib.request import urlopen


def get_articles_from_lenta(create_item):
    data = urlopen('https://lenta.ru/rss').read().decode('utf8')
    root = ET.fromstring(data)
    articles = []

    for leaf in root[0]:
        if len(leaf) == 8:
            articles.append(create_item(leaf))

    return articles


def save_json(file_name, obj):
    with open(file_name, "w", encoding="utf8") as items:
        json.dump(obj, items, ensure_ascii=False, separators=(",\n", ": "))


def create_news(leaf):
    return {"pubDate": leaf[5].text, "title": leaf[2].text}


save_json("news.json", get_articles_from_lenta(create_news))
