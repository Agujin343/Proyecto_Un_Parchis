import fichas
import pygame
import variables
from fichas import Ficha, Jugador, jugadores, casillas, cuadricula, recorridos_jugadores
import random

pygame.init()

ventana = pygame.display.set_mode((variables.alto, variables.ancho))
pygame.display.set_caption("Parchís")

orden_turnos = list(jugadores.keys())
turno = 0
run = True
fase_lanzamiento = True
contador_dobles = 0

while run:
    ventana.fill((0, 0, 0))
    cuadricula(ventana, variables.cuadricula_tamano)


    for jugador in jugadores.values():
        for ficha in jugador.fichas:
            ficha.draw(ventana, casillas)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            jugador_actual = jugadores[orden_turnos[turno]]
            recorrido_jugador = recorridos_jugadores[jugador_actual.color]

            if fase_lanzamiento:
                dado1, dado2, suma_dados = jugador_actual.lanzar_dados()
                print(f"{jugador_actual.nombre} sacó {dado1} y {dado2} (Total: {suma_dados})")

                fichas_en_carcel = [ficha for ficha in jugador_actual.fichas if
                                    ficha.casilla == f"casa_{jugador_actual.color}"]
                fichas_fuera = [ficha for ficha in jugador_actual.fichas if ficha.casilla in recorrido_jugador]


                if fichas_en_carcel and (dado1 == 5 or dado2 == 5 or suma_dados == 5):
                    ficha_a_sacar = fichas_en_carcel[0]
                    ficha_a_sacar.mover(0, casillas, jugadores, dado1, dado2, suma_dados)
                    print(f"{jugador_actual.nombre} saca una ficha al tablero")


                if fichas_fuera:
                    fase_lanzamiento = False
                else:
                    if dado1 == dado2:
                        contador_dobles += 1
                        if contador_dobles == 3:
                            print(f"{jugador_actual.nombre} sacó dobles 3 veces seguidas y pierde el turno.")
                            contador_dobles = 0
                            turno = (turno + 1) % len(orden_turnos)
                    else:
                        turno = (turno + 1) % len(orden_turnos)
                        contador_dobles = 0
                    fase_lanzamiento = True

            else:  # Fase de movimiento
                fichas_movibles = [ficha for ficha in jugador_actual.fichas if ficha.casilla in recorrido_jugador]

                if fichas_movibles:
                    ficha_a_mover = fichas_movibles[0]
                    ficha_a_mover.mover(suma_dados, casillas, jugadores, dado1, dado2, suma_dados)
                    print(
                        f"La ficha {ficha_a_mover.numero} de {jugador_actual.color} se movió a {ficha_a_mover.casilla}.")
                else:
                    print(f"{jugador_actual.nombre} no tiene fichas para mover.")


                if dado1 == dado2:
                    contador_dobles += 1
                    if contador_dobles == 3:
                        print(f"{jugador_actual.nombre} sacó dobles 3 veces seguidas y pierde el turno.")
                        contador_dobles = 0
                        turno = (turno + 1) % len(orden_turnos)
                else:
                    turno = (turno + 1) % len(orden_turnos)
                    contador_dobles = 0
                    fase_lanzamiento = True

    pygame.display.update()

pygame.quit()




