# 1	2739	 구구단
n = int(input())

for i in range (1, 10):
    print(n,'*',i,'=',n*i)
    
# 2	10950	 A+B - 3
t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    print(a+b)
    
# 3	8393	 합
n = int(input())
sum = 0

for i in range(n+1):
    sum = sum+i
print(sum)

# 4	15552	 빠른 A+B
import sys

input = sys.stdin.readline
t=int(input())

for i in range(t):
    a, b = map(int, input().split())
    print(a+b)
    
# 5	2741	 N 찍기
n = int(input())

for i in range(1,n+1):
    print(i)

# 6	2742	 기찍 N
n = int(input())

for i in range (n, 0, -1):
    print(i)
    
# 7	11021	 A+B - 7
T = int(input())

for i in range (1, T+1):
    a, b = map(int, input().split())
    print("Case #"+str(i)+":", a + b)

# 8	11022	 A+B - 8
T = int(input())

for i in range(1, T+1):
    a, b = map(int, input().split())
    print(f"Case #{i}: {a} + {b} = {a+b}")

# 9	2438	 별 찍기 - 1
n = int(input())

for i in range(1, n+1):
    print("*"*i)

# 10	2439	 별 찍기 - 2
n = int(input())

for i in range(1, n+1):
    print(" "*(n-i)+"*"*i)

# 11	10871	 X보다 작은 수
n, x = map(int, input().split())
a = list(map(int, input().split()))

for i in range(n):
    if a[i] < x:
        print(a[i])
