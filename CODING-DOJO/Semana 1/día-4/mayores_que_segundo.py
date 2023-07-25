
def mayores_que_segundo( lista ):
    resultado = []

    if len( lista ) >= 2:
        for numero in lista:
            if numero > lista[1]:
                resultado.append( numero )
    
    print( len( resultado ) )
    if len( resultado ) < 2:
        return False
    else:
        return resultado
    
lista1 = mayores_que_segundo( [5, 2, 3, 2, 1, 4] )
print( lista1 )
lista2 = mayores_que_segundo( [3] )
print( lista2 )
lista3 = mayores_que_segundo( [8, 3, 2, 9, 7, 5, 1, 10, 6, 4] )
print( lista3 )
lista4 = mayores_que_segundo( [4, 2] )
print( lista4 )