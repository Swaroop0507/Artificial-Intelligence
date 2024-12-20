from queue import PriorityQueue

def find_transformation_path(start, goal):
    if sorted(start) != sorted(goal):
        return "Goal is not possible!"

    # Priority queue for storing steps with estimated cost
    queue = PriorityQueue()
    queue.put((0, start, [start]))  # Initial cost, starting string, path
    visited = set([start])          # Track visited strings

    while not queue.empty():
        _, current, path = queue.get()

        # Check if we have reached the goal
        if current == goal:
            return path

        # Generate all adjacent swaps
        for i in range(len(current) - 1):
            # Swap adjacent characters
            swapped = current[:i] + current[i + 1] + current[i] + current[i + 2:]
            if swapped not in visited:
                visited.add(swapped)
                # Queue with priority based on matching characters
                cost = sum(1 for a, b in zip(swapped, goal) if a != b)
                queue.put((cost, swapped, path + [swapped]))

    return "Goal is not possible!"

# Example usage
if __name__ == "__main__":
    start_string = "secure"
    goal_string = "rescue"
    print("Starting...")
    path = find_transformation_path(start_string, goal_string)
    if isinstance(path, list):
        for step, state in enumerate(path):
            print(f"{step}) {state}")
    else:
        print(path)
