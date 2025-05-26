import tkinter
import tkinter.messagebox
from PIL import ImageTk, Image


root=tkinter.Tk()
root.title("캔버스 만들기")

result= [
   "전생에 고양이었을 가능성은 매우 낮습니다",
   "보통 사람입니다",
   "특별히 이상한 곳은 없습니다",
   "꽤 고양이 다운 구석이 있습니다",
   '고양이와 비슷한 성격 같습니다',
   "고양이와 근접한 성격입니다",
   "전생에 고양이었을지도 모릅니다",
   "겉모습은 사람이지만 속은 고양이일 가능성이 있습니다"

]

def mouseMove(event):
    x = event.x
    y = event.y
    labelMouse["text"]=str(x)+","+str(y)

    labelMouse.place(x=0,y=280)

#캔버스 생성
canvas = tkinter.Canvas(root, width=800, height=600, bg="skyblue")
canvas.pack()

#체크크버튼 클릭시
# def chkBtnClick():
#     if cvalue.get() == True:
#         print("체크 되었습니다")
        # answer = tkinter.messagebox.askyesno("제목","오징어 게임에 참가하시겠습니까")
        # answer = tkinter.messagebox.askokcancel("제목","오징어 게임에 참가하시겠습니까")
        # if answer ==True:
        #     print("동의")
        # else:
        #     print("거절")
        # tkinter.messagebox.showinfo("제목","내용")
        # tkinter.messagebox.showwarning("제목","내용")
        # tkinter.messagebox.showerror("제목","내용")
    # else:
    #     print("체크가 해제 되었습니다")

def chkBtnClick():
  numCheck=0
  if cvalue1.get() == True:numCheck +=1
  if cvalue2.get() == True:numCheck +=1
  if cvalue3.get() == True:numCheck +=1
  if cvalue4.get() == True:numCheck +=1
  if cvalue5.get() == True:numCheck +=1
  if cvalue6.get() == True:numCheck +=1
  if cvalue7.get() == True:numCheck +=1
  print(numCheck)
  

#버튼 클릭시 
def btnClick():
  numCheck=0
  if cvalue1.get() == True:numCheck +=1
  if cvalue2.get() == True:numCheck +=1
  if cvalue3.get() == True:numCheck +=1
  if cvalue4.get() == True:numCheck +=1
  if cvalue5.get() == True:numCheck +=1
  if cvalue6.get() == True:numCheck +=1
  if cvalue7.get() == True:numCheck +=1
  print(numCheck)
  textFiled.delete("1.0",tkinter.END)
  textFiled.insert("1.0","<진단결과>\n 당신의 고양이 지수는"+str(int(numCheck/7*100))+"%입니다  \n"+result[numCheck])

#좌표출력기
root.bind("<Motion>",mouseMove)
labelMouse = tkinter.Label(root,text=",", font=("맑은고딕",10))
labelMouse.pack()

#캔버스 내 이미지 생성
bgimg = ImageTk.PhotoImage(Image.open('mina.png'))
canvas.create_image(400,300,image=bgimg)

#
cvalue1 = tkinter.BooleanVar()
cvalue2 = tkinter.BooleanVar()
cvalue3 = tkinter.BooleanVar()
cvalue4 = tkinter.BooleanVar()
cvalue5 = tkinter.BooleanVar()
cvalue6 = tkinter.BooleanVar()
cvalue7 = tkinter.BooleanVar()
cvalue1.set(False)
cvalue2.set(False)
cvalue3.set(False)
cvalue4.set(False)
cvalue5.set(False)
cvalue6.set(False)
cvalue7.set(False)


cBtn1=tkinter.Checkbutton(text="높은 곳이 좋다",variable=cvalue1,command=chkBtnClick)
cBtn2=tkinter.Checkbutton(text="공을 보면 굴리고 싶어진다",variable=cvalue2,command=chkBtnClick)
cBtn3=tkinter.Checkbutton(text="깜짝 놀라면 털이 곤두선다",variable=cvalue3,command=chkBtnClick)
cBtn4=tkinter.Checkbutton(text="쥐구멍이 마음에 든다",variable=cvalue4,command=chkBtnClick)
cBtn5=tkinter.Checkbutton(text="개에게 적대감을 느낀다",variable=cvalue5,command=chkBtnClick)
cBtn6=tkinter.Checkbutton(text="생선 뼈를 발라 먹고 싶다",variable=cvalue6,command=chkBtnClick)
cBtn7=tkinter.Checkbutton(text="밤 기운이난다",variable=cvalue7,command=chkBtnClick)

ygap=40
cBtn1.place(x=402,y=165)
cBtn2.place(x=402,y=165+ygap*1)
cBtn3.place(x=402,y=165+ygap*2)
cBtn4.place(x=402,y=165+ygap*3)
cBtn5.place(x=402,y=165+ygap*4)
cBtn6.place(x=402,y=165+ygap*5)
cBtn7.place(x=402,y=165+ygap*6)

textFiled= tkinter.Text()
textFiled.place(x=330,y=50,width=420,height=90)

btn= tkinter.Button(text="진단하기",font=("맑은고딕",24),bg="#CFF7EB",command=btnClick)
btn.place(x=430,y=480,width=150,height=60)
root.mainloop()