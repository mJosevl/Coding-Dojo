"""
for( let i = 1; i <= 10; i ++ ){
    console.log( i );
}
"""

# Un solo parámetro en range es nuestro límite
for i in range( 11 ):
    print( i )

print( "----------" )
# Dos parámetros en range: El primero el valor inicial de la variable de control
#                          El segundo es nuestro límite
for i in range( 1, 11 ):
    print( i )

print( "----------" )
# Tres parámetros en range: El primero el valor inicial de la variable de control
#                           El segundo es nuestro límite
#                           El tercero es el incremento o decremento
for i in range( 1, 11, 3 ):   # i < 11
    print( i )

print( "----------" )
for i in range( 10, 0, -1 ):  # i > 0
    print( i )