class ColaConPilas:
    def __init__(self):
        # Inicializar dos pilas: una para la entrada y otra para la salida
        self.pila_entrada = []  # Pila para encolar elementos
        self.pila_salida = []   # Pila para desencolar elementos

    def enqueue(self, elemento):
        """Encolar un elemento: Agrega el elemento a la pila de entrada."""
        self.pila_entrada.append(elemento)
        print(f"Elemento {elemento} encolado.")

    def dequeue(self):
        """Desencolar un elemento: Devuelve el elemento más antiguo en la cola."""
        if not self.pila_salida:
            # Si la pila de salida está vacía, transferir elementos de la pila de entrada
            # a la pila de salida para mantener el orden de la cola.
            while self.pila_entrada:
                self.pila_salida.append(self.pila_entrada.pop())

        if not self.pila_salida:
            # Ambas pilas están vacías, la cola está vacía.
            print("La cola está vacía.")
            return None

        # Pop de la pila de salida (que ahora contiene los elementos en orden de cola)
        elemento_desencolado = self.pila_salida.pop()
        print(f"Elemento {elemento_desencolado} desencolado.")
        return elemento_desencolado

# Ejemplo de uso
cola = ColaConPilas()

cola.enqueue(1)
cola.enqueue(2)
cola.enqueue(3)

print(cola.dequeue())  # Salida: 1
print(cola.dequeue())  # Salida: 2

cola.enqueue(4)
print(cola.dequeue())  # Salida: 3
print(cola.dequeue())  # Salida: 4
print(cola.dequeue())  # Salida: La cola está vacía. (None)

# Prueba desencolar de una cola vacía
print(cola.dequeue())  # Salida: La cola está vacía. (None)
