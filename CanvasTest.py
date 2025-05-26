import tkinter
import random
from PIL import ImageTk, Image

root=tkinter.Tk()
root.title("캔버스 만들기")
#좌표출력기
def mouseMove(event):
    x = event.x
    y = event.y
    labelMouse["text"]=str(x)+","+str(y)

    labelMouse.place(x=0,y=280)

def click_btn():
    label["text"]= random.choice(["대길","중길","소길","흉"])
    text.insert(tkinter.END,label["text"]+"\n")

#캔버스 생성
canvas = tkinter.Canvas(root, width=800, height=600, bg="skyblue")
canvas.pack()

#좌표출력기
root.bind("<Motion>",mouseMove)
labelMouse = tkinter.Label(root,text=",", font=("맑은고딕",10))
labelMouse.pack()

#캔버스 내 이미지 생성
# 사이즈를 지정하지않아도 들어감
# bgimg = tkinter.PhotoImage(file="miko.png")
bgimg = ImageTk.PhotoImage(Image.open('miko.png'))
canvas.create_image(400,300,image=bgimg)

canvas.create_rectangle(352,394,601,488,fill='darkgray',outline='red',width=5)


label=tkinter.Label(root, text="??",font=("맑은고딕",120))
label.place(x=380,y=60)

btn=tkinter.Button(root, text="제비뽑기",font=("맑은고딕",36),command=click_btn)
btn.place(x=360,y=400)

text=tkinter.Text()
text.place(width=800,height=200)

root.mainloop()