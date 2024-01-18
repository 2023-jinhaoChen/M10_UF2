import xml.etree.ElementTree as ET

def crearXML(filename):
    root = ET.Element("students")
    student1 = ET.SubElement(root, 'student')
    student1.set("altura", "165")
    name = ET.SubElement(student1, "name")
    name.text="Jinhao"
    surname = ET.SubElement(student1, "surname")
    surname.text="Chen"
    email = ET.SubElement(student1, "email")
    email.text="jinhaochen@gmail.com"
    dni = ET.SubElement(student1, "dni")
    dni.text = "12345678X"

    student2 = ET.SubElement(root, 'student')
    student2.set("altura", "170")
    name = ET.SubElement(student2, "name")
    name.text="Pedro"
    surname = ET.SubElement(student2, "surname")
    surname.text="Blanco"
    email = ET.SubElement(student2, "email")
    email.text="pedroblanco@gmail.com"
    dni = ET.SubElement(student2, "dni")
    dni.text = "22345678X"

    student3 = ET.SubElement(root, 'student')
    student3.set("altura", "175")
    name = ET.SubElement(student3, "name")
    name.text="Miquel"
    surname = ET.SubElement(student3, "surname")
    surname.text="Casanova"
    email = ET.SubElement(student3, "email")
    email.text="miquelcasanova@gmail.com"
    dni = ET.SubElement(student3, "dni")
    dni.text = "32345678X"

    student4 = ET.SubElement(root, 'student')
    student4.set("altura", "180")
    name = ET.SubElement(student4, "name")
    name.text="Antonio"
    surname = ET.SubElement(student4, "surname")
    surname.text="Garcia"
    email = ET.SubElement(student4, "email")
    email.text="Antoniogarcia@gmail.com"
    dni = ET.SubElement(student4, "dni")
    dni.text = "42345678X"

    student5 = ET.SubElement(root, 'student')
    student5.set("altura", "160")
    name = ET.SubElement(student5, "name")
    name.text="Joan"
    surname = ET.SubElement(student5, "surname")
    surname.text="Martinez"
    email = ET.SubElement(student5, "email")
    email.text="joanmartinez@gmail.com"
    dni = ET.SubElement(student5, "dni")
    dni.text = "52345678X"

    ET.indent(root)
    ET.dump(root)

    tree = ET.ElementTree(root)
    with open(filename, 'wb') as file:
        tree.write(file)

filename = "./actividad22.xml"
crearXML(filename)

    