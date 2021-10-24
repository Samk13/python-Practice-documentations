import xml.etree.ElementTree as ET
from inspect import getmembers, isfunction, isclass

# Display functions in ET module

for (name, value) in getmembers(ET):
    if name.startswith("_"):
        continue
    if isfunction(value):
        print(name, end="\n  |=====|  ", flush=True)
