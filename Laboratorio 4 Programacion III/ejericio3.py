def verificar_parentesis(cadena):
    """
    Verifica si los paréntesis en una cadena están balanceados.

    Parameters:
      cadena (str): La cadena que contiene los paréntesis a verificar.

    Returns:
      bool: True si los paréntesis están balanceados, False si no lo están.
    """
    # Conjuntos que contienen los caracteres de apertura y cierre de paréntesis
    abrir_par = set("([{")
    cerrar_par = set(")]}")

    # Pila para rastrear los paréntesis abiertos
    pila = []

    # Iterar a través de cada caracter en la cadena
    for caracter in cadena:
        # Si el caracter es un paréntesis de apertura, agregarlo a la pila
        if caracter in abrir_par:
            pila.append(caracter)
        # Si el caracter es un paréntesis de cierre
        elif caracter in cerrar_par:
            # Verificar si la pila está vacía, en cuyo caso no hay paréntesis abiertos para emparejar
            if not pila:
                return False
            # Obtener el último paréntesis abierto de la pila
            ultimo_caracter = pila.pop()
            # Verificar si los paréntesis coinciden
            if ultimo_caracter not in abrir_par or ultimo_caracter != caracter:
                return False

    # La cadena está balanceada si la pila está vacía al final
    return not pila

# Ejemplo de uso
cadena1 = "(()())"
cadena2 = "(()))"

# Imprimir resultados con explicaciones
print(f"Cadena '{cadena1}': {verificar_parentesis(cadena1)} (Balanceada si True, No balanceada si False)")
print(f"Cadena '{cadena2}': {verificar_parentesis(cadena2)} (Balanceada si True, No balanceada si False)")
