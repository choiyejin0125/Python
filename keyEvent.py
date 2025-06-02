import tkinter
from PIL import ImageTk, Image
#전역변수
key = 0
cx =400
cy=300
def main_proc():
  # lable["text"]=key

  #키보드 입력으로 위치 변경
  global cx,cy,key
  if key == "Up":
    cy-=20
  if key == "Down":
    cy+=20
  if key == "Left":
    cx = cx-20
  if key == "Right":
    cx= cx+20

  #시간에 따라 캐릭터가 내려감
  cy += 10


  #변경된 위치의 경계를 확인
  if cy<40: cy=40
  if cy>600-40: cy=600-40
  if cx<40: cx=40
  if cx>800-40:cx=800-40

  #변경된 위치에 이미지를 옮김
  canvas.coords("춘식",cx,cy)
  key=0
  root.after(100, main_proc)

def key_down(e):
  global key
  key=e.keysym #keycode
  pass 

def key_up(e):
  global key
  key=0

root=tkinter.Tk()
root.title("키 이벤트")
root.bind("<KeyPress>",key_down)
root.bind("<KeyRelease>",key_up)

# lable=tkinter.Label(font=("맑은고딕",80))
# lable.pack()

canvas= tkinter.Canvas(width=800,height=600,bg='skyblue')
canvas.pack()

img= ImageTk.PhotoImage(Image.open("춘식.png"))
canvas.create_image(400,300, image=img ,tag="춘식")
canvas.coords("춘식",500,400)


main_proc()
root.mainloop()