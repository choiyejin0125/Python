import tkinter
# 버튼 클릭하면 실행하는 함수
def click_btn():

    # 값 입력 (글자여서 숫자로 바꿔야 함)
    
    num1= int(entry1.get())
    num2= int(entry2.get())

    # 라벨에 넣을 문자열

    str1= str(num1)+"을(를) "+str(num2)+"(으)로 나눈 몫은 "+str(num1//num2)+"입니다."
    str2= str(num1)+"을(를) "+str(num2)+"(으)로 나눈 나머지는 "+str(num1%num2)+"입니다."

    # 라벨 만들기 (설명이 담긴 문자열 1,2)
    labelRes1 = tkinter.Label(root,text=str1, font=("맑은고딕",10))
    labelRes1.place(x=21,y=86)
    labelRes2 = tkinter.Label(root,text=str2, font=("맑은고딕",10))
    labelRes2.place(x=21,y=124)

def mouseMove(event):
    x = event.x
    y = event.y
    labelMouse.config(text=str(x)+","+str(y))
    labelMouse.place(x=0,y=280)

# tkinter 기본문
root= tkinter.Tk()
root.title("산술 연산자")
root.geometry("400x300")

root.bind("<Motion>",mouseMove)
labelMouse = tkinter.Label(root,text=",", font=("맑은고딕",10))


# 라벨 만들기 (설명이 담긴 문자열 1,2)
label1 = tkinter.Label(root, text="나눠지는 수", font=("맑은고딕",10))
label2 = tkinter.Label(root, text="나누는 수", font=("맑은고딕",10))
label1.place(x=20,y=20)
label2.place(x=25,y=45)

# 사용자가 값을 입력흐는 란
entry1 = tkinter.Entry(width=10)
entry1.place(x=120, y=20)
entry2 = tkinter.Entry(width=10)
entry2.place(x=120, y=45)

# 계산버튼
btn = tkinter.Button(root, text="계산", font=("휴먼옛체",10),command=click_btn)
btn.place(x=186, y=20, width=54, height=54)




root.mainloop()