
"""
    Clase que maneja el conjunto de los primeros 100 números. 
    Esta clase tendra metodos para extraer un número y calcular el número que fue
    extraido.
"""
class NumberSet:
    # Crea un conjunto de los primeros 100 números
    def __init__(self):
        self.numbers = set(range(1, 101))
        self.extracted_number = None
        
    #Extrae el número dado, siempre que esté en el rango válido.
    def extract(self, number):
        if not (1 <= number <= 100):
            raise ValueError("El número debe estar entre 1 y 100")
        self.numbers.remove(number)
        self.extracted_number = number

    #Calcula el número que falta en el conjunto.
    def calculate_missing(self):
        if self.extracted_number is None:
            raise ValueError("No se ha extraído ningún número")
        return 5050 - sum(self.numbers)
