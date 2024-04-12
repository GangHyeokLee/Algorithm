import sys
input = sys.stdin.readline

for _ in range(int(input())):
  # 지원자 성적 받고
  candi = [list(map(int, input().split())) for _ in range(int(input()))]
  # 서류 성적 기준으로 정렬하기
  candi.sort()
  # 서류 1등의 면접 성적
  doc1int = candi[0][1]
  
  hap = 0
  # 돌면서 서류 1등의 면접 성적보다 낮은 사람은 다 나가
  for i in candi:
    if i[1] <= doc1int:
      hap += 1
      doc1int = i[1]
  print(hap)
        
  