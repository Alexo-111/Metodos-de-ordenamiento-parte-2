"""Ordenamiento QuickSort con menú interactivo."""


def particion(arr, bajo, alto):
    """Partición de Lomuto usando como pivote el elemento central."""
    medio = (bajo + alto) // 2
    arr[medio], arr[alto] = arr[alto], arr[medio]
    pivote = arr[alto]
    i = bajo - 1
    for j in range(bajo, alto):
        if arr[j] <= pivote:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
    return i + 1


def quick_sort(arr, bajo=0, alto=None):
    """Ordena la lista in situ usando QuickSort."""
    if alto is None:
        alto = len(arr) - 1
    if bajo < alto:
        p = particion(arr, bajo, alto)
        quick_sort(arr, bajo, p - 1)
        quick_sort(arr, p + 1, alto)
    return arr


def leer_entero_positivo(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            print("  Ingresa un entero mayor que 0.")
        except ValueError:
            print("  Entrada inválida. Ingresa un número entero.")


def leer_numeros(cantidad):
    numeros = []
    for i in range(cantidad):
        while True:
            try:
                numeros.append(float(input(f"  Número {i + 1}: ")))
                break
            except ValueError:
                print("  Entrada inválida. Intenta de nuevo.")
    return numeros


def formatear(lista):
    return [int(x) if x == int(x) else x for x in lista]


def menu():
    while True:
        print("\n===== QUICKSORT =====")
        print("1. Ordenar números")
        print("2. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            n = leer_entero_positivo("¿Cuántos números deseas ordenar? ")
            numeros = leer_numeros(n)
            print("\nOriginal:", formatear(numeros))
            ordenados = quick_sort(numeros.copy())
            print("Ordenado (QuickSort):", formatear(ordenados))
        elif opcion == "2":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
