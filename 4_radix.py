"""Ordenamiento Radix Sort (LSD, base 10) con menú interactivo.
Soporta números enteros positivos y negativos."""


def counting_sort_por_digito(arr, exp):
    """Ordenamiento estable por el dígito indicado por exp (1, 10, 100...)."""
    n = len(arr)
    salida = [0] * n
    cuenta = [0] * 10

    for num in arr:
        cuenta[(num // exp) % 10] += 1
    for i in range(1, 10):
        cuenta[i] += cuenta[i - 1]
    for i in range(n - 1, -1, -1):
        d = (arr[i] // exp) % 10
        cuenta[d] -= 1
        salida[cuenta[d]] = arr[i]
    return salida


def radix_sort_positivos(arr):
    if not arr:
        return arr
    maximo = max(arr)
    exp = 1
    while maximo // exp > 0:
        arr = counting_sort_por_digito(arr, exp)
        exp *= 10
    return arr


def radix_sort(arr):
    """Separa negativos y positivos, ordena cada grupo y los une."""
    negativos = [-x for x in arr if x < 0]
    positivos = [x for x in arr if x >= 0]

    positivos = radix_sort_positivos(positivos)
    negativos = radix_sort_positivos(negativos)
    negativos = [-x for x in reversed(negativos)]
    return negativos + positivos


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
                numeros.append(int(input(f"  Número {i + 1}: ")))
                break
            except ValueError:
                print("  Radix solo admite números enteros. Intenta de nuevo.")
    return numeros


def menu():
    while True:
        print("\n===== RADIX SORT =====")
        print("1. Ordenar números")
        print("2. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            n = leer_entero_positivo("¿Cuántos números deseas ordenar? ")
            numeros = leer_numeros(n)
            print("\nOriginal:", numeros)
            ordenados = radix_sort(numeros.copy())
            print("Ordenado (Radix):", ordenados)
        elif opcion == "2":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
