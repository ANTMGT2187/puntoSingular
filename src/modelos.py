from validaciones import validar_nombre, validar_correo, validar_fecha, validar_identificador, validar_identificador_existente

catalogo_premios = {
                    "P01": {"nombre": "Café de cortesía", "puntosNecesarios": 100},
                    "P02": {"nombre": "Cupón de descuento 10%", "puntosNecesarios": 250},
                    "P03": {"nombre": "Gift card de 50 u.m", "puntosNecesarios": 800},
                    "P04": {"nombre": "Audífonos inalambricos", "puntosNecesarios": 1200},
                    "P05": {"nombre": "Fin de semana en hotel", "puntosNecesarios": 4000}
                }
niveles_puntos = {
                "Bronce": {"minimo": 0, "maximo": 999, "multiplicador": 1},
                "Plata": {"minimo": 1000, "maximo": 4999, "multiplicador": 1.25},
                "Oro": {"minimo": 5000, "maximo": float('inf'), "multiplicador": 1.5}
            }

#Crear clientes
def calcular_puntos(monto, clientes):
    puntos_actuales = clientes["id_cliente"]["puntos"]
    for nivel, datos in niveles_puntos.items():
        if puntos_actuales >= datos["minimo"]:
            multiplicador = datos["multiplicador"]
            puntos_ganados = (monto/10) * multiplicador
    return puntos_ganados

def pedir_dato(mensaje, validador):
    valor = input(mensaje)
    while not validador(valor):
        valor = input(mensaje)
    return valor

def crear_clientes(identificador, nombre, correo, fecha):
    return identificador, {
        "nombre": nombre,
        "correo": correo,
        "fecha_registro": fecha,
        "puntos": 0,
    }

def solicitar_datos_cliente(clientes):
    identificador = pedir_dato("Ingrese el identificador del cliente: ",
        lambda v: validar_identificador(v, clientes),
    )
    nombre = pedir_dato("Ingrese el nombre del cliente: ", validar_nombre)
    correo = pedir_dato("Ingrese el correo del cliente: ", validar_correo)
    fecha = pedir_dato("Ingrese la fecha de registro (dd/mm/yyyy): ", validar_fecha)
    return crear_clientes(identificador, nombre, correo, fecha)

def registrar_compra(clientes):
    identificador = pedir_dato("Ingrese el identificador del cliente: ", validar_identificador_existente)
    fecha = pedir_dato("Ingrese la fecha de la compra (dd/mm/yyyy): ", validar_fecha)
    monto = float(input("Ingrese el monto de la compra: "))
    puntos_ganados = calcular_puntos(monto, identificador)
    clientes[identificador]["puntos"] += puntos_ganados

