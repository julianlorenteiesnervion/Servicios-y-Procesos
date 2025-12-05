def movil_schema(movil) -> dict:
    return {
        "id": movil.id,
        "precio_coste": movil.precio_coste,
        "precio_venta": movil.precio_venta,
        "id_persona": movil.id_persona
    }

def movil_schema_list(moviles) -> list:
    return [movil_schema(movil) for movil in moviles]