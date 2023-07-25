
def cuenta_regresiva( num ):
    resultado = []
    #while num >= 0:
    #    resultado.append( num )
    #    num -= 1

    for i in range( num, -1, -1 ):  # num > -1    num -= 1
        resultado.append( i )

    return resultado

lista1 = cuenta_regresiva( 5 )
lista2 = cuenta_regresiva( 10 )
lista3 = cuenta_regresiva( 20 )

print( lista1 )
print( lista2 )
print( lista3 )