import xml.etree.ElementTree as ET

tree = ET.parse("holders.xml")
root = tree.getroot()
# print(ET.tostring(root))

# get xml attribute
coin = root.get("coin")
# print("Crypto name = {val}".format(val=coin))

# set xml attribute
root.set("lunched", "324234234")
# print(root.attrib)
# Save updated xml
tree.write("holders.xml")

# add id attrib to all inverstors
id = 1
for investor in tree.findall("investor"):
    investor.set("id", str(id))
    id += 1
# save xml
tree.write("holders.xml")

# delete attrib
# for investor in tree.findall("investor"):
# del(investor.attrib["id"])
# save xml
# tree.write("holders.xml")
