# num = 99

# if num < 100 :
#     print("100보다 작은 수 입니다.")
# else :
#     print("100과 같거나 큰 수 입니다.")


# print("프로그램 종료")

# num1=input("숫자 ==>")
# num1 = int(num1)

# num2=num1%2

# if num2 > 0 :
#     print("홀수입니다")
# else :
#     print("짝수입니다")

num = int(input="숫자 입력 =>")


# <-100 / 100~1000 / 1000 ->
# 1. 100이하 조건
# 2. 1000이하 조건

if num < 1000 :
    if num < 100:
        print("100보다 작음")
else :
    if num>100:
        print("100보다 크고 , 1000보다 작음")
    else :
        print("100보다 작음")