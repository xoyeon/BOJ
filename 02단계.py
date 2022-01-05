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
