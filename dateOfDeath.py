"""
Больше всего правок было 06.09.21, что совпадает
с датой смерти. Значит предположение, что
большое число правок в статье совпадает с датой
смерти, верно.
"""
from wiki import get_wiki_revisions_stats
from urllib import parse

name = parse.quote("Бельмондо,_Жан-Поль")
id = "192203"

for key, count in get_wiki_revisions_stats(name, id):
    print(key, count)
