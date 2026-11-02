from main import validarIdentificador, validarNombre, validarCorreo, validarFecha, clientes

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
