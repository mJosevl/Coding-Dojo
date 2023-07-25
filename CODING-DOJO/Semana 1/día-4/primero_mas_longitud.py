
def primero_mas_longitud( lista ):
    resultado = lista[0] + len( lista )
    return resultado

resultado1 = primero_mas_longitud( [1, 2, 3, 4, 5] )
resultado2 = primero_mas_longitud( [10, 12, 42, 23, 12, 23, 45] )

print( resultado1 )
print( resultado2 )