# Programa de lealtad por puntos

Aplicación de consola en Python para gestionar un programa de lealtad: registro de clientes, compras que acumulan puntos según el nivel del cliente (Bronce, Plata y Oro), catálogo de premios, canje de puntos e historial de movimientos.

## Instalación y ejecución

El proyecto no tiene dependencias externas: usa solo la biblioteca estándar de Python, así que no hay nada que instalar.

**Requisito:** Python 3.14 (versión con la que se probó).

```bash
python3 main.py
```

En Windows puede ser `python main.py`. El programa se maneja desde el menú que aparece en la consola.

## Niveles completados

- **Nivel 1:** completado.
- **Nivel 2:** completado.
- **Nivel 3:** no implementado.

## Modelo de datos

Todo el estado vive en diccionarios de Python, cargados en memoria mientras el programa se ejecuta:

- **`clientes`:** un diccionario con el identificador del cliente como clave. Cada cliente guarda su nombre, correo, fecha de registro, puntos acumulados, saldo, nivel y su `historial` (una lista de movimientos).
- **`compras`:** un diccionario con el identificador de la compra como clave (`C-1`, `C-2`, ...). Cada compra guarda el cliente, la fecha, el monto y los puntos ganados.
- **Movimientos:** cada elemento del historial de un cliente tiene `tipo` (`ACUMULACION` o `CANJE`), `puntos`, `fecha` y `referencia` (el id de la compra o del premio). Se guardan en el orden en que ocurren.
- **`catalogo_premios` y `niveles_puntos`:** diccionarios de configuración con los premios, sus puntos necesarios, y el mínimo de puntos y el multiplicador de cada nivel.

```python
clientes = {
    "U1": {
        "nombre": "Ana", "correo": "ana@correo.com", "fecha_registro": "01-01-2025",
        "puntos": 1500.0, "saldo": 700.0, "nivel": "Plata",
        "historial": [
            {"tipo": "ACUMULACION", "puntos": 1000.0, "fecha": "01-02-2025", "referencia": "C-1"},
            {"tipo": "CANJE", "puntos": -800, "fecha": "10-02-2025", "referencia": "P03"},
        ],
    }
}
```

**Por qué diccionarios:** son una forma sencilla de mantener los datos ordenados al estilo de una base de datos (cada registro se busca por su identificador), sin necesidad de una base real, solo cargando los datos en memoria. La consecuencia es que los datos no persisten: se pierden al cerrar el programa.

Los **puntos acumulados** determinan el nivel del cliente; el **saldo** es lo que tiene disponible para canjear.

## Limitaciones conocidas y mejoras

- **Validación de fechas:** no se valida que la fecha de una operación no sea anterior a las operaciones previas del cliente.
- **Organización del código:** el archivo con la lógica creció más de lo esperado. Con más tiempo separaría las funciones en más módulos (por ejemplo clientes, compras, canjes e historial).
- **Pruebas automáticas:** no se pudieron aplicar. Con más tiempo las agregaría para verificar las reglas de puntos, niveles y canjes.

## Herramientas de apoyo

Se usaron **Claude** y **GitHub Copilot** como apoyo durante el desarrollo.
