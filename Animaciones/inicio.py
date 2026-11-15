import os
import time

RESET = "\033[0m"
NEGRITA = "\033[1m"
CIAN = "\033[96m"
MAGENTA = "\033[95m"
AMARILLO = "\033[93m"
VERDE = "\033[92m"
GRIS = "\033[90m"

ANCHO = 60  # ancho de la "pantalla" en caracteres

LOGO = [
    r" ____           _                      _      ",
    r"|  _ \ _   _   / \   _ __ ___ __ _  __| | ___ ",
    r"| |_) | | | | / _ \ | '__/ __/ _` |/ _` |/ _ \ ",
    r"|  __/| |_| |/ ___ \| | | (_| (_| | (_| |  __/",
    r"|_|    \__, /_/   \_\_|  \___\__,_|\__,_|\___|",
    r"       |___/                                  ",
]

ANCHO_LOGO = max(len(linea) for linea in LOGO) #identifica la linea mas larga del logo para centrarlo correctamente
LOGO = [linea.ljust(ANCHO_LOGO) for linea in LOGO] # rellena todo el resto de las lineas del logo con espacios para que todas tengan el mismo largo y se pueda centrar correctamente

FOTOGRAMAS_ENCENDIDO = [
    "                             .                              ",
    "                            ---                             ",
    "                        -----------                         ",
    "                ---------------------------                 ",
    "      -----------------------------------------------       ",
    "============================================================",
]


# ---------------------------------------------------------------------------
# Funciones de ayuda
# ---------------------------------------------------------------------------
def limpiar_pantalla():
    #borrar la pantalla de la consola
    print("\033[H\033[J", end="")


def centrar(texto):
    """Devuelve el texto centrado dentro del ancho de la pantalla."""
    return texto.center(ANCHO)


def mostrar_fotograma(lineas, color="", espera=0.1):
    """Dibuja un fotograma completo (lista de líneas) y espera un momento."""
    limpiar_pantalla()
    print("\n" * 4, end="")  # margen superior
    for linea in lineas:
        print(color + centrar(linea) + RESET)
    time.sleep(espera)


# ---------------------------------------------------------------------------
# Escenas de la animación
# ---------------------------------------------------------------------------
def escena_encendido():
    """La pantalla se enciende: un punto que se convierte en una línea."""
    for fotograma in FOTOGRAMAS_ENCENDIDO:
        mostrar_fotograma(["", "", fotograma], GRIS, 0.12)
    time.sleep(0.3)


def escena_logo():
    """El logo aparece de izquierda a derecha, columna por columna."""
    ancho_logo = len(LOGO[0])
    for columna in range(0, ancho_logo + 1, 2):
        # Cada fotograma muestra solo una parte de cada línea del logo
        fotograma = []
        for linea in LOGO:
            fotograma.append(linea[:columna].ljust(ancho_logo))
        mostrar_fotograma(fotograma, CIAN, 0.03)


def escena_destello():
    """El logo cambia de color varias veces, como un destello."""
    colores = [MAGENTA, AMARILLO, VERDE, CIAN]
    for color in colores:
        mostrar_fotograma(LOGO, NEGRITA + color, 0.15)


def escena_subtitulo():
    """Escribe el subtítulo letra por letra debajo del logo."""
    subtitulo = "Consola de juegos clásicos"
    for i in range(len(subtitulo) + 1):
        mostrar_fotograma(LOGO, NEGRITA + CIAN, 0)
        print()
        # Cada fotograma muestra una letra más del subtítulo
        print(AMARILLO + centrar(subtitulo[:i].ljust(len(subtitulo))) + RESET)
        time.sleep(0.05)


def escena_carga():
    """Barra de carga que se llena de 0 % a 100 %."""
    largo_barra = 30
    for porcentaje in range(0, 101, 5):
        llenos = porcentaje * largo_barra // 100
        barra = "█" * llenos + "░" * (largo_barra - llenos)
        mostrar_fotograma(LOGO, NEGRITA + CIAN, 0)
        print()
        print(AMARILLO + centrar("Consola de juegos clásicos") + RESET)
        print()
        print(VERDE + centrar(f"[{barra}] {porcentaje:3d}%") + RESET)
        time.sleep(0.06)
    time.sleep(0.3)


def escena_presiona_enter():
    """El mensaje parpadea unas veces y luego espera el ENTER del jugador."""
    mensaje = ">>> Presiona ENTER para comenzar <<<"
    for i in range(6):
        mostrar_fotograma(LOGO, NEGRITA + CIAN, 0)
        print()
        print(AMARILLO + centrar("Consola de juegos clásicos") + RESET)
        print("\n")
        if i % 2 == 0:  # en los fotogramas pares se ve, en los impares no
            print(NEGRITA + centrar(mensaje) + RESET)
        else:
            print()
        time.sleep(0.4)

    # Último fotograma: el mensaje queda fijo esperando al jugador
    mostrar_fotograma(LOGO, NEGRITA + CIAN, 0)
    print()
    print(AMARILLO + centrar("Consola de juegos clásicos") + RESET)
    print("\n")
    print(NEGRITA + centrar(mensaje) + RESET)
    print(GRIS + centrar("Hecho por Juan y Alison") + RESET)
    input()


# ---------------------------------------------------------------------------
# Función principal
# ---------------------------------------------------------------------------
def animacion_inicio():
    """Ejecuta toda la animación de arranque de PyArcade."""
    os.system("")  # activa los colores ANSI en Windows
    print("\033[?25l", end="")  # oculta el cursor durante la animación
    try:
        escena_encendido()
        escena_logo()
        escena_destello()
        escena_subtitulo()
        escena_carga()
    finally:
        print("\033[?25h", end="")  # vuelve a mostrar el cursor
    escena_presiona_enter()
    limpiar_pantalla()


# Permite probar la animación sola: python animaciones/inicio.py
if __name__ == "__main__":
    animacion_inicio()