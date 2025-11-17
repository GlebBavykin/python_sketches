exmaple = {
    "glossary": {
        "title": "example glossary",
        "GlossDiv": {
            "title": "S",
            "GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
                    "SortAs": "SGML",
                    "GlossTerm": "Standard Generalized Markup Language",
                    "Acronym": "SGML",
                    "Abbrev": "ISO 8879:1986",
                    "GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
                        "GlossSeeAlso": ["GML", "XML"]
                    },
                    "GlossSee": "markup"
                }
            }
        }
    }
}


def get_all_names(data: dict) -> list:

    name_list = []

    def _get_all_names(data: dict):

        if data is not None:
            if isinstance(data, dict):
                for name, _ in data.items():
                    if name not in name_list:
                        name_list.append(name)
            elif isinstance(data, list):
                for item in data:
                    _get_all_names(item)

        for name in name_list:
            try:
                _get_all_names(data.get(name))
            except AttributeError:
                continue

    _get_all_names(data)

    return name_list


from pprint import pprint

pprint(get_all_names(exmaple))
