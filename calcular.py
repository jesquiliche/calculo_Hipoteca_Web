# Este código en Python es un programa que calcula una hipoteca. 
# Toma como entrada el capital, los años y el interés, y 
# luego calcula la cuota mensual y el total a pagar. 
# También muestra un cuadro que detalla el interés, la amortización y 
# el capital pendiente de cada mes de la hipoteca. Finalmente, 
# devuelve una lista de diccionarios que contienen la información del cuadro.



def Calcular_hipoteca(capital,anos,interes):
    #Entrada de datos

    #Operaciones necesarias
    plazos = anos * 12
    interesMensual = interes / 12

    cuota = capital*interesMensual/(100*(1-(1+interesMensual/100)**-plazos))
    round (cuota, 2)

    hipoteca = cuota * plazos
                                        
    #Mostrar resultado
   

    pagado= 0
    # Calculamos el intres mensual
    interes_mensual = interes  / 12 / 100  #para calcular intereses de cada mes

    # Montamos el cuadro de amorización 
    cuadro=[]
    pago={}
    # Montamos el cuadro de amoritzación en un lista con datos de diccionario
    for mes in range (plazos):
    
        intereses_mes_actual = (capital - pagado) * interes_mensual
        amortiza_mes_actual = cuota - intereses_mes_actual
        #calculos
        pagado = pagado + amortiza_mes_actual
       
        # Guardamos el pago del mes actual en un diccinario y lo añadimos a la lista
        pago={"mes":mes+1,"intereses":round(intereses_mes_actual,2),
        "cuota":round(cuota,2),"amortizacion":round(amortiza_mes_actual,2),"capital_ped":round(capital-pagado,2)}
        cuadro.append(pago)
    return cuadro
    #Fin
    
    

print(Calcular_hipoteca(10000,4,10))