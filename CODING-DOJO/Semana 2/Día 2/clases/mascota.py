
class Mascota:
    def __init__( self, nombre, dueño ):
        self.nombre = nombre
        self.dueño = dueño
    
    def imprime_info( self ):
        print( f"Nombre: {self.nombre}" )
        print( f"Dueño:  {self.dueño}" )

    def acariciar_mascota( self ):
        raise NotImplementedError