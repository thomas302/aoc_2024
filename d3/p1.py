with open(r'.\velez\input', 'r') as f:
    x = f.read()

y = x.split("mul(")

del y[0]
out = 0
for i in y:
    z = i.split(")")
    a = z[0].split(",")
    if (a[0].isnumeric() and a[1].isnumeric() and len(a)==2):
        v1 = int(a[0])
        v2 = int(a[1])
        if(v1<1000 and v2<1000):
            out += v1*v2
print(out)
