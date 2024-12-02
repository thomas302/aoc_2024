l1 = list()
l2 = list()

with open("input.txt", 'r+') as f:
    lines = f.readlines()

    print(lines)
    
    for line in lines:
        print(line)
        temp = line.split("   ")
        print(temp)

        l1.append(int(temp[0]))
        l2.append(int(temp[1]))

l1.sort()
l2.sort()

out = 0
for i,j in tuple(zip(l1,l2)):
    out += abs(i - j);

print(out)
