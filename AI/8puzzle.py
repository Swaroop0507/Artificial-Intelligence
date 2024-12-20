from collections import deque

class Solution:
    def solve(self, board):
        # Convert board to a single tuple for easier manipulation and to store in the visited set
        start = tuple(sum(board, []))
        goal = (0, 1, 2, 3, 4, 5, 6, 7, 8)

        if start == goal:
            return 0

        # BFS setup
        queue = deque([(start, 0)])  # Queue holds (current_state, move_count)
        visited = {start}
        moves = {
            0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
            3: [0, 4, 6], 4: [1, 3, 5, 7], 5: [2, 4, 8],
            6: [3, 7], 7: [4, 6, 8], 8: [5, 7]
        }

        # Perform BFS
        while queue:
            current, moves_count = queue.popleft()
            zero_pos = current.index(0)

            for move in moves[zero_pos]:
                # Swap 0 with the adjacent number to create a new state
                new_state = list(current)
                new_state[zero_pos], new_state[move] = new_state[move], new_state[zero_pos]
                new_state = tuple(new_state)

                # Check if the goal is reached
                if new_state == goal:
                    return moves_count + 1

                # Add new state to the queue if not visited
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, moves_count + 1))

        return -1  # Return -1 if goal is not reachable

# Example usage
ob = Solution()
matrix = [
    [3, 1, 2],
    [4, 7, 5],
    [6, 8, 0]
]
print("NO OF MOVES==", ob.solve(matrix))
