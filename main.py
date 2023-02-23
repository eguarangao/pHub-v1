
class Cliente:

    def __init__(self, nodo, distancia=0):
        self.nodo = nodo
        self.distancia_servidor = distancia


class Servidor:

    def __init__(self, nodo):
        self.nodo = nodo
        self.clientes = []


class Nodo:

    def __init__(self, id, x, y, capacidad):
        self.id = id
        self.coordenada_x = x
        self.coordenada_y = y
        self.capacidad = capacidad

