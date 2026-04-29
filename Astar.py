# A* Algorithm - 8 Puzzle Problem
# Goal State: 1 2 3 / 4 5 6 / 7 8 0  (0 = blank)

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
        0: [1, 3],    1: [0, 2, 4],    2: [1, 5],
        3: [0, 4, 6], 4: [1, 3, 5, 7], 5: [2, 4, 8],
        6: [3, 7],    7: [4, 6, 8],    8: [5, 7]
    }

    for move in moves[blank]:
        new_state = state[:]
        new_state[blank], new_state[move] = new_state[move], new_state[blank]
        neighbors.append(tuple(new_state))

    return neighbors

def get_move_direction(prev, curr):
    # Find which direction the blank moved
    blank_prev = list(prev).index(0)
    blank_curr = list(curr).index(0)
    diff = blank_curr - blank_prev
    if diff == -3: return "UP    (blank moved up)"
    if diff ==  3: return "DOWN  (blank moved down)"
    if diff == -1: return "LEFT  (blank moved left)"
    if diff ==  1: return "RIGHT (blank moved right)"
    return "Unknown"

def get_moved_tile(prev, curr):
    # Find which tile was slid into the blank
    blank_prev = list(prev).index(0)
    return curr[blank_prev]   # tile that came into old blank spot

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

# ── Take Input from User ──────────────────────────────────
print("Enter the start state row by row.")
print("Use 0 for the blank tile. Example: 1 2 3")
print()

tiles = []
for i in range(3):
    row = input(f"Row {i+1}: ").split()
    tiles.extend([int(x) for x in row])

start = tuple(tiles)

print("\nStart State:")
print_state(start)
print("Goal State:")
print_state(GOAL)

print(f"\nMisplaced tiles in start state : {heuristic(start)}")
print(f"(This is the initial h value — how far we are from goal)\n")

path = astar(start)

if path:
    total_moves = len(path) - 1
    print(f"Solution found in {total_moves} moves!\n")
    print("=" * 30)

    for step, state in enumerate(path):
        g = step                        # cost so far
        h = heuristic(state)            # misplaced tiles
        f = g + h                       # total estimated cost

        print(f"\nStep {step}:")

        if step == 0:
            print(f"  >> This is the START state.")
        else:
            prev = path[step - 1]
            direction  = get_move_direction(prev, state)
            moved_tile = get_moved_tile(prev, state)
            print(f"  >> Move : {direction}")
            print(f"  >> Tile {moved_tile} was slid into the blank space.")

        print(f"  >> g(n) = {g}  (moves made so far)")
        print(f"  >> h(n) = {h}  (misplaced tiles remaining)")
        print(f"  >> f(n) = {f}  (g + h = total estimated cost)")

        if h == 0:
            print(f"  >> h = 0 means we reached the GOAL STATE!")

        print_state(state)
        print("-" * 30)

else:
    print("No solution found!")
