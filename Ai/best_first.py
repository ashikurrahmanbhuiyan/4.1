import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.h = 0  # Heuristic (distance to goal)

    def __lt__(self, other):
        return self.h < other.h  # Priority queue uses h(n)

def heuristic(a, b):
    # Manhattan Distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def best_first_search(grid, start, end):
    start_node = Node(start)
    end_node = Node(end)

    open_list = []
    closed_set = set()

    start_node.h = heuristic(start, end)
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_set.add(current_node.position)

        # Goal check
        if current_node.position == end:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        # Explore neighbors (up, down, left, right)
        for d in [(0,1), (1,0), (0,-1), (-1,0)]:
            neighbor_pos = (current_node.position[0] + d[0],
                            current_node.position[1] + d[1])

            if (0 <= neighbor_pos[0] < len(grid) and
                0 <= neighbor_pos[1] < len(grid[0]) and
                grid[neighbor_pos[0]][neighbor_pos[1]] == 0 and
                neighbor_pos not in closed_set):

                neighbor = Node(neighbor_pos, current_node)
                neighbor.h = heuristic(neighbor_pos, end)
                
                # If already in open list with better or equal h, skip
                if any(n.position == neighbor.position and n.h <= neighbor.h for n in open_list):
                    continue

                heapq.heappush(open_list, neighbor)

    return None  # No path found

