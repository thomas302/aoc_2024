data = [
        [7,6,4,2,1],
        [1,2,7,8,9],
        [9,7,6,2,1],
        [1,3,2,4,5],
        [8,6,4,4,1],
        [1,3,6,7,9]
        ]

'''
with open("input", 'r+') as f:
    l = f.readlines()

    for i in l:
        data.append([int(x) for x in i.split(" ")])
'''

print(data)

def checkVals(x:list)->bool:
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
    



    

out = filter(checkVals, data)

print(len(list(out)))
