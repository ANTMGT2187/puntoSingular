import pytest

from modelos import crear_clientes

FECHA = "05/01/2026"


def test_crear_cliente_y_rechazar_duplicado():
	assert crear_clientes("C001", "Ana Pérez", "ana@correo.com", FECHA) == "Cliente creado"
	assert (
		crear_clientes("C001", "Ana Pérez", "ana@correo.com", FECHA)
		== "Error CLIENTE_DUPLICADO"
	)


@pytest.mark.parametrize(
	("nombre", "correo"),
	[
		("", "luis@correo.com"),
		("Luis Gómez", "luis.correo.com"),
	],
)
def test_rechazar_datos_invalidos(nombre, correo):
	assert crear_clientes("C002", nombre, correo, FECHA) == "Error DATOS_INVALIDOS"




