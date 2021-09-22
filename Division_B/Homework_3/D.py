max_guessed_num = 0
# probable_solutions = set([str(num) for num in range(1, max_guessed_num + 1)])
probable_solutions = set()
wrong_solutions = set()
# should_continue = True

file = open('input.txt')
first_line = True
for line in file:
    if first_line:
        max_guessed_num = int(line.strip())
        first_line = False
# while should_continue:

    next_input = line.strip()
    if next_input == 'HELP':
        # should_continue = False
        break
    else:
        nums = set([int(num) for num in next_input.split()])

        next_input = input()
        if next_input == 'YES':
            if len(probable_solutions) == 0:
                probable_solutions  = nums
            else:
                probable_solutions = probable_solutions.intersection(nums)
        elif next_input == 'NO':
            wrong_solutions = wrong_solutions.union(nums)
            probable_solutions = probable_solutions.difference(nums)
print("AAAAAAAAAAAAA")
if len(probable_solutions) != 0:
    print(' '.join([str(elem) for elem in sorted(list(probable_solutions))]))
else:
    nums = []
    for i in range(1, max_guessed_num + 1):
        if i not in wrong_solutions:
            nums.append(i)
    print(' '.join([str(elem) for elem in nums]))
