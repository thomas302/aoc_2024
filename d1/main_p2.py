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

sim = 0
for i in l1:
    sim += i * l2.count(i)

print(sim)
