from clases.mascota import Mascota

class Perro( Mascota ):
    def __init__( self, nombre, dueño, raza, color ):
        super().__init__( nombre, dueño )
        self.raza = raza
        self.color = color
    
    def imprime_info_perro( self ):
        super().imprime_info()
        print( f"Raza:  {self.raza}" )
        print( f"Color: {self.color}" )

    # Sobrescritura (Overriding)
    def imprime_info( self ):
        self.imprime_info_perro()

    # Polimorfismo
    def acariciar_mascota( self ):
        print( "El perro esta muy feliz!" )