import copy
_input = '''.........
.#.......
........#
........#
........#
........#
........#
#...^...#
.......#.
'''

with open('input') as f:
    _input = f.read()

_map = _input.split('\n')


print(_map)
del _map[-1]

def get_start(_map: list)->tuple:
    for l in range(len(_input)):
        line = _map[l]
        c = line.find('^')
        if not c == -1:
            return [l, c]

def traverse_direction(_map, start, direction):
    pos = start
    while True:
        if pos[0] < len(_map) and pos[1] < len(_map[0]) and pos[0] >= 0 and pos[1] >= 0:
            current_val = _map[pos[0]][pos[1]]
            if current_val == '#':
                return [pos[0]-direction[0], pos[1]-direction[1]], [direction[1], -direction[0]], True, _map
            else:
                s = _map[pos[0]] 
                _map[pos[0]] = s[:pos[1]] + 'X' + s[pos[1] + 1:]
                
        else:
            return [pos[0], pos[1]], direction, False, _map
            
        pos[0] += direction[0]
        pos[1] += direction[1]

direction = [-1, 0]

start = get_start(_map)
print(start)

orig_start = start.copy()
orig_map = _map.copy()

while True:
    start, direction, cont, _map = traverse_direction(_map, start, direction)
    if not cont:
        break

print(''.join(_map).count("X"))

try_positions = []
for i in range(len(_map)):
    for j in range(len(_map[0])):
        if _map[i][j] == 'X':
            try_positions.append([i,j])


print(len(try_positions))

up = [-1, 0]

cnt = 0
for i in try_positions:
    if i == orig_start:
        continue
    _map = orig_map.copy()

    s = _map[i[0]]

    _map[i[0]] = s[:i[1]] + '#' + s[i[1] + 1:]
    
    posList = list()

    s = orig_start.copy()

    _dir = up.copy()

    while True:
        s, _dir, cont, _map = traverse_direction(_map, s, _dir)
        
        x = (tuple(s),tuple(_dir))
        #print(x)

        if not cont:
            print("no loop")
            break 

        if posList.count(x) > 2:
            print("loop")
            cnt += 1
            break
        
        posList.append(x)

print(cnt)
