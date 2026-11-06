import re
from datetime import datetime
def validar_correo(correo):
    patron = r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$'
    if re.match(patron, correo):
        return True
    else:
        print("Correo inválido. Por favor, ingrese un correo válido (formato: ejemplo@dominio.com).")
        return False

def validar_nombre(nombre):
    patron = r'^(?=.*[a-zA-Z\s]+$)'
    if re.match(patron, nombre):
        return True
    else:
        print("Nombre inválido. Por favor, ingrese un nombre válido (solo letras y espacios).")
        return False

def validar_fecha(fecha):
    try:
        datetime.strptime(fecha, "%d-%m-%Y")
        return True
    except ValueError:
        print("Fecha inválida. Por favor, ingrese una fecha válida (formato: dd-mm-yyyy).")
        return False

def validar_identificador(identificador, clientes):
    if identificador in clientes:
        print("El identificador ya existe. Por favor, ingrese uno válido.")
        return False
    return True

def validar_identificador_existente(identificador, clientes):
    if identificador not in clientes:
        print("El identificador no existe. Por favor, ingrese un identificador válido.")
        return False
    return True

def validar_clientes_vacios(clientes, funcion):
    while clientes == {}:
        print("No hay clientes registrados. Por favor, cree un cliente antes de continuar.")
        return funcion()
    return True

def validar_monto(numero):
    valor = float(numero)
    try:
        valor
    except ValueError:
        print("El valor debe ser un número. Por favor, ingrese un valor válido.")
        return False
    if valor <= 0:
        print("El valor no puede ser negativo. Por favor, ingrese un valor válido.")
        return False
    if valor != round(valor, 2):
        print(f"El valor no puede tener más de {2} decimales. Por favor, ingrese un valor válido.")
        return False
    return True
    

