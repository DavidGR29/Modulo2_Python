#Cabecera
def cabecera():
    """Muesta la cabecera de la aplicacion"""
    titulo = r"""
  ________                           ___________                     
 /  _____/_____    _____   __________\__    ___/____     ____  ______
/   \  ___\__  \  /     \_/ __ \_  __ \|    |  \__  \   / ___\/  ___/
\    \_\  \/ __ \|  Y Y  \  ___/|  | \/|    |   / __ \_/ /_/  >___ \ 
 \______  (____  /__|_|  /\___  >__|   |____|  (____  /\___  /____  >
        \/     \/      \/     \/                    \//_____/     \/ 
        ¡Crea tu identidad gamer!                                                                                                                                                                                                                                                                                                                                                                                                                    
""" 
    print(titulo)

cabecera()
#Tag Basico
def crear_tag_basico(nombre):
    """ 
    Crea un gamertag básico usando las primeras 4 lentras del nombre.
    
    Parámetros:
    nombre(str) : Escribe el nombre del usuario

    Retrona:
    st: Garmertag báscio
    """
    tag = nombre[0:4]
    print(f"1. TAG BASICO: {tag}", sep= "")



#Tag invertido
def crear_tag_invertido(nombre):
    """
    Crea una gamertag invirtiendo el nombre completo 

    Parámetro:
    str: El nombre del usuario

    Retorna:
    str: Gametag (nombre) invertido
    """
    tag = nombre[::-1] #Recorido al inversa
    print(f"2. TAG INVERTIDO: {tag}", sep = "")




#Tag Intercalado
def crear_tag_intercalado(nombre, apellido):
    """
    Debe combinar las iniciales del nombre y apellido, seguidas del resto de cada uno
    Parámetro:
    str : nombre y apelleido del usuario
    Retorna:
    str: nombre y apellido convinado
    """
    tag = nombre[0]
    tag1 = apellido[0]
    tag2 = nombre[1:]
    tag3 = apellido[1:]
    print(f"3. TAG INTERCALADO:{tag}{tag1}{tag2}{tag3}" , sep= "")
    




#Tag Elite
def crear_tag_elite(nombre):
    """
   Descripción:Debe tomar las primeras 2 letras y las últimas 2 letras del nombre. 
    Parámetro:
    str : nombre y apelleido del usuario
    Retorna:
    str: nombre y apellido convinado
    """
    tag1 = nombre[2:]
    tag2 = nombre[-2:]
    print(f"4. TAG ELITE: {tag1}{tag2}" , sep="")
   



#Tag con numero
def crear_tag_con_numero(nombre, numero_favorito):
    """
   Descripción:Debe combinar las primeras 5 letras del nombre con el número favorito.  
    Parámetro:
    str : nombre 
    int : numero_favorito
    Retorna:
    str: nombre 
    
    """
    tag = nombre[:5]
    print (f"5. TAG CON NUMERO:{tag} {numero_favorito}", sep = " ")

#Estadisticas Gamer
def mostrar_estadisticas(nombre):
    """ Descripción: Debe mostrar información estadística sobre el nombre del usuario. """
    print ("\n-- ESTADÍSTICAS DE TU NOMBRE: --\n")
    print (f"Nombre completo: {nombre}")
    print (f"Longitud del nombre: {len(nombre)}") 
    print (f"Primera letra: {nombre[1]}") 
    print (f"Última letra: {nombre[-1]}") 




# ========================================
#APLICACION PRINCIPAL
#=========================================

#Solictir datos al usuario
nombre = input("\nIntroduce tu nombre: ")
apeliido = input("\nIntroduce tu apellido: ")
numero = input("\nIntroduce tu numere favorito: ")


# Llamar_Funciones 
mostrar_estadisticas(nombre)
print ("""\n
====================================
TUS OPCIONES DE GAMER TAG:
====================================
       \n""")
crear_tag_basico(nombre)
crear_tag_invertido(nombre)
crear_tag_intercalado(nombre, apeliido)
crear_tag_elite(nombre)
crear_tag_con_numero(nombre, numero)
print ("\n===============================")