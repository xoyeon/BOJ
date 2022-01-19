# 1	11654	 아스키 코드
n = input()
print(ord(n))   ## ord:문자에 맞는 아스키코드, chr:숫자에 맞는 아스키코드

# 2	11720	 숫자의 합
n = int(input())
num = map(int, input())

print(sum(num))

# 3	10809	 알파벳 찾기
s = str(input())
abc = 'abcdefghijklmnopqrstuvwxyz'

for i in abc:
    print(s.find(i))
    
# 4	2675	 문자열 반복
t = int(input())

for i in range(t):
    r, s = input().split()

    for i in range (len(s)):
        print(int(r)*str(s)[i], end='')

    print()
    
# 5	1157	 단어 공부
word = input().upper()
word_list = list(set(word))

num = []
for i in word_list:
    cnt = word.count(i)
    num.append(cnt)
    
if num.count(max(num)) > 1 :
    print('?')
else:
    print(word_list[num.index(max(num))])

# 6	1152	 단어의 개수
words = input().split()
print(len(words))

# 7	2908	 상수
a, b = map(str, input().split())
a = a[::-1]
b = b[::-1]

if a > b:
  print(a)
else:
  print(b)

# 8	5622	 다이얼
word = input()
phone = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

answer = 0
for i in range(len(word)):
  for j in phone:
    if word[i] in j:
      answer+= phone.index(j)+3
print(answer)

# 9	2941	 크로아티아 알파벳
change = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in change:
  word = word.replace(i, '*')
print(len(word))

# 10	1316	 그룹 단어 체커
n = int(input())
count = n

for i in range(n):
  word = input()
  for j in range(len(word)-1):
    if word.find(word[j]) > word.find(word[j+1]) :
      count-=1
      break
print(count)
