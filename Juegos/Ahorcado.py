import random

alimentos = ["manzana", "fresa", "sandia", "melon", "frambuesa", "durazno", "cereza", "aguacate",
             "mandarina", "granadilla", "tomate", "arandano"]
tecnologia = ["programacion","desarrollo", "procesador", "teclado", "monitor",
             "internet", "algoritmo", "variable", "funcion", "condicional", "bucle", ]
objetos = ["computador", "celular", "televisor", "congelador","corrector", "espatula", "estufa",
           "audifonos","impresora","ventilador", "resaltador","esfero"]


print("Bienvenido/a al juego del ahorcado")
print("Seleccione una categoría:")
print("\t1. Alimentos")
print("\t2. Tecnología")
print("\t3. Objetos")

categoria=int(input("Ingrese el número de la categoría que desea elegir: "))


if categoria == 1:
    palabra_Adivinable = random.choice(alimentos) 
elif categoria == 2:
    palabra_Adivinable = random.choice(tecnologia)
elif categoria == 3:
    palabra_Adivinable = random.choice(objetos)
else:
    print("No selecciono una opción válida, vuelva a ingresar: ")
    while categoria != 1 and categoria !=2 and categoria !=3:
        categoria=int(input("Ingrese el número de la categoría que desea elegir: "))

print(palabra_Adivinable)
for i in range(len(palabra_Adivinable)):
    print("_", end= "  ")

errores=0
incompleto=False
letras_correctas=" "


while errores <8:
    letra=(str(input("\nIngrese una letra: ")))
    if letra not in palabra_Adivinable:
        errores+=1
       
    for j in palabra_Adivinable:
        if j==letra:
            print(letra,end="  ")
            
        else:
            incompleto=True
            print("_", end= "  ")

    if errores == 1:
        print("\n__________" \
            "\n|\n|\n|\n|\n|\n" \
            "---------------")
        print("No se encuentra, intente de nuevo")
    elif errores ==2:
        print("\n__________" \
            "\n|     |\n|\n|\n|\n|\n" \
            "---------------")
        print("Intente de nuevo")


