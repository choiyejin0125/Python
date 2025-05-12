#test.txt파일을 읽어와서
#outTest.txt파일에 작성한다

inFile = open("test.txt","r",encoding="UTF-8")
outfile = open("outTest.txt","w",encoding="UTF-8")

while True:
  str = inFile.readline()
  outfile.writelines(str)
  if(str==""):
      break


inFile.close()
outfile.close()