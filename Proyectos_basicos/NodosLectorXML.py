#Desplazamiento a través de los nodos

#En este ejemplo menudo el XML tiene múltiples nodos y tenemos que escribir un bucle para  procesarlos todos.

#Seguimos utilizando la libreria ET (xml.etree.ElementTree)

import xml.etree.ElementTree as ET

datos = '''
<cosa>
    <usuarios>
        <usuario x="2">
        <id>001</id>
        <nombre>Chuck</nombre>
    </usuario>
    <usuario x="7">
        <id>009</id>
        <nombre>Brent</nombre>
        </usuario>
    </usuarios>
</cosa>
'''

cosa = ET.fromstring(datos)
lst = cosa.findall('usuarios/usuario')
print('Datos de usuarios:', len(lst))

for item in lst:
    print('Nombre:', item.find('nombre').text)
    print('ID:', item.find('id').text)
    print('Atriburo:', item.get('x'))

#Es importante incluir todos los elementos base en la declaración de ‘findall’ exceptuando aquel que se encuentra en el nivel superior

#Ejemplo si no cuenta findall
print('---------------------')
lst2 = cosa.findall('usuario')
print('Datos de usuarios:', len(lst2))
for item in lst2:
    print('Nombre:', item.find('nombre').text)
    print('ID:', item.find('id').text)
    print('Atriburo:', item.get('x'))

#Si no se declara correctamente como el ejemplo dos no se va a imprimir nada esto