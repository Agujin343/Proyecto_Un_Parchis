from turtle import color
import pygame
import variables
import random

def cuadricula(ventana, cuadricula_tamaño):
     celda = variables.cuadricula_tamano // 15
     centro = 4 * celda

     pygame.draw.rect(ventana, "white", (100, 100, variables.cuadricula_tamano, variables.cuadricula_tamano), 4)

     center_x = (variables.cuadricula_tamano - centro) // 2

     pygame.draw.rect(ventana, "white", (320, 320, centro, centro), 3)

     pygame.draw.line(ventana, "white", (100, 270), (700, 270), 2)
     pygame.draw.line(ventana, "white", (100, 356), (320, 356), 2)
     pygame.draw.line(ventana, "white", (100, 452), (320, 452), 2)
     pygame.draw.line(ventana, "white", (100, 530), (700, 530), 2)
     pygame.draw.line(ventana, "white", (530, 270), (700, 270), 2)
     pygame.draw.line(ventana, "white", (480, 356), (700, 356), 2)
     pygame.draw.line(ventana, "white", (480, 452), (700, 452), 2)

     pygame.draw.line(ventana, "white", (356, 100), (356, 320), 2)
     pygame.draw.line(ventana, "white", (452, 100), (452, 320), 2)
     pygame.draw.line(ventana, "white", (530, 100), (530, 700), 2)
     pygame.draw.line(ventana, "white", (270, 100), (270, 700), 2)
     pygame.draw.line(ventana, "white", (356, 480), (356, 700), 2)
     pygame.draw.line(ventana, "white", (452, 480), (452, 700), 2)

     pygame.draw.line(ventana, "white", (270, 270), (530, 530), 3)
     pygame.draw.line(ventana, "white", (270, 530), (530, 270), 3)

     pygame.draw.line(ventana, "white", (124, 270), (124, 530), 3)
     pygame.draw.line(ventana, "white", (148, 270), (148, 530), 3)
     pygame.draw.line(ventana, "white", (172, 270), (172, 530), 3)
     pygame.draw.line(ventana, "white", (196, 270), (196, 530), 3)
     pygame.draw.line(ventana, "white", (220, 270), (220, 530), 3)
     pygame.draw.line(ventana, "white", (244, 270), (244, 530), 3)
     pygame.draw.line(ventana, "white", (270, 270), (270, 530), 3)

     pygame.draw.line(ventana, "white", (554, 270), (554, 530), 3)
     pygame.draw.line(ventana, "white", (578, 270), (578, 530), 3)
     pygame.draw.line(ventana, "white", (602, 270), (602, 530), 3)
     pygame.draw.line(ventana, "white", (626, 270), (626, 530), 3)
     pygame.draw.line(ventana, "white", (650, 270), (650, 530), 3)
     pygame.draw.line(ventana, "white", (674, 270), (674, 530), 3)

     pygame.draw.line(ventana, "white", (270, 124), (530, 124), 3)
     pygame.draw.line(ventana, "white", (270, 148), (530, 148), 3)
     pygame.draw.line(ventana, "white", (270, 172), (530, 172), 3)
     pygame.draw.line(ventana, "white", (270, 196), (530, 196), 3)
     pygame.draw.line(ventana, "white", (270, 220), (530, 220), 3)
     pygame.draw.line(ventana, "white", (270, 244), (530, 244), 3)
     pygame.draw.line(ventana, "white", (270, 554), (530, 554), 3)
     pygame.draw.line(ventana, "white", (270, 578), (530, 578), 3)
     pygame.draw.line(ventana, "white", (270, 602), (530, 602), 3)
     pygame.draw.line(ventana, "white", (270, 626), (530, 626), 3)
     pygame.draw.line(ventana, "white", (270, 650), (530, 650), 3)
     pygame.draw.line(ventana, "white", (270, 674), (530, 674), 3)


     pygame.draw.line(ventana, "white", (530, 530), (530, 700), 2)

casillas = {
     1 : (270,196,86, 24), 18: (196,442, 24, 86), 35: (442,578, 86, 24),52: (578,270, 24, 86),

     2: (270,220, 86, 24), 3: (270,244, 86, 24),
     4:(270, 270, 86, 50), 5:(270, 270, 50, 86),
     6: (244,270, 24, 86), 7: (220, 270, 24, 86), 9: (172,270, 24, 86), 10: (148,270, 24, 86), 11: (124,270, 24, 86),
     12: (100,270, 24, 86), 14: (100,442, 24, 86), 15: (124,442, 24, 86), 16: (148,442, 24, 86), 17: (172,442, 24, 86), 19: (220,442, 24, 86),
     20: (244,442, 24, 86),
     21:(270, 442,50,86), 22:(320, 480, 36,90),
     23: (270,530, 86, 24), 24: (270,554, 86, 24), 26: (270,602, 86, 24), 27: (270,626, 86, 24), 28: (270,650, 86, 24),
     29: (270,674, 86, 24), 31: (442,674, 86, 24), 32: (442,650, 86, 24), 33: (442,626, 86, 24), 34: (442,602, 86, 24), 36: (442,554, 86, 24),
     37: (442,530, 86, 24),
     38:(442, 570, 36, 90), 39:(480,442,90,36),
     40: (570,442, 24, 86), 41: (554, 442, 24, 86), 43: (602,442, 24, 86), 44: (626, 442, 24, 86), 45: (650,448, 24, 86),
     46: (674,442, 24, 86), 48: (674,270, 24, 86), 49: (650,270, 24, 86), 50: (626, 270, 24, 86), 51: (602,270, 24, 86),
     53: (554, 270, 24, 86), 54: (530,270, 24, 86),
     55: (320,480,90,36),
     56: (442,270,86,50),
     57: (442,244, 86, 24), 58: (442,220, 86, 24), 60: (442,172, 86, 24), 61: (442,148, 86, 24), 62: (442,124, 86, 24),
     63: (442,100, 86, 24), 65: (270,100, 86, 24), 66: (270,124, 86, 24), 67: (270,148, 86, 24), 68: (270,172, 86, 24),

    # Casa y zona segura
    "centro": (320, 320, 160,160),
    64: (356,100, 86, 24), 30: (356,674, 86, 24), 47: (674, 356, 24, 86), 13: (100,356, 24, 86),
    8: (196,270, 24, 86), 42: (578,448,24, 86), 59: (442,196, 86, 24), 25: (442,196, 86, 24),
    "casa_rojo": (100,100,270,270),
    "casa_amarillo": (100, 530, 270, 270),
    "casa_azul": (530, 530, 270, 270),
    "casa_verde": (530, 100, 270, 270)
}

recorrido_rojo = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
    14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
    24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
    34, 35, 36, 37, 38, 39, 40, 41, 42, 43,
    44, 45, 46, 47, 48, 49, 50, 51, 52, 53,
    54, 55, 56, 57, 58, 59, 60, 61, 62, 63,
    64, "centro"
]

recorrido_amarillo = [
    18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
    28, 29, 30, 31, 32, 33, 34, 35, 36, 37,
    38, 39, 40, 41, 42, 43, 44, 45, 46, 47,
    48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
    58, 59, 60, 61, 62, 63, 64, 65, 66, 67,
    68, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, "centro"
]

recorrido_azul = [
    35, 36, 37, 38, 39, 40, 41, 42, 43, 44,
    45, 46, 47, 48, 49, 50, 51, 52, 53, 54,
    55, 56, 57, 58, 59, 60, 61, 62, 63, 64,
    65, 66, 67, 68, 1, 2, 3, 4, 5, 6, 7,
    8, 9, 10, 11, 12, 14, 15, 16, 17, 18,
    19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
    29, 30, "centro"
]

recorrido_verde = [
    52, 53, 54, 55, 56, 57, 58, 59, 60, 61,
    62, 63, 64, 65, 66, 67, 68, 1, 2, 3, 4,
    5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16,
    17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
    27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
    37, 38, 39, 40, 41, 42, 43, 44, 45, 46,
    47, "centro"
]


recorridos_jugadores = {
    "rojo": recorrido_rojo,
    "amarillo": recorrido_amarillo,
    "azul": recorrido_azul,
    "verde": recorrido_verde
}



class Ficha:
    def __init__(self, casilla, color, numero, jugador, radius=10):
        self.casilla = casilla
        self.color = color
        self.numero = numero
        self.jugador = jugador
        self.radius = radius
        self.text = str(numero)

    def draw(self, ventana, casillas):
        x, y, ancho, alto = casillas[self.casilla]
        posicion = (x + ancho // 2, y + alto // 2)
        pygame.draw.circle(ventana, self.color, posicion, self.radius)
        font = pygame.font.Font(None, 24)
        text_surface = font.render(self.text, True, "white")
        text_rect = text_surface.get_rect(center=posicion)
        ventana.blit(text_surface, text_rect)

    def mover(self, pasos, casillas, jugadores, dado1, dado2, suma_dados):
        recorrido = recorridos_jugadores[self.jugador]

        # Si la ficha ya está en el centro, no se mueve más
        if self.casilla == "centro":
            print(f"La ficha {self.numero} de {self.jugador} ya está en el centro y no se puede mover.")
            return


        if isinstance(self.casilla, str) and self.casilla.startswith("casa_"):
            if 5 in [dado1, dado2] or suma_dados == 5:
                if self.jugador == "rojo":
                    salida = variables.salida_rojo
                elif self.jugador == "amarillo":
                    salida = variables.salida_amarillo
                elif self.jugador == "azul":
                    salida = variables.salida_azul
                elif self.jugador == "verde":
                    salida = variables.salida_verde
                else:
                    print(f"Error: Jugador {self.jugador} no reconocido.")
                    return

                if salida in recorrido:
                    self.casilla = salida
                    print(f"La ficha {self.numero} de {self.jugador} salió a la casilla {salida}.")
            else:
                print(f"La ficha {self.numero} de {self.jugador} sigue en casa porque no sacó un 5.")
            return


        if self.casilla in recorrido:
            try:
                indice_actual = recorrido.index(self.casilla)
                nueva_posicion = indice_actual + pasos

                if nueva_posicion >= len(recorrido):
                    print(f"La ficha {self.numero} de {self.jugador} llegó a la meta y se queda en el centro.")
                    self.casilla = "centro"
                else:
                    nueva_casilla = recorrido[nueva_posicion]
                    self.casilla = nueva_casilla
                    print(f"La ficha {self.numero} de {self.jugador} se movió a la casilla {nueva_casilla}.")
            except ValueError:
                print(f"Error: La ficha {self.numero} de {self.jugador} tiene una casilla inválida ({self.casilla}).")
        else:
            print(f"Error: La ficha {self.numero} de {self.jugador} no está en un recorrido válido.")

    def comer_ficha(self, nueva_casilla, jugadores):
        for jugador in jugadores:
            if jugador != self.jugador:
                for ficha in jugador.fichas:
                    if ficha.casilla == nueva_casilla:
                        print(f"¡{self.jugador.nombre} ha comido la ficha {ficha.numero} de {jugador.nombre}!")
                        ficha.casilla = f"casa_{jugador.color}"
                        return

    def ha_ganado(self):
        return all(ficha.casilla == "meta" for ficha in self.jugador.fichas)

class Jugador:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
        self.fichas = Ficha


    def lanzar_dados(self):
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        suma_dados = dado1+dado2
        return dado1, dado2, suma_dados

    def seleccionar_ficha(self, indice):
        if 0 <= indice < len(self.fichas):
            return self.fichas[indice]
        return None

    def mover_ficha(self, indice, pasos, casillas, recorrido, jugadores, dado1, dado2, suma_dados):
        ficha = self.seleccionar_ficha(indice)
        if ficha:
            Ficha.mover(pasos, casillas, recorrido, jugadores, dado1, dado2, suma_dados)

jugador_rojo = Jugador("Jugador Rojo", "rojo")
jugador_amarillo = Jugador("Jugador Amarillo", "amarillo")
jugador_azul = Jugador("Jugador Azul", "azul")
jugador_verde = Jugador("Jugador Verde", "verde")

jugador_rojo.fichas = [
        Ficha("casa_rojo", "red", 1, "rojo"),
        Ficha("casa_rojo", "red", 2, "rojo"),
        Ficha("casa_rojo", "red", 3, "rojo"),
        Ficha("casa_rojo", "red", 4, "rojo"),
    ]
jugador_amarillo.fichas = [
        Ficha("casa_amarillo", "yellow", 1, "amarillo"),
        Ficha("casa_amarillo", "yellow", 2, "amarillo"),
        Ficha("casa_amarillo", "yellow", 3, "amarillo"),
        Ficha("casa_amarillo", "yellow", 4, "amarillo"),
    ]
jugador_azul.fichas = [
        Ficha("casa_azul", "blue", 1, "azul",),
        Ficha("casa_azul", "blue", 2, "azul",),
        Ficha("casa_azul", "blue", 3, "azul",),
        Ficha("casa_azul", "blue", 4, "azul",),
    ]
jugador_verde.fichas = [
        Ficha("casa_verde", "green", 1, "verde",),
        Ficha("casa_verde", "green", 2, "verde",),
        Ficha("casa_verde", "green", 3, "verde",),
        Ficha("casa_verde", "green", 4, "verde",),
    ]

jugadores = {
    1: jugador_rojo,
    2: jugador_amarillo,
    3: jugador_azul,
    4: jugador_verde,
}
