import random
import os
import time

RESET = "\033[0m"
NEGRITA = "\033[1m"
CIAN = "\033[96m"
AMARILLO = "\033[93m"
VERDE = "\033[92m"
ROJO = "\033[91m"
GRIS = "\033[90m"

#digitos grandes para mostrar el número del intento
DIGITOS = {
    "0": ["█████", "█   █", "█   █", "█   █", "█████"],
    "1": ["  █  ", " ██  ", "  █  ", "  █  ", " ███ "],
    "2": ["█████", "    █", "█████", "█    ", "█████"],
    "3": ["█████", "    █", "█████", "    █", "█████"],
    "4": ["█   █", "█   █", "█████", "    █", "    █"],
    "5": ["█████", "█    ", "█████", "    █", "█████"],
    "6": ["█████", "█    ", "█████", "█   █", "█████"],
    "7": ["█████", "    █", "   █ ", "  █  ", "  █  "],
    "8": ["█████", "█   █", "█████", "█   █", "█████"],
    "9": ["█████", "█   █", "█████", "    █", "█████"],
}

#flechas y simbolos
FLECHA_ARRIBA = ["   █   ", "  ███  ", " █████ ", "  ███  ", "  ███  "]
FLECHA_ABAJO = ["  ███  ", "  ███  ", " █████ ", "  ███  ", "   █   "]
CHULO = ["      █", "     █ ", "█   █  ", " █ █   ", "  █    "]
VACIO = ["       "] * 5


def limpiarPantalla():
    print("\033[H\033[J", end="")

# crea un numero apartir de sus dijitos para poder mostrarlo en grande
def numeroGrande(numero):
    lineas = ["", "", "", "", ""]
    for digito in str(numero):
        for i in range(5):
            lineas[i] += DIGITOS[digito][i] + "  "  # 2 espacios entre dígitos
    return lineas

#para las animaciones solo mueve de arriba a abajo
def moverVertical(figura, desplazamiento):
    relleno = "       "
    # si es -1 desplaza hacia arriba, si es 1 desplaza hacia abajo, si es 0 no desplaza y se le coloca el releno arriba y abajo
    lienzo = [relleno] * (1 + desplazamiento) + figura + [relleno] * (1 - desplazamiento)
    return lienzo


def dibujarPantalla(intento, figura, colorFigura, mensaje, intentos, minimo, maximo):
    limpiarPantalla()
    numero = numeroGrande(intento)
    numero = [""] + numero + [""]  # mismo alto que la figura (7 líneas)

    print(NEGRITA + CIAN + "  ╔══════════════════════════════════╗")
    print("  ║    ADIVINA EL NÚMERO (1-100)     ║")
    print("  ╚══════════════════════════════════╝" + RESET)
    print()
    for i in range(7): #numero[i].ljust(16) alinia el numero a la izquierda y le da un ancho de 16 caracteres el resto es la figura
        print("    " + NEGRITA + numero[i].ljust(16) + RESET + "   " + colorFigura + figura[i] + RESET)
    print()
    print("  " + NEGRITA + colorFigura + mensaje + RESET)
    print()
    print(GRIS + f"  Intentos: {intentos}   |   Está entre {minimo} y {maximo}" + RESET)
    print()

#una pequeña animacion para mostrar el resultado del intento, si es mayor o menor que el numero secreto
def animarResultado(intento, numeroSecreto, intentos, minimo, maximo):
    if intento < numeroSecreto:
        flecha = FLECHA_ARRIBA
        color = AMARILLO
        mensaje = "▲ El número secreto es MAYOR"
        movimiento = [0, -1, 0, -1, 0]  # la flecha "salta" hacia arriba
    elif intento > numeroSecreto:
        flecha = FLECHA_ABAJO
        color = ROJO
        mensaje = "▼ El número secreto es MENOR"
        movimiento = [0, 1, 0, 1, 0]  # la flecha "cae" hacia abajo
    else:
        flecha = CHULO
        color = VERDE
        mensaje = f"¡Felicidades! Lo adivinaste en {intentos} intentos."
        movimiento = [0, 0, 0, 0, 0] # no se mueve la flecha si acierta

    # Fotograma por fotograma: la flecha se mueve
    for desplazamiento in movimiento:
        dibujarPantalla(intento, moverVertical(flecha, desplazamiento), color,
                        mensaje, intentos, minimo, maximo)
        time.sleep(0.15)

    # Si ganó, el chulo parpadea
    if intento == numeroSecreto:
        for i in range(6):
            if i % 2 == 0:
                figura = moverVertical(VACIO, 0)
            else:
                figura = moverVertical(CHULO, 0)
            dibujarPantalla(intento, figura, color, mensaje, intentos, minimo, maximo)
            time.sleep(0.2)


def generarNumeroAleatorio():
    return random.randint(1, 100)

#validacion
def pedirNumero():
    while True:
        try:
            intento = int(input(CIAN + "  Introduce tu intento: " + RESET))
            if 1 <= intento <= 100:
                return intento
            print(ROJO + "  El número debe estar entre 1 y 100." + RESET)
        except ValueError:
            print(ROJO + "  Por favor, introduce un número válido." + RESET)


def jugarAdivinarNumero():
    os.system("")  # activa los colores en Windows
    numeroSecreto = generarNumeroAleatorio()
    intentos = 0
    minimo = 1
    maximo = 100

    limpiarPantalla()
    print(NEGRITA + CIAN + "  ¡Bienvenido al juego de adivinar el número!" + RESET)
    print("  Estoy pensando en un número entre 1 y 100.\n")

    while True:
        intento = pedirNumero()
        intentos += 1

        # Actualizamos el rango donde puede estar el número
        if intento < numeroSecreto and intento >= minimo:
            minimo = intento + 1
        elif intento > numeroSecreto and intento <= maximo:
            maximo = intento - 1

        animarResultado(intento, numeroSecreto, intentos, minimo, maximo)

        if intento == numeroSecreto:
            input(GRIS + "  Presiona ENTER para volver al menú..." + RESET)
            break


if __name__ == "__main__":
    jugarAdivinarNumero()