from Animaciones.inicio import animacion_inicio
from Juegos.adivinar import jugarAdivinarNumero
from Utilidades.menu import menu, juegos

animacion_inicio()

juego_seleccionado = menu(juegos)

print(f"Juego seleccionado: {juego_seleccionado}")

from Juegos.juego_seleccionado import jugarAdivinarNumero 