# 9498	 시험 성적
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
    
# 10817	 세 수
nums = list(map(int, input().split()))

nums.sort(reverse=True) # 'reverse' 없는 것보다 시간이 약간 빠름
print(nums[1])

# 11653	 소인수분해
n = int(input())

while n != 1:
    for i in range(2, n+1):
        if n % i == 0:
            print(i)
            n = n // i
            break

# 1789	 수들의 합

# 2753	 윤년

# 10039	 평균 점수

# 1934	 최소공배수

# 2480	 주사위 세개
# 4101	 크냐?
# 10156	 과자
# 3009	 네 번째 점
# 2476	 주사위 게임
# 2754	 학점계산
# 2884	 알람 시계
# 7567	 그릇
# 5063	 TGN
# 10102	 개표
# 10886	 0 = not cute / 1 = cute
# 10988	 팰린드롬인지 확인하기
# 5086	 배수와 약수
# 5717	 상근이의 친구들
# 9610	 사분면
# 8958	 OX퀴즈
# 9506	 약수들의 합
# 10162	 전자레인지
# 10103	 주사위 게임
# 10214	 Baseball
# 11557	 Yangjojang of The Year

# 10757	 큰 수 A+B
a, b = map(int, input().split())
print(a+b)
