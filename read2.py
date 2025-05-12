import tkinter

root=tkinter.Tk()


file = open("test2.txt","r",encoding="UTF-8")

strFile= file.readline()
root.geometry(strFile[:-1])

strFile = file.readline()
root.title(strFile[:-1])




file.close()

root.mainloop()