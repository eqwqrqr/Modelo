print ("Qué año?")
año= int(input()) 

if (año %4 == 0) and (año % 100 != 0):
  print ("Bisiesto")

elif (año % 400 == 0):
  print("Bisiesto")

else:
  print ("No es bisiesto")