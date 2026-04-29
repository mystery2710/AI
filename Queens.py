# N-Queens Problem

def solve_n_queens(n):
    col_used = [False] * n
    diag1_used = [False] * (2 * n - 1)
    diag2_used = [False] * (2 * n - 1)

    queens = [-1] * n
    solutions = []

    def is_safe(row, col):
        return (
            not col_used[col]
            and not diag1_used[row - col + n - 1]
            and not diag2_used[row + col]
        )

    def place(row, col):
        queens[row] = col
        col_used[col] = True
        diag1_used[row - col + n - 1] = True
        diag2_used[row + col] = True

    def remove(row, col):
        queens[row] = -1
        col_used[col] = False
        diag1_used[row - col + n - 1] = False
        diag2_used[row + col] = False

    def backtrack(row):
        if row == n:
            solutions.append(queens[:])
            return

        for col in range(n):
            if is_safe(row, col):
                place(row, col)
                backtrack(row + 1)
                remove(row, col)

    backtrack(0)
    return solutions

def print_board(queens, n):
    border = "+" + ("---+" * n)
    print(border)
    for row in range(n):
        row_str = "|"
        for col in range(n):
            row_str += " Q |" if queens[row] == col else " . |"
        print(row_str)
        print(border)

def main():
    n = int(input("Enter value of N: "))
    solutions = solve_n_queens(n)

    if not solutions:
        print(f"No solution exists for N = {n}")
        return

    total = len(solutions)
    print(f"\nTotal solutions found: {total}\n")

    for i in range(total):
        print(f"\n--- Solution {i + 1} ---")
        print("Queen positions:", solutions[i])
        print_board(solutions[i], n)

if __name__ == "__main__":
    main()