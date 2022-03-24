# 1	2557	 Hello World
print("Hello World!")

# 2	10718	 We love kriii
print("강한친구 대한육군\n강한친구 대한육군")

# 3	10171	 고양이😺
print("\\    /\\") ## 역슬래시(\)는 두번입력해야 문자
print(" )  ( ')")
print("(  /  )")
print(" \\(__)|")

# 4	10172	 개
print('|\_/|')
print('|q p|   /}')
print('( 0 )"""\\')
print('|"^"`    |')
print('||_/=\\\__|') ## 여기에서도 역슬래시 한 번 더

# 5	1000	 A+B
a, b =input().split()
print(int(a)+int(b))

# 6	1001	 A-B
a, b = input().split()
print(int(a)-int(b))

# 7	10998	 A×B
a, b = map(int, input().split())
print(a*b)

# 8	1008	 A/B
a, b = map(int, input().split())
print(round(a/b, 9))

# 9	10869	 사칙연산
a, b = map(int, input().split())

print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
print(a%b)

# 10 10926	 ??!
print(input()+"??!")

# 11 	18108	 1998년생인 내가 태국에서는 2541년생?!
y = int(input())
print(y-543)

# 12	10430	 나머지
A, B, C = map(int, input().split())
print(int((A+B)%C))
print(int(((A%C) + (B%C))%C))
print(int((A*B)%C))
print(int(((A%C) * (B%C))%C))

# 13	2588	 곱셈	성공
a = int(input())
b = input()

print(a * int(b[2]))
print(a * int(b[1]))
print(a * int(b[0]))
print(a * int(b))
