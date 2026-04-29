import heapq

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def heuristic(state):
    count = 0
    for i in range(9):
        if state[i] != 0 and state[i] != GOAL[i]:
            count += 1
    return count

def get_neighbors(state):
    neighbors = []
    state = list(state)
    blank = state.index(0)

    moves = {
        0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
        3: [0, 4, 6], 4: [1, 3, 5, 7], 5: [2, 4, 8],
        6: [3, 7], 7: [4, 6, 8], 8: [5, 7]
    }

    for move in moves[blank]:
        new_state = state[:]
        new_state[blank], new_state[move] = new_state[move], new_state[blank]
        neighbors.append(tuple(new_state))

    return neighbors

def get_move_direction(prev, curr):
    blank_prev = list(prev).index(0)
    blank_curr = list(curr).index(0)
    diff = blank_curr - blank_prev
    if diff == -3: return "UP"
    if diff == 3: return "DOWN"
    if diff == -1: return "LEFT"
    if diff == 1: return "RIGHT"
    return "Unknown"

def get_moved_tile(prev, curr):
    blank_prev = list(prev).index(0)
    return curr[blank_prev]

def astar(start):
    heap = [(heuristic(start), 0, start, [])]
    visited = set()

    while heap:
        f, g, state, path = heapq.heappop(heap)

        if state in visited:
            continue
        visited.add(state)
        path = path + [state]

        if state == GOAL:
            return path

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(neighbor)
                heapq.heappush(heap, (new_f, new_g, neighbor, path))

    return None

def print_state(state):
    print("+-------+")
    for i in range(3):
        row = state[i*3 : i*3+3]
        print("|", ' '.join(str(x) if x != 0 else '_' for x in row), "|")
    print("+-------+")

tiles = []
for i in range(3):
    row = input().split()
    tiles.extend([int(x) for x in row])

start = tuple(tiles)

print_state(start)
print_state(GOAL)

path = astar(start)

if path:
    for step, state in enumerate(path):
        g = step
        h = heuristic(state)
        f = g + h

        print(f"Step {step}")
        print(f"g={g}, h={h}, f={f}")

        if step > 0:
            prev = path[step - 1]
            print(get_move_direction(prev, state))
            print(get_moved_tile(prev, state))

        print_state(state)
else:
    print("No solution found")
