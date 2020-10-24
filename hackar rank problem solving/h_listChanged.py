def mutable_change(string, position, character):
    l = list(string)
    l[position] = character
    string  = ''.join(l)
    return string

s = "Natora"
z = "5 e"
i, p = z.split()
string = mutable_change(s, int(i), p)
print(string)