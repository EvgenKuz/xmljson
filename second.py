import first


def create_item(leaf):
    item = {}
    for tag in leaf:
        item[tag.tag] = tag.text

    return item


first.save_json("items.json", first.get_articles_from_lenta(create_item))
