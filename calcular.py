def Calcular_hipoteca(capital,anos,interes):
    #Entrada de datos

    #Operaciones necesarias
    plazos = anos * 12
    interesMensual = interes / 12

    cuota = capital*interesMensual/(100*(1-(1+interesMensual/100)**-plazos))
    round (cuota, 2)

    hipoteca = cuota * plazos
                                        
    #Mostrar resultado
   
    print (' En una hipoteca de capital: ', capital, ' y con un interes de ', interes)
    print (' a pagar en: ', anos, ' ańos ')
    print (' Tendra que pagar ', plazos, ' cuotas mensuales de ',"%12.2f" % cuota, ' euros ')
    print (' Con lo que usted debera pagar un total de: ', "%12.2f" % hipoteca)

    print ('*' * 80)

    pagado= 0
    interes_mensual = interes  / 12 / 100  #para calcular intereses de cada mes

   # print ("%4s  %12s  %12s  %12s" %  ("Mes", "Intereses", "Amortiza", "Pendiente"))
    cuadro=[]
    pago={}
    for mes in range (plazos):
        #datos que voy a mostrar
        intereses_mes_actual = (capital - pagado) * interes_mensual
        amortiza_mes_actual = cuota - intereses_mes_actual
        #calculos
        pagado = pagado + amortiza_mes_actual
       # print ("%4d  %12.2f   %12.2f  %12.2f" %   (mes+1, intereses_mes_actual, amortiza_mes_actual, capital -pagado))
        pago={"mes":mes+1,"intereses":round(intereses_mes_actual,2),
        "cuota":round(cuota,2),"amortizacion":round(amortiza_mes_actual,2),"capital_ped":round(capital-pagado,2)}
        cuadro.append(pago)
    return cuadro
    #Fin
    input (' Pulse intro para salir ')
    

print(Calcular_hipoteca(10000,4,10))