import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position  # (row, col)
        self.parent = parent
        self.g = 0  # Cost from start to node
        self.h = 0  # Heuristic cost to goal
        self.f = 0  # Total cost

    def __lt__(self, other):
        return self.f < other.f  # for heapq to sort nodes

def heuristic(a, b):
    # Manhattan Distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, end):
    start_node = Node(start)
    end_node = Node(end)

    open_list = []
    closed_set = set()

    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_set.add(current_node.position)

        # Goal check
        if current_node.position == end_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # reversed path

        # 4-directional movement
        for d in [(0,1), (1,0), (0,-1), (-1,0)]:
            neighbor_pos = (current_node.position[0] + d[0],
                            current_node.position[1] + d[1])

            # Check boundaries and obstacles
            if (0 <= neighbor_pos[0] < len(grid) and
                0 <= neighbor_pos[1] < len(grid[0]) and
                grid[neighbor_pos[0]][neighbor_pos[1]] == 0 and
                neighbor_pos not in closed_set):

                neighbor = Node(neighbor_pos, current_node)
                neighbor.g = current_node.g + 1
                neighbor.h = heuristic(neighbor.position, end_node.position)
                neighbor.f = neighbor.g + neighbor.h

                # If already in open list with lower f, skip
                if any(n.position == neighbor.position and n.f <= neighbor.f for n in open_list):
                    continue

                heapq.heappush(open_list, neighbor)

    return None  # No path found

