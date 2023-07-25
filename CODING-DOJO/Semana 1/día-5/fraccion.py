# Clase
class Fraccion:
    # Constructor
    def __init__( self, numerador = 2, denominador = 3 ):
        # Atributos de instancia
        self.numerador = numerador
        self.denominador = denominador
        self.mensage = "¡Hola a todas!"
    # Método de instancia
    def imprimir( self ):
        print( f"{self.numerador}/{self.denominador}" )
        return self
    
    def suma( self, fraccion_adicional ):
        num_resultante = self.numerador * fraccion_adicional.denominador + fraccion_adicional.numerador * self.denominador
        den_resultante = self.denominador * fraccion_adicional.denominador
        resultado = Fraccion( num_resultante, den_resultante )
        return resultado
    
    def imprime_hola( self ):
        print( self.mensage )
        return self

fraccion_uno = Fraccion( 1, 2 )
fraccion_dos = Fraccion( 3, 4 )
fraccion_uno.imprimir()

fraccion_dos.imprimir()

fraccion_resultante = fraccion_uno.suma( fraccion_dos )
fraccion_resultante.imprimir()
fraccion_resultante_dos = fraccion_dos.suma( fraccion_uno )
fraccion_resultante_dos.imprimir() 
"""
fraccion_uno = Fraccion( 1, 2 )
print( fraccion_uno )
print( fraccion_uno.numerador )
print( fraccion_uno.denominador )
print( fraccion_uno.mensage )
fraccion_uno.mensage = "Estamos aprendiendo Programación Orientada a Objetos"
print( fraccion_uno.mensage )

fraccion_dos = Fraccion( 3, 4 )
print( fraccion_dos )
print( fraccion_dos.numerador )
print( fraccion_dos.denominador )
print( fraccion_dos.mensage )

fraccion_uno.imprimir()
fraccion_dos.imprimir()


fraccion_tres = Fraccion( )
fraccion_tres.imprimir()
"""

fraccion_uno.imprimir().imprime_hola()
