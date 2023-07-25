from clases.mascota import Mascota
from clases.perro import Perro
from clases.gato import Gato

jagger = Mascota( "Jagger", "Julieta" )
jagger.imprime_info()

max = Perro( "Max", "Andres", "Golden Retriever", "Golden" )
max.imprime_info()

max.acariciar_mascota()

chetos = Gato( "Chetos", "Alfredo", "Mediano" )

chetos.imprime_info()
chetos.acariciar_mascota()