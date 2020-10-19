taka = float(input()) * 1000
notes = [100000, 50000, 20000, 10000, 5000, 2000]
coines = [1000, 500, 250, 100, 50, 10]
print("NOTAS:")
for i in notes:
    print("{} nota(s) de R$ {}".format(int((taka) // i), format(i / 1000, ".2f")))
    taka %= i
print("MOEDAS:")
for j in coines:
    print("{} moeda(s) de R$ {}".format(int(taka // j), format(j / 1000, ".2f")))
    quantia %= j