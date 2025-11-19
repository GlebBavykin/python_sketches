from pprint import pprint

from lxml import etree as et

root = et.Element("html", version="5.0")

et.SubElement(root, "head")
et.SubElement(root, "title", bgcolor="red", fontsize="22")
et.SubElement(root, "body", fontsize="15")

print(et.tostring(root, pretty_print=True).decode("utf-8"))
print(root.tag)

for element in root:
    print(element.tag)

root.set("newAttribute", "attributeValue")
print(et.tostring(root, pretty_print=True).decode("utf-8"))

print(root.get("newAttribute"))
print(root[1].get("alpha"))
print(root[1].get("bgcolor"))

root.text = "This is an HTML file"
root[0].text = "This is the head of that file"
root[1].text = "This is the title of that file"
root[2].text = "This is the body of that file and would contain paragraphs etc"

# print(et.tostring(root, pretty_print=True).decode("utf-8"))

print(root.getparent())
print(root[1].getnext())
print(root[1].getprevious())

print(root.findtext('title'))
