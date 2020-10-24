lines = str(input(" "))
split = lines.split()
a = int(split[0])
b = int(split[1])
c = int(split[2])
max = max(a, b, c)
ot = str(max) + "eh o maior"
print(ot)