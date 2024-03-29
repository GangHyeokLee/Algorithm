n = int(input())
score = list(map(int, input().split()))
print(sum(score)/(n * max(score)) * 100)