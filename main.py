import re
from datetime import datetime
# Parametros y reglas de calculo
catalogoPremios = {
                    "P01": ["Café de cortesía", 100], 
                    "P02": ["Cupón de descuento 10%", 250],
                    "P03": ["Gift card de 50 u.m", 800],
                    "P04": ["Audífonos inalambricos", 1200],
                    "P05": ["Fin de semana en hotel", 4000]
                }

clientes = {}

def validarIdentificador(identificador):
    if identificador in clientes:
        print("El identificador ya existe. Por favor, ingrese uno diferente.")
        return False
    return True

def validarCorreo(correo):
    patron = r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$'
    if re.match(patron, correo):
        return True
    else:
        print("Correo inválido. Por favor, ingrese un correo válido (formato: ejemplo@dominio.com).")
        return False

def validarNombre(nombre):
    patron = r'^(?=.*[a-zA-Z\s]+$)'
    if re.match(patron, nombre):
        return True
    else:
        print("Nombre inválido. Por favor, ingrese un nombre válido (solo letras y espacios).")
        return False

def validarFecha(fecha):
    try:
        datetime.strptime(fecha, "%d/%m/%Y")
        return True
    except ValueError:
        print("Fecha inválida. Por favor, ingrese una fecha válida (formato: dd/mm/yyyy).")
        return False

def crearClientes():
    identificador = input("Ingrese el identificador del cliente: ")
    while not validarIdentificador(identificador):
        identificador = input("Ingrese el identificador del cliente: ")
    nombre = input("Ingrese el nombre del cliente: ")
    while not validarNombre(nombre):
        nombre = input("Ingrese el nombre del cliente: ")
    correo = input("Ingrese el correo del cliente: ")
    while not validarCorreo(correo):
        correo = input("Ingrese el correo del cliente: ")
    fecha_registro = input("Ingrese la fecha de registro (dd/mm/yyyy): ")
    while not validarFecha(fecha_registro):
        fecha_registro = input("Ingrese la fecha de registro (dd/mm/yyyy): ")
    clientes[identificador] = {"nombre": nombre, "correo": correo, "fecha_registro": fecha_registro, "puntos": 0}
    print (clientes)


x = 0
while x < 3:
    crearClientes()
    x += 1


