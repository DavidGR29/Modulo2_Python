def compararLogitud(palabra1, palabra2):
    longitud1 = len(palabra1)
    longitud2 = len(palabra2)
    longitud = longitud1 == longitud2
    return print(f"¿Son {palabra1} y {palabra2} dos palabras con la misma logintud: {longitud}")

compararLogitud("Perro", "Loro")