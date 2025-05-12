for i in range(1,5,2): #1,3 번
    for j in range(2,3,2): #2,3 2번 총 6벚번 출력
        print("안녕하세요")
        if j%2==0:
            continue #총8번출력 break시 4번
        print("안녕하세요")
    print("안녕하세요")


strIn=input("원본 문자열")
strOut=strIn[3]+strIn[2]+strIn[1]+strIn[0]
n=len(strIn) ##문자 길이 받기 반복문for문으로 출력
print(n)
print("반대문자열==>",strOut)

