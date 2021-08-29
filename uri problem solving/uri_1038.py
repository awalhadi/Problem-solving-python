
x,y =list(map(int,input().split()))

prices = [4.00, 4.50, 5.00, 2.00, 1.50]
totalPrice = format(prices[x-1]*y, '.2f')
print("Total: R$ {}". format(totalPrice))