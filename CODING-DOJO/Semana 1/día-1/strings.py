edad = 25
nombre = 'Alejandro'
apellido = "Venegas"

resultado = f"Hola como estas {nombre} {apellido}. ¡Hoy cumples {edad} años!"
resultado2 = "Hola como estas " + nombre + " " + apellido + ". ¡Hoy cumples " + str(edad) + " años!"
resultado3 = "Hola como estas {} {}. ¡Hoy cumples {} años!".format( nombre, apellido, edad )
print( resultado )
print( resultado2 )
print( resultado3 )

print( nombre.upper(), len( nombre ) )