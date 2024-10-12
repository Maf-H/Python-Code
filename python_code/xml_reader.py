import xml.etree.ElementTree
# parse() function reads xml document builds a tree and returns it.
# getroot() function returns the root element of the tree
cars_for_sale = xml.etree.ElementTree.parse("cars.xml").getroot()
print(cars_for_sale.tag)
for car in cars_for_sale.findall("car"):
    print("\t", car.tag)
    for prop in car:
        print("\t\t", prop.tag, end="")
        if prop.tag == "price":
            print(prop.attrib, end="")
        print(" =", prop.text)
        
# the following code remove's Ford Mustang.
tree = xml.etree.ElementTree.parse("cars.xml")
cars_for_sale = tree.getroot()

    
# The code bellow add's Maserati Mexico
new_car = xml.etree.ElementTree.Element('car')
xml.etree.ElementTree.SubElement(new_car, 'id').text = "4"
xml.etree.ElementTree.SubElement(new_car, 'brand').text = "Maserati"
xml.etree.ElementTree.SubElement(new_car, "model").text = "Mexico"
xml.etree.ElementTree.SubElement(new_car, 'production_year').text = "1970"
xml.etree.ElementTree.SubElement(new_car, "price", {"Currency": "EUR"}).text = "61800"
cars_for_sale.append(new_car)
tree.write('new_car.xml', method='')

cars_for_sale = xml.etree.ElementTree.parse("new_car.xml").getroot()
print(cars_for_sale.tag)
for car in cars_for_sale.findall("car"):
    print("\t", car.tag)
    for prop in car:
        print("\t\t", prop.tag, end="")
        if prop.tag == "price":
            print(prop.attrib, end="")
        print(" =", prop.text) 