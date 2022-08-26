
#datos generales
nombre = input("Introduce tu nombre: ")
apellidopaterno = input("introduce tu apellido paterno: ")
apellidomaterno = input("introduce tu apellido materno: ")
edad = int(input("introduce tu edad: "))
peso = float(input("Introduce tu peso  en (kg) por favor: "))
estatura = float(input("Introduce tu estatura en (m) por favor: "))

print("Nombre: " + nombre)
print("Apellido paterno: " + apellidopaterno)
print("Apellido materno: " + apellidomaterno)
print("Tu edad es: " + str( edad) + " años")
print(" Tu peso: " + str(peso) + " kg")
print(" Tu estatura: " + str(estatura) + " m")

#Indice de Masa Corporal

indice = float(peso/estatura**2)

if indice >= 0 and indice <= 18.9 :
 print("tienes peso bajo")
if indice >= 18.50 and indice <= 24.99 :
    print("tienes peso normal")
if indice >= 25.00 and indice <= 29.99 :
    print("tienes sobrepeso")
if indice >= 30.00 and indice <= 34.99 :
    print("tienes obesidad leve")
if indice >= 35.00 and indice <= 39.99 :
    print("tienes obesidad media")
if indice >= 40.00 :
    print("tienes obesidad morbida")