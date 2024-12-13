import re
with open("input") as f:
    data = f.read()

rules = re.findall(r'(\d{2})\|(\d{2})',data)
data = re.findall(r"(\d{2},.*)\n", data)

l =  list(set([i[0] for i in rules] + [i[1] for i in rules]))

class value:
    def __init__(self, v, rules):
        self.v = v
        self.lt = [k[1] for k in filter(lambda k: k[0]==v, rules)]

    def __lt__(self, other):
        return other.v in self.lt
    def __repr__(self):
        return str(self.v)


def convertToVals(l):
    vals = []
    for v in l:
        vals.append(value(v, rules))
    return vals


data = [convertToVals(e.split(',')) for e in data]

c = 0
c2 = 0 
for e in data:
    s = sorted(e)
    if e == s:
        c+= int(e[len(e)//2].v)
    else:
        c2+=int(s[len(s)//2].v)e
        
print(c)
print(c2)