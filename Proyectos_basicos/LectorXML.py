#Es este un pequeño lector XML simple.

#Se importa el siemte modulo que py pueda leer los archivos XML

import xml.etree.ElementTree as ET

datos = '''
<persona>
    <nombre>Chuck</nombre>
    <telefono type="intl"> +1 734 303 4456</telefono>
    <email oculto="si" />
</persona>
'''

arbol = ET.fromstring(datos)
print('Nombre:', arbol.find('nombre').text)
print('Telefono:', arbol.find('telefono').text)
print('Atributo:', arbol.find('email').get('oculto'))


