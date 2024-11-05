def solution(enroll, referral, seller, amount):
    rev = [0] * len(enroll)
    
    enum = dict()
    for i, e in enumerate(enroll):
        enum[e] = i
    
    for idx, s in enumerate(seller):
        money = amount[idx] * 100
        while s != "-" and money > 0:
            i = enum[s]
            rev[i] += money - money//10
            money //= 10
            s = referral[i]
    
    return rev