list_1 = [int(num) for num in input().split()]
list_2 = [int(num) for num in input().split()]

print(len(set(list_1).intersection(set(list_2))))
