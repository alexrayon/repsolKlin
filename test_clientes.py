
# Importo la función que quiero probar
from ejercicio_clientes2 import calcular_gasto_medio

# Creo una prueba sencilla
def test_gasto_medio():
    assert calcular_gasto_medio(100, 5) == 20
    assert calcular_gasto_medio(200, 10) == 20
