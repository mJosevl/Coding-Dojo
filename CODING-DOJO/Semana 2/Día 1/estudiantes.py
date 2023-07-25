
class Stack:
    def __init__( self, nombre, calificacion ):
        self.nombre = nombre
        self.calificacion = calificacion
    
    def imprime_info( self ):
        print( f"Nombre: {self.nombre}" )
        print( f"Calificación: {self.calificacion}" )

class Estudiante:
    pais = "Chile"
    lista_estudiantes = []

    def __init__( self, nombre, apellido, identificador, stack ):
        self.nombre = nombre
        self.apellido = apellido
        self.identificador = identificador
        self.stack = stack
        Estudiante.lista_estudiantes.append( self )
    
    def imprime_info( self ):
        print( f"Nombre: {self.nombre}" )
        print( f"Apellido: {self.apellido}" )
        print( f"Identificador: {self.identificador}" )
        print( f"Pais: {self.pais}" )
        print( f"Stack:" )
        self.stack.imprime_info()
    
    @classmethod
    def imprime_nombres_estudiantes( cls ):
        for estudiante in cls.lista_estudiantes:
            print( f"{estudiante.nombre} {estudiante.apellido}" )

    @classmethod
    def imprime_todos_los_estudiantes( cls ):
        for estudiante in cls.lista_estudiantes:
            estudiante.imprime_info()
    
    @classmethod
    def promedio_general( cls ):
        suma = 0.0
        for estudiante in cls.lista_estudiantes:
            suma += estudiante.stack.calificacion
        promedio = suma / len( cls.lista_estudiantes )
        return promedio
    
    @staticmethod
    def imprime_hola( nombre ):
        print( f"Hola, {nombre}" )

alex_python = Stack( "Python", 9.4 )
martha_java = Stack( "Java", 8.7 )
roger_fundamentos = Stack( "Fundamentos de la Web", 10.0 )
alan_python = Stack( "Python", 6.8 )

alex = Estudiante( "Alex", "Miller", 12345, alex_python )
martha = Estudiante( "Martha", "Gonzalez", 62634, martha_java )
roger = Estudiante( "Roger", "Infante", 82828, roger_fundamentos )
alan = Estudiante( "Alan", "Morales", 63543, alan_python )


Estudiante.pais = "Costa Rica"
Estudiante.imprime_todos_los_estudiantes()
print( "--------" )
print( Estudiante.lista_estudiantes )
print( "--------" )
Estudiante.imprime_nombres_estudiantes()
print( f"Promedio general: {Estudiante.promedio_general()}")


Estudiante.imprime_hola( "Julieta" )

