# 2163	 초콜릿 자르기
n, m = map(int, input().split())
print(n * m -1)

# 11021	 A+B - 7
T = int(input())

for i in range (1, T+1):
    a, b = map(int, input().split())
    print("Case #"+str(i)+":", a + b)
    
# 11022	 A+B - 8
T = int(input())

for i in range(1, T+1):
    a, b = map(int, input().split())
    print("Case #"+str(i)+":", a,"+",b,"=", a+b)

# 다른 풀이 11022	 A+B - 8
T = int(input())

for i in range(1, T+1):
    a, b = map(int, input().split())
    print(f"Case #{i}: {a} + {b} = {a+b}")
    
# 10699	 오늘 날짜
from datetime import date
print(date.today())

# 7287	 등록
print(15)
print('mudosaa')

# 2525	 오븐 시계
a, b = map(int, input().split())
c = int(input())

a+= c // 60
b+= c % 60

if b >= 60:
    a+=1
    b-=60

if a >= 24:
    a-=24

print(a, b)

# 2530	 인공지능 시계
a, b, c = map(int, input().split())
d = int(input())

c += d
b += c // 60
a+= b // 60

c%=60
b%=60
a%=24

print(a,b,c)

# 2914	 저작권
a, i = map(int, input().split())
print(a*(i-1)+1)

# 5355	 화성 수학
t = int(input())

for _ in range(t):
    a = list(map(str, input().split()))
    answer = 0
    
    for i in range(len(a)):
        if i == 0:
            answer+= float(a[i])
        else:
            if a[i] == '@':
                answer*=3
            elif a[i] == '%':
                answer+=5
            elif a[i] == '#':
                answer-=7

    print("%0.2f" % answer)
    
# 2675	 문자열 반복
t = int(input())

for i in range(t):
    r, s = input().split()
    r = int(r)
    s = str(s)

    for i in range(len(s)):
        print(r*s[i], end='')

    print()
    
# 2935	 소음
a = int(input())
math = input()
b = int(input())

if math == "+":
    print(a+b)
if math == "*":
    print(a*b)
