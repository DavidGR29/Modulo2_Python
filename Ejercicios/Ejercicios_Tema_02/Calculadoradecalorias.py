def calcularCalorias(carbohidratos,  proteinas ,  grasas):
    """ Informacion: 
    carbohidratos : int
    proteinas : int
    grasas : int

    return int 
    """
    operacion1 = carbohidratos * 4
    operacion2 = proteinas * 4
    operacion3 = grasas * 9
    totalCalorias = operacion1 + operacion2 +operacion3
    print(f"Calorias totales: {totalCalorias}")

calcularCalorias(10,20,30)
