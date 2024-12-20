data = []

with open("input", 'r+') as f:
    l = f.readlines()

    for i in l:
        data.append([int(x) for x in i.split(" ")])

'''
    [7,6,4,2,1],
        [1,2,7,8,9],
        [9,7,6,2,1],
        [1,3,2,4,5],
        [8,6,4,4,1],
        [1,3,6,7,9]
    ]
'''
count = 0;
def checkVals(x:list)->bool:
    global count
    count+=1;
    y = x.copy();

    y.sort();
    
    if (x == y or x == y[::-1]):
        for i in range(len(x)):
            if i == (len(x)-1):
                break

            if abs(x[i]-x[i+1]) > 3 or abs(x[i]-x[i+1])<=0: 
                return False
    else:
        return False

    return True

def checkDampener(x):
    if checkVals(x):
        return True

    for i in range(len(x)):
        y = x.copy()
        
        del y[i]
        if checkVals(y):
            return True

    return False

out_2 = filter(checkDampener, data)

print(len(list(out_2)))

print("iterations", count)
