from validaciones import validar_nombre, validar_correo, validar_fecha, validar_identificador, validar_identificador_existente, validar_monto
from datetime import datetime
import math
catalogo_premios = {
                    "P01": {"nombre": "Café de cortesía", "puntos_necesarios": 100},
                    "P02": {"nombre": "Cupón de descuento 10%", "puntos_necesarios": 250},
                    "P03": {"nombre": "Gift card de 50 u.m", "puntos_necesarios": 800},
                    "P04": {"nombre": "Audífonos inalambricos", "puntos_necesarios": 1200},
                    "P05": {"nombre": "Fin de semana en hotel", "puntos_necesarios": 4000}
                }
niveles_puntos = {
                "Bronce": {"minimo": 0, "multiplicador": 1},
                "Plata": {"minimo": 1000, "multiplicador": 1.25},
                "Oro": {"minimo": 5000, "multiplicador": 1.5}
            }

#Crear clientes
def calcular_puntos(monto, clientes, identificador):
    puntos_actuales = clientes[identificador]["puntos"]
    for nivel, datos in niveles_puntos.items():
        if puntos_actuales >= datos["minimo"]:
            multiplicador = datos["multiplicador"]
            puntos_ganados = math.floor((monto/10) * multiplicador)
    return puntos_ganados

def pedir_dato(mensaje, validador):
    valor = input(mensaje)
    while not validador(valor):
        valor = input(mensaje)
    return valor

# Metodos para crear clientes
def crear_clientes(identificador, nombre, correo, fecha):
    return identificador, {
        "nombre": nombre,
        "correo": correo,
        "fecha_registro": fecha,
        "puntos": 0,
        "saldo": 0,
        "nivel": "Bronce",
        "historial": []
    }

def solicitar_datos_cliente(clientes):
    identificador = pedir_dato("Ingrese el identificador del cliente: ",
        lambda v: validar_identificador(v, clientes),
    )
    nombre = pedir_dato("Ingrese el nombre del cliente: ", validar_nombre)
    correo = pedir_dato("Ingrese el correo del cliente: ", validar_correo)
    fecha = pedir_dato("Ingrese la fecha de registro (dd-mm-yyyy): ", validar_fecha)
    cliente, datos = crear_clientes(identificador, nombre, correo, fecha)
    print (f"Cliente {nombre} creado satisfactoriamente")
    return cliente, datos

def consultar_catalogo():
    print("Catálogo de premios:")
    for codigo, premio in catalogo_premios.items():
        print(f"{codigo}: {premio['nombre']} - Puntos necesarios: {premio['puntos_necesarios']}")

def consultar_nivel(clientes):
    identificador = pedir_dato("Ingrese el identificador del cliente: ",
        lambda v: validar_identificador_existente(v, clientes),
    )
    puntos = clientes[identificador]["puntos"]
    nivel = obtener_nivel(puntos)
    print(f"El cliente {clientes[identificador]["nombre"]} es nivel {nivel} y tiene un saldo de {puntos} puntos acumulados")
    for nombre, datos in niveles_puntos.items():
        if puntos < datos["minimo"]:
            print(f"Le faltan {datos['minimo'] - puntos} puntos para el nivel {nombre}")
            break
    else:
        print("Ya está en el nivel máximo")

def consultar_saldo(clientes):
    identificador = pedir_dato("Ingrese el identificador del cliente: ",
        lambda v: validar_identificador_existente(v, clientes),
    )
    puntos = clientes[identificador]["saldo"]
    print(f"El cliente {clientes[identificador]["nombre"]} tiene un saldo de {puntos} puntos ")

def crear_identificador_compra(compras):
    return f"C-{len(compras) + 1}"

def obtener_nivel(puntos):
    for nivel, datos in reversed(niveles_puntos.items()):
        if puntos >= datos["minimo"]:
            return nivel

def crear_movimiento(tipo, puntos, fecha, referencia):
    return {
        "tipo": tipo,              
        "puntos": puntos,          
        "fecha": fecha,            
        "referencia": referencia 
    }

def registrar_movimiento(clientes, identificador, tipo, puntos, fecha, referencia):
    movimiento = crear_movimiento(tipo, puntos, fecha, referencia)
    clientes[identificador].setdefault("historial", []).append(movimiento)

def obtener_historial(clientes, identificador):
    historial = clientes[identificador].get("historial", [])
    ordenado = sorted(historial, key=lambda m: datetime.strptime(m["fecha"], "%d-%m-%Y"))
    return [dict(m) for m in ordenado]

def consultar_historial(clientes):
    identificador = pedir_dato("Ingrese el identificador del cliente: ",
        lambda v: validar_identificador_existente(v, clientes),
    )
    historial = obtener_historial(clientes, identificador)
    if not historial:
        print(f"El cliente {clientes[identificador]['nombre']} no tiene movimientos.")
        return historial
    print(f"Historial de {clientes[identificador]['nombre']}:")
    for m in historial:
        print(f"{m['fecha']} | {m['tipo']:<11} | {m['puntos']:+} puntos | Ref: {m['referencia']}")
    return historial

def crear_compra(id_compra, identificador_cliente, fecha, monto, puntos_ganados):
    return id_compra, {
        "id_cliente": identificador_cliente,
        "fecha": fecha,
        "monto": monto,
        "puntos_ganados": puntos_ganados
    }
def registrar_compra(clientes, compras):
    identificador = pedir_dato("Ingrese el identificador del cliente: ",
        lambda v: validar_identificador_existente(v, clientes),
    )
    id_compra = crear_identificador_compra(compras)
    fecha = pedir_dato("Ingrese la fecha de la compra (dd-mm-yyyy): ", validar_fecha)
    monto = float(pedir_dato("Ingrese el monto de la compra: ", validar_monto))
    puntos_ganados = calcular_puntos(monto, clientes, identificador)
    nivel = obtener_nivel(clientes[identificador]["puntos"])
    clientes[identificador]["puntos"] += puntos_ganados
    clientes[identificador]["nivel"] = nivel
    clientes[identificador]["saldo"] += puntos_ganados
    id_compra, datos = crear_compra(id_compra, identificador, fecha, monto, puntos_ganados)
    registrar_movimiento(clientes, identificador, "ACUMULACION", +puntos_ganados, fecha, id_compra)
    print(f"Compra registrada exitosamente. ID de la compra: {id_compra}. Nivel del cliente: {nivel} (multiplicador x{niveles_puntos[nivel]["multiplicador"]}). Puntos ganados: {puntos_ganados}.")
    return id_compra, datos


def canjear_premio(clientes):
    identificador = pedir_dato("Ingrese el identificador del cliente: ",
        lambda v: validar_identificador_existente(v, clientes),
    )
    identificador_premio = pedir_dato("Ingrese el identificador del premio: ",
        lambda v: validar_identificador_existente(v, catalogo_premios),
    )
    if clientes[identificador]["saldo"] < catalogo_premios[identificador_premio]["puntos_necesarios"]:
        print ("No cuenta con suficiente saldo. Por favor, vuelva a inmtentar")
        return
    fecha = pedir_dato("Ingrese la fecha de la compra (dd-mm-yyyy): ", validar_fecha)
    puntos = catalogo_premios[identificador_premio]["puntos_necesarios"]
    clientes[identificador]["saldo"] -= puntos
    registrar_movimiento(clientes, identificador, "CANJE", -puntos, fecha, identificador_premio)
    print(f"Canje realizado exitosamente, disfrute de su {catalogo_premios[identificador_premio]["nombre"]}")