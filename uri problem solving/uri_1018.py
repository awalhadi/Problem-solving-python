notes = int(input())
print(notes)
print("{} nota(s) de R$ 100,00".format(int(notes/100)))
restTaka = (notes%100)
print("{} nota(s) de R$ 50,00".format(int(restTaka/50)))
restTaka = (restTaka%50)
print("{} nota(s) de R$ 20,00".format(int(restTaka/20)))
restTaka = (restTaka%20)
print("{} nota(s) de R$ 10,00".format(int(restTaka/10)))
restTaka = (restTaka%10)
print("{} nota(s) de R$ 5,00".format(int(restTaka/5)))
restTaka = (restTaka%5)
print("{} nota(s) de R$ 2,00".format(int(restTaka/2)))
restTaka = (restTaka%2)
print("{} nota(s) de R$ 1,00".format(int(restTaka/1)))
