
def datos_alexander():
  print("Mi nombre es Alexander Garrido y tengo 19 años")
def datos_martin():
    print("Mi nombre es Martin Bustamante y tengo 19 años")

def datos_sebastian():
    print("Mi nombre es Sebastian Nuñez y tengo 18 años")



# Menú base del programa
while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Función de integrante 1")
    print("2. Función de integrante 2")
    print("3. Función de integrante 3")
    print("0. Salir ")

    op = input("Selecciona una opcion : ")
    if op == "0":
        print("Programa finalizado.")
        break
    elif op == "1":
        datos_alexander() #funcion integrante 1
    elif op == "2":
        datos_martin() #funcion integrante 2
    elif op == "3":
        datos_sebastian() #funcion integrante 3
    else:
        print("Opcion invalida.")

