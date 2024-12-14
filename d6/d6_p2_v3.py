with open('input') as f:
    _input = f.read()

_map = _input.split('\n')
del _map[-1]

_map = {r+c*1j:_map[r][c] for r in range(len(_map)) for c in range(len(_map[0]))}
orig_map = _map.copy()

start = list(filter(lambda x: _map[x] == '^', _map))[0]

bounds = (max([k.real for k in _map]), max([k.imag for k in _map]))

print(bounds)

_dir = 1 + 0j
def traverse(start, direction, _map, visited = [], bounds = bounds):
    while True:
        _next = start + direction
        
        if (start, direction) in visited:
            return False, visited
        
        visited.append((start, direction))
        
        if _next.real < 0 or _next.imag < 0 or _next.real > bounds[0] or _next.imag > bounds[1]:
            return True, visited
 
        if _map[_next] == '#':
            direction =  direction*-1j
        else:
            direction = direction 
            start = _next

exited, visited = traverse(start, -1+0j, _map)

_visited = []
for i in visited:
    if i[0] in _visited:
        continue
    _visited.append(i[0])

print(exited)
print(len(_visited))
orig_start = start
cnt = 0
l = 0
for i in _visited:
    if i == orig_start:
        continue

    _map = orig_map.copy()
    _map[i] = '#'

    e, v = traverse(start, _dir, _map, [])
    if e: 
        print(l, 'no loop')
    else:
        print(l, 'loop')
        cnt += 1
    start = i
    _dir = v[-1][1]
    l += 1

print(cnt)

