# 1	10818	 최소, 최대
n = int(input())
num = list(map(int, input().split()))

print(min(num), max(num))

# 2	2562	 최댓값
num_list=[]
for i in range(9):
    num_list.append(int(input()))
    
print(max(num_list))
print(num_list.index(max(num_list))+1)

# 3	2577	 숫자의 개수
a = int(input())
b = int(input())
c = int(input())

num = list(str(a*b*c))

for i in range(10):
    print(num.count(str(i)))
    
# 4	3052	 나머지
num=[]
for i in range(10):
    n = int(input())
    num.append(n%42)
num = set(num)
print(len(num))

# 5	1546	 평균
n = int(input())
test = list(map(int, input().split()))
best = max(test)

new = []
for score in test:
    new.append(score/best*100)
print(sum(new)/n)

# 6	8958	 OX퀴즈
n = int(input())

for i in range(n):
    ox = list(map(str, input()))
    
    correct = 0
    score = 0

    for i in ox:
        if i == 'O':
            correct+=1
            score = correct+score
        else:
            correct = 0
    print(score)
    
# 7	4344	 평균은 넘겠지
c = int(input())
for i in range(c):
    score = list(map(int, input().split()))
    avg = sum(score[1:])/score[0]
    
    cnt = 0
    for j in score[1:]:
        if j > avg:
            cnt+=1
    rate = cnt/score[0]*100
    
    print(f'{rate:.3f}%')
