# ========================================== 

# CALCULADORA DE FITNESS Y SALUD PERSONAL 

# ========================================== 
nombre = input("Introudce tu nombre:\n")
imc = float(input("Introduce tu IMC por favor:\n"))
peso_kg =float(input("Introduce tu peso en KG:\n"))
altura_m =float(input("Introduce tu altura en M:\n"))
edad = int(input("Introduce tu edad:\n"))
es_hombre = bool(input("Eres Hombre TRUE/FALSE:\n"))

def calcular_imc(): 

    """ 
    Calcula el Índice de Masa Corporal (IMC). 
    Fórmula: IMC = peso / (altura^2) 

    Parámetros: 
    peso_kg (float): Peso en kilogramos 
    altura_m (float): Altura en metros 

    Retorna: 
    float: El IMC calculado 
    """ 
    imc = peso_kg / (altura_m ** 2) 
    print(f"Tu IMC es igual a = {imc}")


def es_peso_saludable(): 

    """ 
    Determina si el IMC está en rango saludable (18.5 - 24.9). 

    Parámetro: 
    imc (float): Índice de Masa Corporal

    Retorna: 
    bool: True si está en rango saludable, False si no 

    """ 
    # Operadores de comparación y lógicos 
    return imc >= 18.5 and imc <= 24.9 

def tiene_sobrepeso(): 
    """ 
    Determina si hay sobrepeso (IMC >= 25). 
    """ 
    if (imc >= 25 ):
        print(f"Tiene sobrepeso {True}", sep= " "  )
    else:
        print(f"No tiene sobrepeso{False}", sep= " ")


def tiene_bajo_peso(): 
    """ 
    Determina si hay bajo peso (IMC < 18.5). 
    """ 
    if (imc < 18 ):
        print(f"Tiene bajo peso {True}", sep= " "  )
    else:
        print(f"No tiene bajo peso {False}", sep= " ")






def calcular_calorias_diarias(): 
    """ 
    Calcula las calorías diarias recomendadas usando Fórmula de Harris-Benedict. 

    Parámetros: 
    peso_kg (float): Peso en kg 
    altura_cm (float): Altura en cm 
    edad (int): Edad en años 
    es_hombre (bool): True si es hombre, False si es mujer 


    Retorna: 

    float: Calorías diarias recomendadas 

    """ 
    # Operadores aritméticos y booleanos 
    # Fórmula para hombres: 88.362 + (13.397 × peso) + (4.799 × altura) - (5.677 × edad) 
    # Fórmula para mujeres: 447.593 + (9.247 × peso) + (3.098 × altura) - (4.330 × edad) 
  
    calorias_hombre = 88.362 + (13.397 * peso_kg) + (4.799 * (altura_m*100)) - (5.677 * edad) 
    calorias_mujer =  447.593 + (9.247 * peso_kg) + (3.098 * (altura_m*100)) - (4.330 * edad)
    #USa el hecho de que TRUE = 1 y False=0 
    return es_hombre * calorias_hombre + (1 - es_hombre) * calorias_mujer

  
def calcular_agua_diaria(): 
    """ 
    Calcula litros de agua recomendados al día (35ml por kg de peso). 
    """ 
    ml_agua = peso_kg * 35 
    litros_agua = ml_agua / 1000 
    return litros_agua




def calcular_ritmo_cardiaco_maximo(): 
  """ Calcula el ritmo cardíaco máximo (220 - edad). """
  return 220-edad

##Llamar funciones 

print(""""
# ========================================== 

    CALCULADORA DE FITNESS Y SALUD PERSONAL 

# ========================================== 
      """)

print(f"Tu nombre es {nombre} \n")
calcular_imc()
es_peso_saludable()
tiene_sobrepeso()
tiene_bajo_peso()
calcular_calorias_diarias()
calcular_agua_diaria()
calcular_ritmo_cardiaco_maximo()