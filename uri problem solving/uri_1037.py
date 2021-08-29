inputNumber = float(input())
if (inputNumber >= 0 and inputNumber <= 25):
    print("Intervalo [0,25]")
elif (inputNumber > 25 and inputNumber <= 50):
    print("Intervalo (25,50]")
elif (inputNumber > 50 and inputNumber <= 75):
    print('Intervalo (50,75]')
elif(inputNumber > 75 and inputNumber <= 100):
     print('Intervalo (75,100]')
elif(inputNumber < 0 or inputNumber > 100):
     print('Fora de intervalo')

