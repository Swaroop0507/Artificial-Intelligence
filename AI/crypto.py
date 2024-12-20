def find_value(word, assigned):
    return int("".join(str(assigned[char]) for char in word))

def is_valid(word1, word2, result, assigned):
    # First letter can't be zero
    return assigned[word1[0]] != 0 and assigned[word2[0]] != 0 and assigned[result[0]] != 0

def solve(word1, word2, result):
    letters = list(set(word1 + word2 + result))
    if len(letters) > 10:
        print("No solutions found.")
        return

    from itertools import permutations
    for perm in permutations(range(10), len(letters)):
        assigned = dict(zip(letters, perm))
        if is_valid(word1, word2, result, assigned):
            num1, num2, num_result = find_value(word1, assigned), find_value(word2, assigned), find_value(result, assigned)
            if num1 + num2 == num_result:
                print(f"Solution: {num1} + {num2} = {num_result} | Assignments: {assigned}")
                return
    print("No solutions found.")

# Main part of the program
print("CRYPTARITHMETIC PUZZLE SOLVER")
word1 = input("Enter WORD1: ").upper()
word2 = input("Enter WORD2: ").upper()
result = input("Enter RESULT: ").upper()

solve(word1, word2, result)
