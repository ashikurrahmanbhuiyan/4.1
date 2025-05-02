import heapq

class PuzzleState:
    def __init__(self, board, parent=None, move="", g=0):
        self.board = board  # 2D list representing the puzzle
        self.parent = parent  # Reference to the parent state
        self.move = move  # Move that led to this state
        self.g = g  # Cost to reach this state (number of moves)
        self.h = self.heuristic()  # Heuristic value (Manhattan Distance)
        self.f = self.g + self.h  # Total cost

    def __lt__(self, other):
        return self.f < other.f  # Comparison for priority queue

    def heuristic(self):
        """Calculates the Manhattan Distance heuristic."""
        distance = 0
        goal = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1)}
        for i in range(3):
            for j in range(3):
                val = self.board[i][j]
                if val and val in goal:  # Ignore empty tile (0)
                    goal_x, goal_y = goal[val]
                    distance += abs(i - goal_x) + abs(j - goal_y)
        return distance

    def get_neighbors(self):
        """Generates valid neighboring states."""
        neighbors = []
        x, y = next((i, j) for i in range(3) for j in range(3) if self.board[i][j] == 0)
        moves = [(0, 1, "Right"), (0, -1, "Left"), (1, 0, "Down"), (-1, 0, "Up")]
        
        for dx, dy, move in moves:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_board = [row[:] for row in self.board]
                new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
                neighbors.append(PuzzleState(new_board, self, move, self.g + 1))
        
        return neighbors

    def is_goal(self):
        """Checks if the current board state is the goal state."""
        return self.board == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def get_solution_path(self):
        """Backtracks to retrieve the solution path."""
        path, current = [], self
        while current.parent:
            path.append(current.move)
            current = current.parent
        return path[::-1]


def solve_puzzle(start_board):
    """Solves the 8-puzzle problem using A* search."""
    open_set = []  # Priority queue
    visited = set()
    start_state = PuzzleState(start_board)
    heapq.heappush(open_set, start_state)
    
    while open_set:
        current = heapq.heappop(open_set)
        if current.is_goal():
            return current.get_solution_path()
        
        visited.add(tuple(map(tuple, current.board)))
        for neighbor in current.get_neighbors():
            if tuple(map(tuple, neighbor.board)) not in visited:
                heapq.heappush(open_set, neighbor)
    
    return None  # No solution found

# Example usage
initial_board = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
solution = solve_puzzle(initial_board)
print("Solution Path:", solution)
