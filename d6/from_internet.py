with open("input") as f:
  rows = [line.strip() for line in f.read().strip().split("\n")]

width, height = len(rows[0]), len(rows)
sx, sy = next((x, y) for y, row in enumerate(rows) for x, c in enumerate(row) if c in "<>v^")

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

direction_map = {
  ">": (1, 0),
  "<": (-1, 0),
  "^": (0, -1),
  "v": (0, 1)
}

def get_jump_location(x, y, dindex):
  if rows[y][x] == "#":
    return None
  
  dx, dy = directions[dindex]
  while x >= 0 and y >= 0 and x < width and y < height and rows[y][x] != "#":
    x += dx
    y += dy
  
  if x < 0 or y < 0 or x >= width or y >= height:
    return (x, y, None)
  
  x -= dx
  y -= dy
  dindex = (dindex + 1) % 4
  return (x, y, dindex)

jump_map = {(x, y, di): get_jump_location(x, y, di) for x in range(width) for y in range(height) for di in range(len(directions))}

def jump_into_block(dindex, block_patch):
  dx, dy = directions[dindex]
  bx, by = block_patch
  return (bx - dx, by - dy, (dindex + 1) % 4)

def jump(x, y, dindex, block_patch):
  dest = jump_map[x, y, dindex]
  if block_patch is not None and dest is not None:
    fx, fy, _ = dest
    bx, by = block_patch
    if fx == bx and min(y, fy) <= by <= max(y, fy):
      return jump_into_block(dindex, block_patch)
    elif min(x, fx) <= bx <= max(x, fx) and fy == by:
      return jump_into_block(dindex, block_patch) 
  return dest


def get_full_path():
  x, y = sx, sy

  visited = set()
  dindex = directions.index(direction_map[rows[y][x]])

  step = 0
  while True:
    visited.add((x, y))

    dx, dy = directions[dindex]
    x, y = x + dx, y + dy
    step += 1
    if x < 0 or y < 0 or x >= width or y >= height:
      break
    elif rows[y][x] == "#":
      x, y = x - dx, y - dy
      dindex = (dindex + 1) % len(directions)
  
  return visited

def path_loops_with_patch(block_patch):
  x, y = sx, sy, 
  dindex = directions.index(direction_map[rows[y][x]])

  visited = set()

  while True:
    x, y, dindex = jump(x, y, dindex, block_patch)
    if dindex is None:
      return False

    if (x, y, dindex) in visited:
      return True
    
    visited.add((x, y, dindex))

path = get_full_path()
print(len(path))

loop_positions = 0
test_list = []
for block in path:
  if block != (sx, sy) and path_loops_with_patch(block):
    test_list.append(True)
    loop_positions += 1
  else: test_list.append(False)
  
print(loop_positions)
print(len(test_list))



with open('input', 'r+') as f:
    _input = f.read()

_map = _input.split('\n')


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

orig_start = start

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

orig_map = _map.copy()

print(len(try_positions))
input()

direction = [-1, 0]

cnt = 0
list_2 = []
for i in try_positions:
    _map = orig_map.copy()

    s = _map[i[0]]

    _map[i[0]] = s[:i[1]] + '#' + s[i[1] + 1:]

    posList = list()

    s = orig_start

    _dir = direction

    while True:
        s, _dir, cont, _map = traverse_direction(_map, s, _dir)
        
        x = (tuple(s),tuple(_dir))
        #print(x)

        if not cont:
            list_2.append(False)
            break 

        if x in posList:
            #print("loop")
            list_2.append(True)
            cnt += 1
            break
        
        posList.append(x)

        

print(cnt)
print(len(list_2))

c = 0 
for i, j in zip(list_2, test_list):
    print(i,j)
    print(c)

    c +=1
