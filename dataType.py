a=100
# 데이터 타입 확인하기
print(type(a))

# 문자줄 형태로 만들기
var1 = """
나는
파이썬을
열공 중입니다.
"""

print(var1)

# 이스케이프 문자
print("나는\n파이썬을열공\n중입니다.")
print("\n줄바꿈\n연습")
print("\t탭키\t연습")
print("글자를 \"강조\"하는 효과1")
print("글자를 \'강조\'하는 효과1")
print("\\\\백슬래시 2개출력")


# 문자열 더하기
var2 = "나는 파이썬을 열공 중입니다."
var3="화이팅"

var4=var2+var3
var5=var3+var2
print(var4)
print(var5)

# 문자열 길이 확인
str1Len=len(var2)
str2Len=len(var3)


print("두 문자열 길이의 차이는 "+str(str1Len-str2Len)+"입니다.")

# 소문자를 대문자로
ss="Pytion을 밤 12시까지 열공 중!"
var6=ss.upper()
print(var6)
# 대문자를 소문자로
var7=ss.lower()
print(var7)

# 문자찾기
var8="123456789"
num1=var8.count("1")
print(num1)

# 인덱스로 문자찾기
print(var8[5])

# 문자위치찾기find("찾을단어","시작위치치")
var9="123456789"
num2=var9.find("5") 
print(num2)


