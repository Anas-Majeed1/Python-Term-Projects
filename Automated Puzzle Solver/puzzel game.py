from collections import deque
from copy import deepcopy
import heapq

def BFS():
 # Function to find the position of the blank tile (0)
 def find_blank_tile(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                return i, j  # Return the row and column of the blank tile

 # Function to check if a state is valid (within boundaries)
 def is_valid_move(x, y, n):
    return 0 <= x < n and 0 <= y < n

 # Function to generate possible moves from the current state
 def get_neighbors(state):
    moves = []
    blank_row, blank_col = find_blank_tile(state)
    directions = [
        (1, 0),   # Down
        (-1, 0),  # Up
        (0, 1),   # Right
        (0, -1)   # Left
    ]
    n = len(state)
    
    for dx, dy in directions:
        new_row, new_col = blank_row + dx, blank_col + dy
        if is_valid_move(new_row, new_col, n):
            # Create a copy of the state
            new_state = [row[:] for row in state]
            # Swap the blank tile with the adjacent tile
            new_state[blank_row][blank_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_row][blank_col]
            moves.append(new_state)
    return moves

 # Function to check if the current state is the goal state
 def is_goal_state(state, goal_state):
    return state == goal_state

 # BFS algorithm to solve the 8-puzzle problem
 def bfs(initial_state, goal_state):
    visited = set()
    queue = deque([(initial_state, [])])  # Each element is (state, path)
    
    while queue:
        current_state, path = queue.popleft()
        
        # Check if the current state is the goal
        if is_goal_state(current_state, goal_state):
            return path
        
        # Convert state to a tuple so it can be added to a set
        state_tuple = tuple(tuple(row) for row in current_state)
        if state_tuple not in visited:
            visited.add(state_tuple)
            
            # Generate all possible moves and add them to the queue
            for neighbor in get_neighbors(current_state):
                queue.append((neighbor, path + [neighbor]))
    
    return None  # Return None if no solution is found

 # Function to print the puzzle state
 def print_state(state):
    for row in state:
        print(" ".join(map(str, row)))
    print()

 # Main function
 if __name__ == "__main__":
    # Take input from the user
    print("Enter the initial state (3x3 grid, use 0 for the blank tile):")
    initial_state = []
    for _ in range(3):
        row = list(map(int, input().split()))
        initial_state.append(row)

    print("Enter the goal state (3x3 grid, use 0 for the blank tile):")
    goal_state = []
    for _ in range(3):
        row = list(map(int, input().split()))
        goal_state.append(row)
    
    # Solve the puzzle
    print("\nSolving the puzzle using BFS...\n")
    solution = bfs(initial_state, goal_state)
    
    # Display the result
    if solution:
        print("Steps to solve the puzzle:")
        for step, state in enumerate(solution):
            print(f"Step {step + 1}:")
            print_state(state)
    else:
        print("No solution found!")

   # Main()









        #####---------------------------

       
def DFS():
 class PuzzleGame:
    def __init__(self, start_state, goal_state):
        self.start_state = start_state
        self.goal_state = goal_state
        self.rows = len(start_state)
        self.cols = len(start_state[0])
        self.solution = []

    def is_solvable(self, state):
        # Flatten the puzzle and count inversions
        flat = [num for row in state for num in row if num != 0]
        inversions = sum(1 for i in range(len(flat)) for j in range(i + 1, len(flat)) if flat[i] > flat[j])
        if self.rows % 2 != 0:
            return inversions % 2 == 0
        zero_row = self.rows - self.find_zero(state)[0]
        return (inversions + zero_row) % 2 == 0

    def find_zero(self, state):
        for i, row in enumerate(state):
            if 0 in row:
                return i, row.index(0)

    def get_neighbors(self, state):
        i, j = self.find_zero(state)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighbors = []
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < self.rows and 0 <= nj < self.cols:
                new_state = deepcopy(state)
                new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
                neighbors.append(new_state)
        return neighbors

    def solve(self):
        if not self.is_solvable(self.start_state):
            return "This puzzle is not solvable."

        queue = [(self.start_state, [])] 
        visited = set()

        while queue:
            current_state, path = queue.pop(0)
            if current_state == self.goal_state:
                return path + [current_state]
            visited.add(self.serialize(current_state))
            for neighbor in self.get_neighbors(current_state):
                if self.serialize(neighbor) not in visited:
                    queue.append((neighbor, path + [current_state]))

        return "No solution found."

    def serialize(self, state):
        return tuple(tuple(row) for row in state)

 def get_user_input(rows, cols):
    print(f"Enter the {rows}x{cols} puzzle row by row (use 0 for the empty space):")
    state = []
    for i in range(rows):
        while True:
            try:
                row = list(map(int, input(f"Row {i + 1}: ").split()))
                if len(row) != cols:
                    raise ValueError
                state.append(row)
                break
            except ValueError:
                print(f"Invalid input! Enter exactly {cols} numbers.")
    return state

 def print_solution(solution):
    if isinstance(solution, str):
        print(solution)
    else:
        for step, state in enumerate(solution):
            print(f"Step {step}:")
            for row in state:
                print(" ".join(map(str, row)))
            print()

 # Main function
 rows, cols = 3, 3  # For a 3x3 puzzle
 goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
 ]

 print("Enter the start state:")
 start_state = get_user_input(rows, cols)

 assert len(start_state) == rows and all(len(row) == cols for row in start_state), "Invalid puzzle dimensions!"

 game = PuzzleGame(start_state, goal_state)
 solution = game.solve()

 print("\nSolution Steps:")
 print_solution(solution)
 #Main()






 ####----------------------------------------


def A():
 #  Converting the input into grid
 def parse_input(prompt, size):
    print(prompt)
    grid = []
    for _ in range(size):
        row = list(map(int, input().split()))
        grid.append(row)
    return grid

 # Function to find the position of the empty space (0)
 def find_zero(grid):
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == 0:
                return i, j
    raise ValueError("The input grid does not contain a 0 (empty space). Please check your input.")

 # Manhattan distance heuristic
 def manhattan_distance(state, goal):
    size = len(state)
    distance = 0
    for i in range(size):
        for j in range(size):
            val = state[i][j]
            if val != 0:  # Skip the empty space
                for x in range(size):
                    for y in range(size):
                        if goal[x][y] == val:
                            distance += abs(i - x) + abs(j - y)
    return distance

 # Function to generate all possible moves
 def get_neighbors(state, zero_pos):
    neighbors = []
    x, y = zero_pos
    size = len(state)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < size and 0 <= ny < size:
            # Swap zero with the neighbor
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append((new_state, (nx, ny)))
    return neighbors

 # A* algorithm
 def a_star(initial, goal):
    size = len(initial)
    zero_pos = find_zero(initial)  # Ensure zero is found
    open_set = []
    heapq.heappush(open_set, (0, initial, zero_pos, []))  # (priority, state, zero_pos, path)
    visited = set()
    
    while open_set:
        _, current, zero_pos, path = heapq.heappop(open_set)
        
        if current == goal:
            return path
        
        visited.add(tuple(map(tuple, current)))
        for neighbor, new_zero_pos in get_neighbors(current, zero_pos):
            if tuple(map(tuple, neighbor)) not in visited:
                new_path = path + [neighbor]
                cost = len(new_path) + manhattan_distance(neighbor, goal)
                heapq.heappush(open_set, (cost, neighbor, new_zero_pos, new_path))
    return None

 # Main program
 def main():
    size = 3  # Fixed to 3x3 for the 8-puzzle
    
    initial_state = parse_input(f"Enter the initial state as {size}x{size} grid (row by row) (for Empty space enter Zero):", size)
    goal_state = parse_input(f"Enter the goal state as {size}x{size} grid (row by row)  (for Empty space enter Zero):", size)
    
    print("\nSolving the puzzle...")
    try:
        solution = a_star(initial_state, goal_state)
        if solution is None:
            print("No solution found!")
        else:
            print(f"Minimum moves required: {len(solution)}")
            print("Steps:")
            for step in solution:
                for row in step:
                    print(" ".join(map(str, row)))
                print()
    except ValueError as e:
        print(f"Error: {e}")

 if __name__ == "__main__":
    main()





def Main():
    print("Select one from the following to execute:")
    print("1:Breath First Search")
    print("2:Depth First Search")
    print("3:A*")



    n=int(input("Enter the choice from 1 to 3:"))
    if n==1:
        BFS()

    elif n==2:
        DFS()
        
    elif n==3:
        A()
   
    else:
        print("Invalid Choice.")


Main()












