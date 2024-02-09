class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def reverse_half(self):
        if self.is_empty():
            return

        stack = []
        size = self.size()

        # Extraer la mitad de los elementos y empujarlos a la pila
        for _ in range(size // 2):
            stack.append(self.dequeue())

        # Revertir la mitad de la cola
        while stack:
            self.enqueue(stack.pop())

        # Mover los elementos restantes a la cola
        for _ in range(size // 2):
            self.enqueue(self.dequeue())

    def __str__(self):
        return str(self.items)


# Ejemplo de uso:
if __name__ == "__main__":
    q = Queue()
    for i in range(1, 11):
        q.enqueue(i)

    print("Cola original:", q)
    q.reverse_half()
    print("Cola con la mitad revertida:", q)
