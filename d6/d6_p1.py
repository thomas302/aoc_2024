with open('input', 'r+') as f:
    _input = f.read()

_map = _input.split('\n')

print(_map)

input()

def get_start(_map: list)->tuple:
    for l in range(len(_input)):
        line = _map[l]
        c = line.find('^')
        if not c ==-1:
            return [l, c]

start = get_start(_map)
print(start)

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
            return [pos[0]-direction[0], pos[1]-direction[1]], direction, False, _map
            
        pos[0] += direction[0]
        pos[1] += direction[1]

direction = [-1, 0]
c = 0
while True:
    start, direction, cont, _map = traverse_direction(_map, start, direction)
    if not cont:
        break

print(''.join(_map).count('X'))
_map
