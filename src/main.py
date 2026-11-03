from modelos import registrar_compra, solicitar_datos_cliente
def main ():
    clientes = {}
    while True:
        print("Seleccione una opción:")
        print("1. Crear cliente")
        print("2. Registrar compra")
        print("3. Salir")
        opcion = input("Ingrese el número de la opción: ")
        match opcion:
            case "1":
                identificador, datos = solicitar_datos_cliente(clientes)
                clientes[identificador] = datos
                print(clientes)
            case "2":
                registrar_compra(clientes)
            case "3":
                break
            case _:
                print("Opción inválida. Intente nuevamente.")
if __name__ == "__main__":
    main()