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
        datos_martin() #funcion integrante 1
    elif op == "2":
        pass #funcion integrante 2
    elif op == "3":
        pass #funcion integrante 3
    else:
        print("Opcion invalida.")

def datos_martin():
    print("Mi nombre es martin y tengo 19 años")
