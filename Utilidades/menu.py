
juegos = ["adivinar.py", "piedra_papel_tijera.py", "ahorcado.py"]

def imprimir_menu():
    print("Selecciona el juego que deseas jugar:")
    for i, juego in enumerate(juegos, start=1):
        print(f"{i}. {juego}")

def pedir_opcion():
    while True:
        try:
            op = int(input("Ingrese el número del juego que desea jugar: "))
            if 1 <= op <= len(juegos):
                return op
            else:
                print(f"Por favor, ingrese un número entre 1 y {len(juegos)}.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

def menu(juegos):
    imprimir_menu()
    op = pedir_opcion()
    return juegos[op - 1]

menu(juegos)