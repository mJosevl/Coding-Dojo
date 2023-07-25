from clases.mascota import Mascota

class Gato( Mascota ):
    def __init__( self, nombre, dueño, tamaño ):
        super().__init__( nombre, dueño )
        self.tamaño = tamaño
    
    # Polimorfismo
    def acariciar_mascota(self):
        print( f"El gato no estaba de buenas y se fue corriendo!" )