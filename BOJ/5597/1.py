st = [0] * 31

for i in range(28):
    st[int(input())] = 1

for i in range(1, 31):
    if st[i] == 0:
        print(i)