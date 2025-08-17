# main.py

def addmultiplenumbers(nums):
    """
    Suma todos los números de la lista.
    Ej.: [5, 7, 9] -> 21
    """
    return sum(nums)


def multiplymultiplenumbers(nums):
    """
    Multiplica todos los números de la lista en cadena.
    Ej.: [4, 5, 6, 7] -> 840
    Si la lista está vacía, devolvemos 1 (elemento neutro de la multiplicación).
    """
    result = 1
    for n in nums:
        result *= n
    return result


def isiteven(num):
    """
    Devuelve True si 'num' es un número entero y además par.
    Acepta enteros como 6, -2 y también flotantes como 6.0 (que son enteros).
    """
    # Verificamos primero si 'num' representa un entero (p. ej., 6.0)
    if isinstance(num, (int, float)) and float(num).is_integer():
        return int(num) % 2 == 0
    return False


def isitaninteger(num):
    """
    Devuelve True si 'num' es un número entero (sin parte decimal).
    Acepta 3 y 3.0 como enteros; 7.3 no lo es.
    """
    return isinstance(num, (int, float)) and float(num).is_integer()


def _parse_number_list(raw: str):
    """
    Utilidad para la interfaz interactiva: convierte una cadena como
    '4, -5, 6.7' o '4 -5 6.7' en [4, -5, 6.7].
    """
    # Admitimos comas y/o espacios como separadores
    # Filtramos vacíos por si hay dobles separadores
    tokens = [t for t in raw.replace(",", " ").split() if t]
    numbers = []
    for t in tokens:
        # Intentamos int primero para que '6' no se convierta a 6.0 innecesariamente
        try:
            numbers.append(int(t))
        except ValueError:
            numbers.append(float(t))
    return numbers


def main():
    print("Hello learners!")
    print("Bienvenido/a a la mini-calculadora.")
    while True:
        print("\nElige una opción:")
        print("1) Sumar una lista de números")
        print("2) Multiplicar una lista de números")
        print("3) ¿Es par?")
        print("4) ¿Es entero?")
        print("5) Salir")
        choice = input("> ").strip()

        if choice == "1":
            raw = input("Escribe números separados por coma o espacio: ")
            nums = _parse_number_list(raw)
            print("Resultado:", addmultiplenumbers(nums))

        elif choice == "2":
            raw = input("Escribe números separados por coma o espacio: ")
            nums = _parse_number_list(raw)
            print("Resultado:", multiplymultiplenumbers(nums))

        elif choice == "3":
            raw = input("Escribe un número: ")
            try:
                num = int(raw)
            except ValueError:
                num = float(raw)
            print("¿Es par?:", isiteven(num))

        elif choice == "4":
            raw = input("Escribe un número: ")
            try:
                num = int(raw)
            except ValueError:
                num = float(raw)
            print("¿Es entero?:", isitaninteger(num))

        elif choice == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
