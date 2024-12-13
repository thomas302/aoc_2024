import pprint as pp
_input='''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''

_map = _input.split('\n')

def get_start(_map: list)->tuple:
    for l in range(len(_input)):
        line = _map[l]
        c = line.find('^')
        if not c ==-1:
            return [l, c]

def traverse_direction(_map, start, direction):
    pos = start
    while True:
        if pos[0] < len(_map) and pos[1] < len(_map[0]) and pos[0] >= 0 and pos[1] >= 0:
            current_val = _map[pos[0]][pos[1]]
            if current_val == '#':
                return [pos[0]-direction[0], pos[1]-direction[1]], [direction[1], -direction[0]], True, _map
            else:
                pass
                #s = _map[pos[0]] 
                #_map[pos[0]] = s[:pos[1]] + 'X' + s[pos[1] + 1:]
        else:
            return [pos[0]-direction[0], pos[1]-direction[1]], direction, False, _map
            
        pos[0] += direction[0]
        pos[1] += direction[1]

direction = [-1, 0]
start = get_start(_map)
_map_og = _map.copy()

map_list = []
for row in range(len(_map)):
    for col in range(len(_map)):
        if [row, col] == start:
            continue
        
        _map = _map_og.copy()

        if _map[row][col] == '#':
            continue

        s = _map[row]
        _map[row] = s[:col] + '#' + s[col + 1:]

        map_list.append(_map)

pp.pp(map_list[88])

print(len(map_list))
l = 0
c = 0
for _map in map_list:
    turning_points = []
    print(c)
    c+=1
    while True:
        s, direction, cont, _map = traverse_direction(_map, start, direction)
        if not cont:
            break
        turning_points.append(s)
        
        
print('--------')
print(l)
