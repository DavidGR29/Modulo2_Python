palabraAdivinar = "Programador"

##Funcion
def adivinarPalabra (letra_prueba, palabra_intento):
    letraenPalabra = letra_prueba in palabraAdivinar
    print(f"¿La letra de prueba se encuentra en la palabra?\n {letraenPalabra}. ")
    resultadoAdivinanza = (palabra_intento ==  palabraAdivinar) and (len(palabra_intento) == len(palabraAdivinar) )
    print(f"El jugador gana: {resultadoAdivinanza}.")

## LLamar funcion
adivinarPalabra("o","Programador")
