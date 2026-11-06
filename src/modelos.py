from validaciones import validar_nombre, validar_correo, validar_fecha, validar_identificador, validar_identificador_existente, validar_monto
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
        "saldo": 0,
        "nivel": "Bronce"
    }

def solicitar_datos_cliente(clientes):
    identificador = pedir_dato("Ingrese el identificador del cliente: ",
        lambda v: validar_identificador(v, clientes),
    )
    nombre = pedir_dato("Ingrese el nombre del cliente: ", validar_nombre)
    correo = pedir_dato("Ingrese el correo del cliente: ", validar_correo)
    fecha = pedir_dato("Ingrese la fecha de registro (dd-mm-yyyy): ", validar_fecha)
    cliente, datos = crear_clientes(identificador, nombre, correo, fecha)
    return cliente, datos

def consultar_catalogo():
    print("Catálogo de premios:")
    for codigo, premio in catalogo_premios.items():
        print(f"{codigo}: {premio['nombre']} - Puntos necesarios: {premio['puntos_necesarios']}")


def consultar_saldo(clientes):
    identificador = pedir_dato("Ingrese el identificador del cliente: ",
        lambda v: validar_identificador_existente(v, clientes),
    )
    puntos = clientes[identificador]["saldo"]
    nivel = obtener_nivel(puntos)
    print(f"El cliente {clientes[identificador]["nombre"]} es nivel {nivel} y tiene un saldo de {puntos} puntos")

def crear_identificador_compra(compras):
    return f"C-{len(compras) + 1}"

def obtener_nivel(puntos):
    for nivel, datos in reversed(niveles_puntos.items()):
        if puntos >= datos["minimo"]:
            return nivel

def crear_compra(compras, identificador_cliente, fecha, monto, puntos_ganados):
    id_compra = crear_identificador_compra(compras)
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
    fecha = pedir_dato("Ingrese la fecha de la compra (dd-mm-yyyy): ", validar_fecha)
    monto = float(pedir_dato("Ingrese el monto de la compra: ", validar_monto))
    puntos_ganados = calcular_puntos(monto, clientes, identificador)
    nivel = obtener_nivel(clientes[identificador]["puntos"])
    clientes[identificador]["puntos"] += puntos_ganados
    clientes[identificador]["nivel"] = nivel
    clientes[identificador]["saldo"] += puntos_ganados
    id_compra, datos = crear_compra(compras, identificador, fecha, monto, puntos_ganados)
    print(f"Compra registrada exitosamente. ID de la compra: {id_compra}. Nivel del cliente: {nivel}. Puntos ganados: {puntos_ganados}.")
    return id_compra, datos

def canjear_premio(clientes):
    identificador = pedir_dato("Ingrese el identificador del cliente: ",
        lambda v: validar_identificador_existente(v, clientes),
    )
    identificador_premio = pedir_dato("Ingrese el identificador del premio: ",
        lambda v: validar_identificador_existente(v, catalogo_premios),
    )
    while clientes[identificador]["saldo"] < catalogo_premios[identificador_premio]["puntos_necesarios"]:
        print ("No cuenta con suficiente saldo. Por favor, ingrese otro premio")
        identificador_premio = pedir_dato("Ingrese el identificador del premio: ",
        lambda v: validar_identificador_existente(v, catalogo_premios)
    )
    clientes[identificador]["saldo"] - catalogo_premios[identificador_premio]["puntos_necesarios"]
    print(f"Canje realizado exitosamente, disfrute de su {catalogo_premios[identificador_premio]["nombre"]}")