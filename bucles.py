# vuelta = int(input("Cuantas vueltas desea dar:"))
# for i in range (vuelta): 
#     print(f"Vuelta {i}")

# vuelta = int(input("Cuantas vueltas desea dar:"))
# for i in range (1,vuelta+1, 1): 
#     print(f"Vuelta {i}")
    
# for i in range (1,10, 2): 
#     print(f"Vuelta {i}")   

# billetes = int(input("Cuantos billetes va a ingresar:"))
# valorBillete = int(input("De que denominacion es el billete:"))
# total = 0
# for i in range (1,billetes+1,1):
#     total = total+ valorBillete 
#     print(f"En total lleva de dinero:{total}") 


# Tabla de multiplicar que el usuario requiera  mostrando 1 hasta el 10    

#--------------------------------------------------------------
'''numero = int(input("Que tabla de multiplicar desea realizar:"))
for i in range (1, 10+1, 1):
       resultado = numero * i 
       print(f"{numero} x {i} = {resultado} ")
       '''
# --------------------------------------------------------     


# # Serie de fibonacci0 1 1 2 3 5 8 13 21 ¿Cuntos numeros desea la serie?

cantidad = int(input("Cuantos numeros desea realizar para la serie de Fibonacci: "))
cero = 0
a = 1
b = 1
print(f"{cero}\n{a} \n{b}")
for i in range (cantidad-3): 
    c = a + b  #2
    b = a      #1
    a = c      #2
    print(c)
 

    