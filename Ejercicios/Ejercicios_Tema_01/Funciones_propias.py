#Contador de caracteres
def contar_caracteres (arg1):
 """Este es un docStrings
 
   Keyword arguments:
   arg1-- Colocar un str"""
 print(f"\n La frase '{arg1}' tiene: {len(arg1)} caracteres")

#Convertidor de Numeros
def convertir_numero(arg2):
 """Este es docStrings
 Keyword arguments:
 arg2 -- Colocar un int"""
 texto = str(arg2)
 num_float = float(arg2)
 print(f"\n Entero: {arg2} Tipo: {type(arg2)}\n \n Cadena: {texto} Tipo: {type(texto)}\n \n Flotante: {num_float} Tipo: {type(num_float)}\n ")


# Llamada
print("\n--Contador de caracteres--")
contar_caracteres("Aprender Python es divertido")
print("\n--Convertidor de numeros--")
convertir_numero(42)
    
