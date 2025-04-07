import tkinter
root=tkinter.Tk()
root.title("캔버스 만들기")
canvas = tkinter.Canvas(root, width=800, height=600, bg="skyblue")
bgimg = tkinter.PhotoImage(file="miko.png")
canvas.create_image(400,300,image=bgimg)

# 사이즈를 지정하지않아도 들어감
canvas.pack()

root.mainloop()