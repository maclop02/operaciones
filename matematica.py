def suma(a, b):
    """Devuelve la suma de dos números."""
    return a + b

def resta(a, b):
    """Devuelve la resta de dos números."""
    return a - b

def multiplicacion(a, b):
    """Devuelve la multiplicación de dos números."""
    return a * b

def division(a, b):
    """Devuelve la división de dos números. Lanza una excepción si el divisor es cero."""
    if b == 0:
        raise ValueError("El divisor no puede ser cero.")
    return a / b
