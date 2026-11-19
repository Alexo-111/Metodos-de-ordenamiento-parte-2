"""Ordenamiento HeapSort con menú interactivo."""


def heapify(arr, n, i):
    """Mantiene la propiedad de max-heap en el subárbol con raíz i."""
    mayor = i
    izq = 2 * i + 1
    der = 2 * i + 2

    if izq < n and arr[izq] > arr[mayor]:
        mayor = izq
    if der < n and arr[der] > arr[mayor]:
        mayor = der

    if mayor != i:
        arr[i], arr[mayor] = arr[mayor], arr[i]
        heapify(arr, n, mayor)


def heap_sort(arr):
    """Ordena la lista in situ usando HeapSort."""
    n = len(arr)
    # Construir el max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # Extraer elementos uno por uno
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
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
        print("\n===== HEAPSORT =====")
        print("1. Ordenar números")
        print("2. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            n = leer_entero_positivo("¿Cuántos números deseas ordenar? ")
            numeros = leer_numeros(n)
            print("\nOriginal:", formatear(numeros))
            ordenados = heap_sort(numeros.copy())
            print("Ordenado (HeapSort):", formatear(ordenados))
        elif opcion == "2":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
