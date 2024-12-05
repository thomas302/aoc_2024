data = []
with open("input", "r") as f:
    data = f.read().split("\n")
del data[len(data)-1]

#get Rows
rcd = data.copy()
print(len(data))
print(len(data[0]))
#get cols
cols = []
for col in range(len(data[0])):
    s = ''
    for row in data:
        s+=''.join(row[col])
        #print(row[col])
    cols.append(s)
    
#get diaggonals
diag = ['']*(len(data)+len(data[0]))
rdiag = ['']*(len(data)+len(data[0]))
min_bdiag = -len(data) + 1

for i in range(len(data)):
    for j in range(len(data[0])):
        diag[i+j] = diag[i+j] + ''.join(data[j][i])
        rdiag[i-j-min_bdiag] = rdiag[i-j-min_bdiag] + ''.join(data[j][i])
        
rcd += cols
rcd += diag
rcd += rdiag

c = 0
for i in rcd:
    c += i.count("XMAS")
    c += i[::-1].count("XMAS")
print(c)