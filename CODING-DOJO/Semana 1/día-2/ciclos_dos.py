
nombres = ['Alex', 'Martha', 'Roger', 'Julieta']

for nom in nombres:
    print( nom )

estudiante = {
    'nombre' : 'Alex',
    'apellido' : 'Gonzalez',
    'edad' : 25,
    'diplomas' : ['Yellow belt', 'Black belt']
}

for prop in estudiante:
    print( prop, estudiante[prop] )

for x in estudiante.values():
    print( x )


estudiantes = [{
    "nombre" : "Alex",
    "apellido" : "Gonzalez"
},
{
    "nombre" : "Martha",
    "apellido" : "Flores"
},
{
    "nombre" : "Roger",
    "apellido" : "Infante"
}]

for persona in estudiantes:
    print( persona )

dias_semana = {
    "Lun" : "Lunes",
    "Mar" : "Martes",
    "Mie" : "Miércoles",
    "Jue" : "Jueves",
    "Vie" : "Viernes",
    "Sáb" : "Sábado",
    "Dom" : "Domingo" 
}

for dia in dias_semana:
    print( dia, dias_semana[dia] )