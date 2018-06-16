p = input(str("¿Qué tipo de operación desea realizar?, use (suma, resta, multiplicacion, division o potencia) para definirla:"))
x = int(input("Ingrese primer número:",))
y = int(input("Ingrese segundo número:",))

if p=="suma":
  print("La suma es: ", x+y)
elif p=="multiplicacion":
  print("La multiplicacion es: ", x*y)
elif p=="potencia":
  print("La potencia es: ",x**y)
elif p=="resta":
  print("La resta es: ",x-y)
elif p=="division":
  print("La división es: ", x/y)
else:
  print("Aún no creamos esa variable")
