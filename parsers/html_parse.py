from pprint import pprint

from lxml import etree
from requests import get

google = get("https://www.google.com/")
parser = etree.HTMLParser()
tree = etree.HTML(google.text, parser)

# for element in tree.iter("a"):
#     if element.text:
#         print(f"{element.tag} {element.text}")
#         for name, value in element.attrib.items():
#             print(f"attribute {name} = {value}")

print(tree.xpath("//div[div]"))

# /html/body/div[1]/div[1]/div/div/div[1]/div/div/div[1]/div/div[2]/a
# //*[@id="gb"]/div/div[1]/div/div[2]/a