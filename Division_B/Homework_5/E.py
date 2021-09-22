s = int(input())

a_raw = [(int(num), index) for index, num in enumerate(input().split())]
a_len = a_raw[0][0]
a = sorted(a_raw[1:])

b_raw = [(int(num), index) for index, num in enumerate(input().split())]
b_len = b_raw[0][0]
b = sorted(b_raw[1:])

c_raw = [(int(num), index) for index, num in enumerate(input().split())]
c_len = c_raw[0][0]
c = sorted(c_raw[1:])

pref_sum = [0] * (a_len + b_len + c_len)

a_i = 0
b_i = 0
c_i = 0

while (a_i < a_len) or (b_i < b_len) or (c_i < c_len):
    pass