# 1	1330	 두 수 비교하기
a, b = map(int, input().split())

if a>b:
    print(">")
elif a<b:
    print("<")
else:
    print("==")
    
# 2	9498	 시험 성적
score = int(input())

if score >=90:
    print('A')
elif score >=80:
    print('B')
elif score >=70:
    print('C')
elif score >=60:
    print('D')
else:
    print('F')

# 3	2753	 윤년
year = int(input())

if (year%4==0 and year%100!=0) or year%400==0:
    print(1)
else:
    print(0)

# 4	14681	 사분면 고르기
x = int(input())
y = int(input())

if x>0 and y>0:
    print(1)
elif x<0 and y>0:
    print(2)
elif x<0 and y<0:
    print(3)
else:
    print(4)
    
# 5	2884	 알람 시계
h, m = map(int, input().split())

if m>44:
    print(h, m-45)
elif m<45 and h>0:
    print(h-1, m+15)
else:
    print(23, m+15)
    
# 6	2525	 오븐 시계
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

# 7	2480	 주사위 세개
a, b, c = map(int, input().split())

if a == b == c:
    print(10000+a*1000)
elif a == b:
    print(1000+a*100)
elif a == c:
    print(1000+a*100)
elif b == c:
    print(1000+b*100)
else:
    print(100 * max(a,b,c))
