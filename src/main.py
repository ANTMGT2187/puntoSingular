from modelos import registrar_compra, solicitar_datos_cliente, consultar_catalogo, consultar_saldo, canjear_premio, consultar_historial, consultar_nivel
from validaciones import validar_clientes_vacios
def main ():
    clientes = {}
    compras = {}
    print("Seleccione una opción:")
    print("1. Crear cliente")
    print("2. Registrar compra")
    print("3. Consultar catálogo")
    print("4. Consultar saldo")
    print("5. Canjear premios")
    print("6. Consultar historial")
    print("7. Hacer una devolucion")
    print("8. Consultar nivel")
    print("9. Salir")
    while True:
        opcion = input("Ingrese el número de la opción: ")
        match opcion:
            case "1":
                identificador, datos = solicitar_datos_cliente(clientes)
                clientes[identificador] = datos
            case "2":
                validar_clientes_vacios(clientes, main)
                identificador, datos = registrar_compra(clientes, compras)
                compras[identificador] = datos
            case "3":
                consultar_catalogo()
            case "4":
                validar_clientes_vacios(clientes, main)
                consultar_saldo(clientes)
            case "5":
                validar_clientes_vacios(clientes, main)
                canjear_premio(clientes)
            case "6":
                consultar_historial(clientes)
            case "7":
                print("No se ha implementado")
            case "8":
                validar_clientes_vacios(clientes, main)
                consultar_nivel(clientes)
            case "9":
                print("Saliendo...")
                break
            case _:
                print("Opción inválida. Intente nuevamente.")
if __name__ == "__main__":
    main()