def solution(users, emoticons):
    answer = []
    
    # 구매 시키려면 최소 비율이상은 할인 해야함
    # 구매 시켰을 때 가격 넘으면 임티플 구매함   
            
    sold = [0] * len(users) + [0] # 유저들에게 판 금액 + 임티플 가입자수
    ans = []
    dfs(0, sold, users, emoticons, ans)
    
    ans.sort(reverse=True) 
    
    return [ans[0][0], int(ans[0][1])]

def dfs(start, sold, users, emoticons, ans):
    
    if start == len(emoticons):
        for idx in range(len(sold)-1):
            if users[idx][1] <= sold[idx]:
                sold[-1] += 1
                sold[idx] = 0
        ans.append([sold[-1], sum(sold[:-1])])
    else:
        for d in [10, 20, 30, 40]:
            tmp = sold[:]
            for idx, u in enumerate(users):
                if u[0] <= d:
                    tmp[idx] += emoticons[start] * (100 - d) / 100
            
            dfs(start + 1, tmp, users, emoticons, ans)
    
    
    
    