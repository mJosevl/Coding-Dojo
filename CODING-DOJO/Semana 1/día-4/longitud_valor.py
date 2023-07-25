
def longitud_valor( longitud, valor ):
    lista = []
    i = 1
    while i <= longitud:
        lista.append( valor )
        i += 1
    return lista

resultado1 = longitud_valor( 4, 7 )
print( resultado1 )
resultado2 = longitud_valor( 6, 2 )
print( resultado2 )
resultado3 = longitud_valor( 10, 8 )
print( resultado3 )
