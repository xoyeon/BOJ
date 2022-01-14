# 1	15596	 정수 N개의 합
def solve(a):
    return sum(a)
  
# 2	4673	 셀프 넘버
num = set(range(1, 10001))
new = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    new.add(i)

self = sorted(num - new)
for i in self:
    print(i)
    
# 3	1065	 한수
n= int(input())

hansu = 0
for i in range(1, n+1):
    num = list(map(int, str(i)))
    if i < 100:
        hansu += 1
    elif num[0]-num[1] == num[1]-num[2]:
        hansu +=1

print(hansu)
