# Crear una funció que mostri, per consola, 
# i guardi en un arxiu extern, un JSON amb una key de nom book que contindrà titel, cover, year i pages.
# Dintre del JSON hi hauran 4 de cada book (s’ha d’omplir amb values). 

import json

def writejson():
    data = {
                "book":[
                        {
                            "titulo":"Harry Potter and the Chamber of Secrets",
                            "cover":"cover1",
                            "year":"1997",
                            "pages":"200"
                        },
                        {
                            "titulo":"Harry Potter and the Prisoner of Azkaban",
                            "cover":"cover2",
                            "year":"1998",
                            "pages":"200"
                        },
                        {
                            "titulo":"Harry Potter and the Goblet of Fire",
                            "cover":"cover3",
                            "year":"1999",
                            "pages":"200"
                        },
                        {
                            "titulo":"Harry Potter and the Chamber of Secrets",
                            "cover":"cover4",
                            "year":"2000",
                            "pages":"200"
                        }
                        ]
            }
    with open("exercici23.json", "w") as file:
        print(data)
        json.dump(data, file, indent=4)

writejson()