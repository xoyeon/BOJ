# 1	2750	 수 정렬하기
n = int(input())

num=[]
for i in range(n):
    num.append(int(input()))
num_sort = sorted(num)

for i in range(len(num)):
               print(num_sort[i])
    
# 2	2751	 수 정렬하기 2
# 3	10989	 수 정렬하기 3
# 4	2108	 통계학
# 5	1427	 소트인사이드
# 6	11650	 좌표 정렬하기
# 7	11651	 좌표 정렬하기 2
# 8	1181	 단어 정렬
# 9	10814	 나이순 정렬
n = int(input())

mem =[]
for i in range(n):
  age, name = map(str, input().split())
  age = int(age)
  mem.append((age, name))

mem.sort(key = lambda a: a[0])

for i in mem:
  print(i[0], i[1])

# 10	18870	 좌표 압축
