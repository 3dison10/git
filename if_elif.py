# Clase 26-02-2024 if anidados
# nombre = "Nicolas"
# edad = 18
# sueldo = 2500000

# nombre = input("Digite su nombre:")
# edad = int(input("Cuantos años tienes  "))
# comfirma = "si"
# #sueldo = float(input("Digite su sueldo:"))

# #print(f"Su nombre es --> {nombre}, su edad es {edad + 10} y su sueldo es {sueldo + 1000000}")
# #print(type(edad))

# if (edad >= 42):
#     print("Tu tienes 42 años o mas!!")
#     edad_real = edad + 10
#     print(f"Tu tienes realmente {edad_real} años")
#     sueldo = int((input("¿Cuanto ganas?")))
#     if (sueldo <= 3000000):
#          print("Bueno gracias, adios")
#     if (sueldo >= 3000000):
#             #print("Te invito a tomar algo, vamos!!")
#             compromiso = input("¿Eres comprometida?")
#     if (compromiso == comfirma):
#         print("Hasta luego que estes bien!!")
#     else:
#         (compromiso != comfirma)
#         print("Vamos a tomar algo!!")
# else:
#     edad <= 42
#     print("Te falta un poco para mi")

# ----------Clase 28/02/2024  elif(Acambio del swich) ----------------

numero_1 = int(input("Por favor digite el primer numero:"))
numero_2 = int(input("Por favor digite el segundo numero:"))
print("MENU PRINCIPAL")
print("--------------")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("9. Salir")
opcion = int(input("---Que opcion desea realizar---"))
if (opcion==1):
    suma = numero_1 + numero_2 
    print(f"La suma es:{suma}")   
elif (opcion==2):
    if(numero_1 > numero_2):
       resta = numero_1 - numero_2
       print(f"La resta es:{resta}")
    if(numero_1<numero_2) :
       resta = numero_2 - numero_1
       print(f"La resta es:{resta}")
    if(numero_1==numero_2) :
       print("El resultado de la resta es 0")   
elif (opcion==3):
     multiplicacion = numero_1 * numero_2
     print(f"La multiplicacion es:{multiplicacion}")
elif (opcion==4):
     division = numero_1 / numero_2
     print(f"La division es:{division}")
elif (opcion==9):
     print("Saliendo de la ejecucion")
else:
      print("¡Opcion no valida!")
   
print("Estoy fuera del elif")


 

