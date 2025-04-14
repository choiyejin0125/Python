for i in range(0,3,1): #0부터3까지 그리고 1씩증가값(초기값,끝값,증가값), 항상0값으로 시작 그래서 0은 생략가능(3,1) i는 카운트세는변수
    print(i,"파이썬은 재미있습니다 ^^")

for j in range(51,101,3):
    print(j, end=" ")

# 실습 1
# 팩토리아 계산기 : 1부터 N까지의 곱 (경우의수)
N=5
res1=1
for x in range(1,N+1,1):
    res1= res1*x
    
    print(res1) #120

# 연습1
# 1000 - 2000 사이에서 홀수의 합을 구하는 프로그램
N=2000
res2=0
for z in range(1001,N+1,2):
    res2 = res2 + z
    
    print(res2)

# 중첩 for 문
for w in range(0,3,1):
    for k in range(0,2,1):
        print("W : ",w,"   k : ",k)

# 실습2
# 2 단부터 9 단까지 구구단 출력
for num1 in range(2,10,1): #단
    print("구구딘",num1,"단")
    for num2 in range(1,10,1): #곱해지는 수
        print(num1, "X", num2,"=\t",num1*num2)

# while 문
q = 0
while(q <3): #참일경우
    print(q) #출력,무한출력 멈추는법:컨트롤+C 또는 정지버튼
    q=q+1


# 계산기 만들기
while(True):
    num1 = int(input("숫자1===> "))
    #num1 이 0이면 반복문 종료
    if num1 == 0:
        break
    num2 = int(input("숫자2===> "))
    res3=num1 +num2
    print(num1,"+",num2,"=",res3)

# 연습2
# 1부터 100까지를 더하되 4의 배수는 더하지 않음
# 3의 배수도 더하지 않음
res4=0
for a in range(1,101,1):
    if a%4 == 0:
        continue
    if a%3 ==0:
        continue
    res4 = res4+a
print(res4)



