num_witnesses = int(input())
witness_sets = []
for _ in range(num_witnesses):
    witness_sets.append(set(input()))

num_suspects = int(input())
max_witness_suspects = []
max_witness_match = 0
for _ in range(num_suspects):
    suspect = input()
    suspect_set = set(suspect)
    match_count = 0
    for witness_set in witness_sets:
        if witness_set.issubset(suspect_set):
            match_count += 1
    if match_count > max_witness_match:
        max_witness_match = match_count
        max_witness_suspects = [suspect]
    elif match_count == max_witness_match:
        max_witness_suspects.append(suspect)

print('\n'.join(max_witness_suspects))
