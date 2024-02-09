class Pila:
    def __init__(self):
        self.items = []

    def push(self, elemento):
        # Agregar un elemento en la parte superior de la pila
        self.items.append(elemento)

    def pop(self):
        # Quitar y devolver el elemento en la parte superior de la pila
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Pop en una pila vacía")

    def peek(self):
        # Devolver el elemento en la parte superior de la pila sin quitarlo
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Observar en una pila vacía")

    def is_empty(self):
        # Verificar si la pila está vacía
        return len(self.items) == 0

    def size(self):
        # Devolver el número de elementos en la pila
        return len(self.items)

    def __str__(self):
        # Devolver una representación en cadena de la pila
        return str(self.items[::-1])

class Cola:
    def __init__(self):
        self.items = []

    def enqueue(self, elemento):
        # Agregar un elemento al final de la cola
        self.items.append(elemento)

    def dequeue(self):
        # Quitar y devolver el elemento del frente de la cola
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Desencolar de una cola vacía")

    def peek(self):
        # Devolver el elemento del frente de la cola sin quitarlo
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Observar en una cola vacía")

    def is_empty(self):
        # Verificar si la cola está vacía
        return len(self.items) == 0

    def size(self):
        # Devolver el número de elementos en la cola
        return len(self.items)

    def __str__(self):
        # Devolver una representación en cadena de la cola
        return str(self.items)

def invertir_lista(elementos):
    # Crear una nueva pila
    p = Pila()

    # Empujar cada elemento en la pila
    for elemento in elementos:
        p.push(elemento)

    # Sacar cada elemento de la pila y agregarlo a la lista de resultados
    resultado = []
    while not p.is_empty():
        resultado.append(p.pop())

    # Devolver la lista de resultados
    return resultado

# Crear una lista de números
numeros = [1, 2, 3, 4, 5]

# Invertir la lista usando la función invertir_lista
numeros_invertidos = invertir_lista(numeros)

# Imprimir la lista original y la lista invertida
print("Lista original:", numeros)
print("Lista invertida:", numeros_invertidos)
