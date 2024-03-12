import nodo from nodo

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