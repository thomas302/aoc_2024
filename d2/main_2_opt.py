import timeit
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
    for i in range(len(x)):
        y = x.copy()
        
        del y[i]
        if checkVals(y):
            return True

    return False
start = timeit.default_timer()
for i in range(10000):
    out_2 = filter(checkDampener, data.copy())
time = timeit.default_timer() - start

print(time)
print(len(list(out_2)))

print("iterations", count)
