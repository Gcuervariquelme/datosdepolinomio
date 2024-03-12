import TDA_Polinomio from TDA_Polinomio
import Datos from Datos

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


