# ----------Clase 28/02/2024  elif(Acambio del swich) ----------------
numero = int(input("Ingrese un numero del 1 al 10 por favor: "))

if (numero == 1):
    numero_letras = "UNO"
elif (numero == 2):
    numero_letras = "DOS"
if (numero == 3):
    numero_letras = "TRES"
elif (numero == 4):
    numero_letras = "CUATRO"
elif (numero == 5):
    numero_letras = "CINCO"   
elif (numero == 6):
    numero_letras = "SEIS"
elif (numero == 7):
    numero_letras = "SIETE"
elif (numero == 8):
    numero_letras = "OCHO"
elif (numero == 9):
    numero_letras = "NUEVE"
elif (numero == 10):
    numero_letras = "DIEZ"
    
else:
    print("Ingreso un numero fuera de rango")
    numero_letras = "Incorrecto"
    
print(f"El numero ingresado es: {numero_letras}")
    