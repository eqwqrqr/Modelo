# x es el número de km que puede correr una persona un día. Cada día puede correr un 10% más. y es la distancia que tiene que llegar a correr

import time   # Delay, también se pued usar Float Value

print ("Cuanto puedes correr el primer día?")
x= int(input())

print ("Cuanto necesitas correr?")
y= int(input())


# Hace que a x se le sume un 10% hasta llegar a ser igual o mayor que y
while x<y:
  x= (x+(x*0.1))

print ()

# Realmente no hace nada, es simplemente decorativo  
print  ("Calculando tiempo necesario...")
time.sleep(1)  
print ("25%")
time.sleep(1)
print ("50%")
time.sleep(1)
print ("75%")  
time.sleep(1)
print ("Done")
time.sleep(1.5)

print ()

# Te da los días que necesitas para llegar a correr y    
print (str(int(x)+1)+ " " + "son los días necesarios")
  
  
