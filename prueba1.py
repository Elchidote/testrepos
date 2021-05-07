def promedio_std(lista):
    ## x es promedio
    ## y es desviasion estandar
    ## esto esta hecho en chield branch
    suma = 0
    SumaEstandar = 0
    i = 0
    j = 0
    while i < len(lista):
       suma = suma + int(lista[i])
       i = i + 1
    x = suma / (len(lista))

    return(x)

a =[1,2,3,4,5,6,7]
print(promedio_std([1,2,3,4,5,6,7]))
