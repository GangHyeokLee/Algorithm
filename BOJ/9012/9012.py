lines = int(input())

for i in range(lines):
    bracket = input()
    check = 0
    for j in bracket:
        if j=='(':
            check+=1
        else:
            check-=1
        if check<0:
            break
    if check == 0:
        print("YES")
    else:
        print("NO")
