mi_diccionario = {}
import os
sw = True

def fnt_agregar(diccionario, id_persona, nombre, apellido, contacto, correo, edad, estrato, sexo, telefono, direccion):
    if id_persona == '' or nombre == '' or apellido == '' or contacto == '' or correo == '' or edad == '' or estrato == '' or sexo == '' or telefono == '' or direccion == '':
        enter = input('Debe diligenciar toda la información solicitada <ENTER>')
    else:
        diccionario[id_persona] = {'nombre': nombre, 'apellido': apellido, 'contacto': contacto, 'correo': correo, 'edad': edad, 'estrato': estrato,'sexo': sexo, 'telefono': telefono, 'direccion': direccion}
        enter = input(f'\nLa persona {nombre} ha sido registrada con éxito <ENTER>')

def fnt_selector(op):
    if op == '1':
        os.system('cls')
        id_persona = input('ID:  ')
        nombre = input('Nombre:  ')
        apellido = input('Apellido:  ')
        contacto = input('Contacto:  ')
        correo = input('Correo:  ')
        edad = input('Edad:  ')
        estrato = input('Estrato:  ')
        sexo = input('Sexo:  ')
        telefono = input('Telefono:  ')
        direccion = input('Direccion:  ')
        fnt_agregar(mi_diccionario, id_persona, nombre, apellido, contacto, correo, edad, estrato, sexo, telefono, direccion)

while sw == True:
    os.system('cls')
    opcion = input('1. Registrar\n2. Mostrar\n3. Salir\n- >  ')
    if opcion == '1':
        fnt_selector(opcion)
    elif opcion == '2':
        os.system('cls')
        print('\nCantidad de registros: ',len(mi_diccionario),'\n')
        for clave, valor in mi_diccionario.items():
            print(f"{clave}: {valor}")
        enter = input('\n\nPresione ENTER para continuar...')
    elif opcion == '3':
        sw = False