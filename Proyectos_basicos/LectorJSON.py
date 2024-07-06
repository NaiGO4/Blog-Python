#Es este un pequeño lector JSOM simple con Python.

import json

#importamos el modudo json para que py lea la informacion que se va a colocar

datos = '''
[

{ 
    "id" : "001",
    "x" : "2",
    "nombre" : "Chuck"
} ,

{ 
    "id" : "009",
    "x" : "7",
    "nombre" : "Brent"
}

]
'''

info = json.loads(datos)
print('Total de usurios: ',len(info))

for elemento in info:
    print('Nombre:', elemento['nombre'])
    print('ID:', elemento['id'])
    print('Atributo', elemento['x'])