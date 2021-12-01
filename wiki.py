"""
Больше всего правок было 28.11.21 и в дни после,
это связано со смертью музыканта.
Все остальные похожи на обычные для википедии исправления.
"""
from datetime import datetime
from urllib.request import urlopen
from json import loads
from itertools import groupby


def get_wiki_revisions_stats(title, page_id):
    url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&' \
          'titles=' + title

    data = loads(urlopen(url).read().decode('utf8'))['query']['pages'][page_id]['revisions']

    groups = groupby(data, lambda x: datetime.strptime(x["timestamp"], "%Y-%m-%dT%H:%M:%SZ").date())

    for key, group in groups:
        yield key, len(list(group))


def main():
    name = '%D0%93%D1%80%D0%B0%D0%B4%D1%81%D0%BA%D0%B8%D0%B9,' \
           '_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80' \
           '_%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BE%D0%B2%D0%B8%D1%87'
    id = "183903"

    for key, count in get_wiki_revisions_stats(name, id):
        print(key, count)


if __name__ == "__main__":
    main()
