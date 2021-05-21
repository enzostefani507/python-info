def mi_funcion(algo=None):
    try:
        if algo is None:
            raise ValueError("No se permite valor nulo")
    except ValueError:
        print("No se permite valor nulo - desde excepcion")