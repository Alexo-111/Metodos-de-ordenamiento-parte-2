"""Ordenamiento ShellSort con menú interactivo."""


def shell_sort(arr):
    """Ordena la lista in situ usando ShellSort (brechas n/2, n/4, ... 1)."""
    n = len(arr)
    brecha = n // 2
    while brecha > 0:
        for i in range(brecha, n):
            temp = arr[i]
            j = i
            while j >= brecha and arr[j - brecha] > temp:
                arr[j] = arr[j - brecha]
                j -= brecha
            arr[j] = temp
        brecha //= 2
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
        print("\n===== SHELLSORT =====")
        print("1. Ordenar números")
        print("2. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            n = leer_entero_positivo("¿Cuántos números deseas ordenar? ")
            numeros = leer_numeros(n)
            print("\nOriginal:", formatear(numeros))
            ordenados = shell_sort(numeros.copy())
            print("Ordenado (ShellSort):", formatear(ordenados))
        elif opcion == "2":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
