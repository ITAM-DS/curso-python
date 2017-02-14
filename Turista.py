# coding: utf-8

from collections import Counter

import numpy as np

import config_ini

import logging
import logging.config
logger = logging.getLogger('turista')

NUM_PARTIDAS=100

class Jugador:
    def __init__(self, nombre, cantidad_inicial):
        self.nombre = nombre
        self.cantidad_inicial = cantidad_inicial
        self.cantidad = cantidad_inicial
        self.turnos = 0
        self.países = []
        self.posicion = 0

    def tirar_dados(self):
        dado = np.arange(1,7)
        dados = np.random.choice(dado, size=2, replace=True)
        self.posicion = (self.posicion + dados.sum()) % 40
        self.turnos += 1
        return self.posicion

    def __repr__(self):
        return "{} está en {} con ${}".format(self.nombre, self.posicion, self.cantidad, self.países)

class País:
    def __init__(self, posicion, nombre, valor, color):
        self.posicion = posicion
        self.nombre = nombre
        self.valor = int(valor)
        self.color = color
        self.dueño = None

    def __repr__(self):
        return "{} [${}] {}".format(self.nombre, self.valor, self.color)

class Turista:
    def __init__(self):
        self.jugadores = [ Jugador(nombre='p'+str(x+1), cantidad_inicial=150000) for x in range(4) ]
        self.tablero = self._cargar_tablero()
        self.contador = Counter()
        self.turnos = 0

    def _cargar_tablero(self):
        tablero = []
        with open('paises.csv', 'r') as países:
            for país in países:
                if not país.startswith('pos'):
                   tablero.append(País(*[x.strip() for x in país.split(',')]))
        return tablero

    def turno(self):
        for jugador in self.jugadores:
            posicion = self.tablero[jugador.tirar_dados()]
            if posicion.color in ['café', 'rosa', 'amarillo', 'azul', 'naranja', 'verde', 'morado', 'rojo']:
                if not posicion.dueño:
                    if jugador.cantidad >= posicion.valor:
                        jugador.países.append(posicion)
                        posicion.dueño = jugador
                        jugador.cantidad -= posicion.valor
                        logger.info("{} COMPRADO por {}".format(posicion.nombre, jugador.nombre))
                else:
                    posicion.dueño.cantidad += posicion.valor
                    jugador.cantidad -= posicion.valor
                    logger.info("{} COBRA RENTA por {} a {}".format(posicion.dueño.nombre, posicion.nombre, jugador.nombre))
            self.contador[posicion] += 1
        self.turnos += 1

    def jugadores_disponibles(self):
        cantidades = np.array([ jugador.cantidad for jugador in self.jugadores ])
        return np.all(cantidades >= 0)

    def partida(self, numero_partida):
        logger.info("{} PARTIDA # {} {}".format("="*10, numero_partida, "="*10))
        while self.jugadores_disponibles():
            self.turno()
            logger.debug(self)

    def __repr__(self):
        return "Turno {}: {}".format(self.turnos,  [jugador for jugador in self.jugadores])


if __name__ == "__main__":
    for num_partida in range(1,NUM_PARTIDAS):
        print("Hola")
        juego = Turista()
        juego.partida(num_partida)
