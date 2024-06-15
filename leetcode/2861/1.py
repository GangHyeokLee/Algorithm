class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        # 만들 수 있는 합금의 최대값
        # 기계를 선택하면 결과는 알아서 나옴

        # 개수를 기준으로 budget을 넘지않은 채로 합금 만들 수 있는 기계를 찾아야하나?
        # binary search 100번
        answer = 0


        for c in composition:
            tmp = 0
            start = 0
            end = 1000000000

            while start <= end:
                mid = (start + end) // 2

                over = createAlloy(c, stock, cost, mid)
                print(c, mid, over)

                if over > budget:
                    end = mid - 1
                else:
                    tmp = mid
                    start = mid + 1
            print(c, tmp)
            answer = max(answer, tmp)
        return answer
            

            

def createAlloy(machine, stock, cost, order):
    totalcost = 0
    
    for i in range(len(machine)):
        # 추가 구매 비용은 이만큼
        if stock[i] < machine[i] * order:
            totalcost += cost[i] * (machine[i] * order - stock[i])

    return totalcost