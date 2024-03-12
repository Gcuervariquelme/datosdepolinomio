
class Nodo:
    def __init__(self, coeficiente, exponente):
        self.coeficiente = coeficiente
        self.exponente = exponente
        self.siguiente = None

class TDA_Polinomio:
    def __init__(self):
        self.cabeza = None

    def agregar_termino(self, coeficiente, exponente):
        nuevo_nodo = Nodo(coeficiente, exponente)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def mostrar_polinomio(self):
        actual = self.cabeza
        while actual is not None:
            print(f"{actual.coeficiente}x^{actual.exponente}", end=" ")
            actual = actual.siguiente
        print()

# Create an instance of TDA_Polinomio
polinomio1 = TDA_Polinomio()

# Add terms to polinomio1
polinomio1.agregar_termino(3, 2)
polinomio1.agregar_termino(2, 1)
polinomio1.agregar_termino(1, 0)

# Create another instance of TDA_Polinomio
polinomio2 = TDA_Polinomio()

# Add terms to polinomio2
polinomio2.agregar_termino(4, 3)
polinomio2.agregar_termino(2, 1)
polinomio2.agregar_termino(1, 0)

# Display polinomio1 and polinomio2
print("polinomio1:")
polinomio1.mostrar_polinomio()

print("polinomio2:")
polinomio2.mostrar_polinomio()
class Datos:
    def __init__(self, polinomio1, polinomio2):
        self.polinomio1 = polinomio1
        self.polinomio2 = polinomio2

    def sumar(self):
        resultado = TDA_Polinomio()
        actual1 = self.polinomio1.cabeza
        actual2 = self.polinomio2.cabeza

        while actual1 is not None and actual2 is not None:
            coeficiente = actual1.coeficiente + actual2.coeficiente
            exponente = actual1.exponente
            resultado.agregar_termino(coeficiente, exponente)
            actual1 = actual1.siguiente
            actual2 = actual2.siguiente

        while actual1 is not None:
            resultado.agregar_termino(actual1.coeficiente, actual1.exponente)
            actual1 = actual1.siguiente

        while actual2 is not None:
            resultado.agregar_termino(actual2.coeficiente, actual2.exponente)
            actual2 = actual2.siguiente

        return resultado

    def restar(self):
        resultado = TDA_Polinomio()
        actual1 = self.polinomio1.cabeza
        actual2 = self.polinomio2.cabeza

        while actual1 is not None and actual2 is not None:
            coeficiente = actual1.coeficiente - actual2.coeficiente
            exponente = actual1.exponente
            resultado.agregar_termino(coeficiente, exponente)
            actual1 = actual1.siguiente
            actual2 = actual2.siguiente

        while actual1 is not None:
            resultado.agregar_termino(actual1.coeficiente, actual1.exponente)
            actual1 = actual1.siguiente

        while actual2 is not None:
            resultado.agregar_termino(-actual2.coeficiente, actual2.exponente)
            actual2 = actual2.siguiente

        return resultado

    def multiplicar(self):
        resultado = TDA_Polinomio()
        actual1 = self.polinomio1.cabeza

        while actual1 is not None:
            actual2 = self.polinomio2.cabeza
            while actual2 is not None:
                coeficiente = actual1.coeficiente * actual2.coeficiente
                exponente = actual1.exponente + actual2.exponente
                resultado.agregar_termino(coeficiente, exponente)
                actual2 = actual2.siguiente
            actual1 = actual1.siguiente

        return resultado

    def dividir(self):
        resultado = TDA_Polinomio()
        actual1 = self.polinomio1.cabeza

        while actual1 is not None:
            actual2 = self.polinomio2.cabeza
            while actual2 is not None:
                coeficiente = actual1.coeficiente / actual2.coeficiente
                exponente = actual1.exponente - actual2.exponente
                resultado.agregar_termino(coeficiente, exponente)
                actual2 = actual2.siguiente
            actual1 = actual1.siguiente

        return resultado

# Create an instance of Datos
datos = Datos(polinomio1, polinomio2)

# Perform operations on polinomio1 and polinomio2
resultado_suma = datos.sumar()
resultado_resta = datos.restar()
resultado_multiplicacion = datos.multiplicar()
resultado_division = datos.dividir()

# Display the results
print("Suma:")
resultado_suma.mostrar_polinomio()

print("Resta:")
resultado_resta.mostrar_polinomio()

print("Multiplicación:")
resultado_multiplicacion.mostrar_polinomio()

print("División:")
resultado_division.mostrar_polinomio()