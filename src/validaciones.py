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



