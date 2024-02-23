import math
# input

X=int(input("digite el valor de X:" ))

#processing

r=X%2

if r==0:
    rta= "Par"

else:
    rta= "Impar"

# output

print("el numero " + str(X)+ " es " + rta)
