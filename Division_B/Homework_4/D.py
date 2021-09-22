votes_counts = {}
seats = 450
votes_total = 0

# TODO: RENAME FILE TO INPUT.TXT!!!
with open("input_D.txt") as file:
    for line in file:
        votes_text = line.split()[-1]
        party_name = line.replace(f" {votes_text}", "").strip()
        votes = int(votes_text)
        votes_total += votes
        votes_counts[party_name] = votes

stats = {}
first_election_val = votes_total / seats
seats_left = seats

for party_name, party_votes in votes_counts.items():
    party_seats = int(party_votes / first_election_val)
    party_residue = (party_votes / first_election_val) - party_seats
    stats[(party_residue, party_votes, party_name)] = party_seats
    seats_left -= party_seats

for key in sorted(stats.keys(), reverse=True):
    data = stats[key]
    if seats_left > 0:
        votes_counts[key[2]] = data + 1
        seats_left -= 1
    else:
        votes_counts[key[2]] = data

for name, count in votes_counts.items():
    print(f"{name} {count}")
