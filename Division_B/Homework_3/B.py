sequence = [int(num) for num in input().split()]

uniques = set()
for num in sequence:
    if num not in uniques:
        print("NO")
        uniques.add(num)
    else:
        print("YES")
