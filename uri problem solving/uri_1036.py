import math
  
a, b, c = list(map(float,input().split()))
d = b*b - 4*a*c
if(a > 0 and d > 0):
    squareRootValue = math.sqrt(d)
    R1 = (-b + squareRootValue) / (2*a)
    R2 = (-b - squareRootValue) / (2*a)
    print("R1 = {}".format(format(R1, '.5f')))
    print("R2 = {}".format(format(R2, '.5f')))

else:
    print("Impossivel calcular")