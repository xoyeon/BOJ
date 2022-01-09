# 1	10952	 A+B - 5
while True:
    a, b = map(int, input().split())
    if a==0 and b==0:
            break
    print(a+b)
    
# 2	10951	 A+B - 4
while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break

# 3	1110	 더하기 사이클
num = n = int(input())
cnt = 0

while True:
    a = num//10
    b = num%10
    c = (a+b)%10
    cnt+=1
    num = (b*10)+c
    
    if num == n:
        break
print(cnt)
