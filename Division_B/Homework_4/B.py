election_results = {}

with open("input.txt") as file:
    for line in file:
        candidate, votes = line.strip().split()
        if candidate in election_results:
            election_results[candidate] += int(votes)
        else:
            election_results[candidate] = int(votes)

for candidate, votes in sorted(election_results.items()):
    print(f"{candidate} {votes}")
