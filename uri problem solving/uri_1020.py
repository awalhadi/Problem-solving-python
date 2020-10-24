days = int(input())
y = int(days / 365)
print("{y} ano(s)".format(y=y))
rest = days % 365
m = int(rest / 30)
print("{m} mes(es)".format(m=m))
d = rest % 30
print("{d} dia(s)".format(d=d))