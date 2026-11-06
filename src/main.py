from modelos import registrar_compra, solicitar_datos_cliente, consultar_catalogo, consultar_saldo
from validaciones import validar_clientes_vacios
def main ():
    clientes = {}
    compras = {}
    clientes.update({
        "1": {
            "nombre": "Juan Pérez",
            "correo": "juan.perez@example.com",
            "fecha_registro": "01-01-2023",
            "puntos": 0,
            "saldo": 0,
            "nivel": "Bronce"
        }
    })
    while True:
        print("Seleccione una opción:")
        print("1. Crear cliente")
        print("2. Registrar compra")
        print("3. Consultar catálogo")
        print("4. Consultar saldo")
        print("5. Salir")
        opcion = input("Ingrese el número de la opción: ")
        match opcion:
            case "1":
                identificador, datos = solicitar_datos_cliente(clientes)
                clientes[identificador] = datos
                print(clientes)
            case "2":
                validar_clientes_vacios(clientes, main)
                identificador, datos = registrar_compra(clientes, compras)
                compras[identificador] = datos
            case "3":
                consultar_catalogo()
            case "4":
                validar_clientes_vacios(clientes, main)
                consultar_saldo(clientes)
            case _:
                print(compras)
                print("Opción inválida. Intente nuevamente.")
if __name__ == "__main__":
    main()