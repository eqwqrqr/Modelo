InicioX=int(input())
InicioY=int(input())
CasillaX=int(input())
CasillaY=int(input())
if (InicioX != CasillaX) and (InicioY != CasillaY):
  print ("No")
elif (InicioX == CasillaX) or (InicioY == CasillaY):
  print("Yes")