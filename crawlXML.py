

import xml.etree.ElementTree as ET

tree = ET.parse('dataXML.xml')
print(str(tree))
root =tree.getroot()
print("haha", root)
for i in tree.find('company'):
    print(i.text)