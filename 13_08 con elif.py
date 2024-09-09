i = 0  
#Modificación 
nombre = input('Nombre: ')
apellido = input('Apellido: ')
anio = int(input('Año de nacimiento: '))
print("\n")

if anio >= 1928 and anio < 1946:
    gen = 'Generación Silenciosa'
    i = 1

elif anio >= 1946 and anio < 1965:
    gen = 'Baby Boomers'
    i = 1
    
elif anio >= 1965 and anio < 1981:
    gen = 'Generación X'
    i = 1
    
elif anio >= 1981 and anio < 1997:
    gen = 'Milenials'
    i = 1
    
elif anio >= 1997 and anio < 2013:
    gen = 'Generación Z'
    i = 1
    
elif anio >= 2013:
    gen = 'Generación Alpha'
    i = 1

if i == 1:    
    print(nombre 
          + " "
          + apellido
          + " nació en el año "
          + str(anio)
          + " y pertenece a la generación "
          + gen)
else: 
    print("Fuera de rango")

