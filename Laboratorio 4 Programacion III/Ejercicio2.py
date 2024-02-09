class Cola:
    def __init__(self):
        self.cola = []

    def enqueue(self, elemento):
        self.cola.append(elemento)

    def dequeue(self):
        if len(self.cola) == 0:
            return None
        return self.cola.pop(0)

    def front(self):
        if len(self.cola) == 0:
            return None
        return self.cola[0]

    def empty(self):
        return len(self.cola) == 0

# Simulación de atención en una fila
cola = Cola()

# Agregar personas a la fila
cola.enqueue("Ana")
cola.enqueue("Juan")
cola.enqueue("Pedro")
cola.enqueue("María")

while not cola.empty():
    # Atender a la siguiente persona
    persona = cola.dequeue()
    print(f"Atendiendo a: {persona}")

# La fila está vacía
print("La fila está vacía")
