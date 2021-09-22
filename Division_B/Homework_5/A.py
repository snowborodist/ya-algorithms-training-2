file = open("input.txt")
lines = file.readlines()
file.close()

n, q = map(int, lines[0].split())
array = [int(elem) for elem in lines[1].split()]

pref_sums = [0] * (n + 1)

for i in range(1, n + 1):
    pref_sums[i] = pref_sums[i - 1] + array[i - 1]

for j in range(2, q + 2):
    from_index, to_index = map(int, lines[j].split())
    print(pref_sums[to_index] - pref_sums[from_index - 1])
