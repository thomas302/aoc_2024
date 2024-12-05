data = []
with open("input", "r") as f:
    data = f.read().split("\n")
del data[len(data)-1]

# Find A's not on the perimiter
a_pos = []
for r in range(len(data)):
    for c in range(len(data[0])):
        if r == 0 or c == 0 or r == (len(data)-1) or c==(len(data[0])-1):
            continue
        if data[r][c] == 'A':
            a_pos.append((r,c))

checkList = [
    (
        ''.join([
            data[i[0]+1][i[1]-1],
            data[i[0]][i[1]],
            data[i[0]-1][i[1]+1]
        ]),
        ''.join([
            data[i[0]-1][i[1]-1],
            data[i[0]][i[1]],
            data[i[0]+1][i[1]+1]
        ])
    )
    for i in a_pos
]

count = 0
for i in checkList:
    if(set([i]).issubset({('SAM', 'SAM'), ('MAS', 'SAM'), ('MAS', 'MAS'), ('SAM', 'MAS')})):
        count += 1

print(count)