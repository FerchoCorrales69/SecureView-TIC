def verificar_estado_camara(estado):
    """
    Simula la validación del estado de una cámara.
    """
    return estado == "activo"


def test_camara_activa():
    resultado = verificar_estado_camara("activo")

    assert resultado == True
