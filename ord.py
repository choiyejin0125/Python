# value="가"
# print(value)
# valueNum= ord(value)
# print(valueNum)
# valueNum=valueNum+100
# print(valueNum)
# value=chr(valueNum)
# print(value)

# value="갬갬"
# print(value)
# valueNum= ord(value)
# print(valueNum)
# valueNum=valueNum-100
# print(valueNum)
# value=chr(valueNum)
# print(value)

#test.txt파일을 읽어와서
#outTest.txt파일에 작성한다

inFile = open("test.txt","r",encoding="UTF-8")
outfile = open("outTest.txt","w",encoding="UTF-8")

while True:
  strFile = inFile.readline()
  #strFile
  strFileChange=""
  for ch in strFile:
    #암호화화
    chNum=ord(ch)
    chNum=chNum+100
    chChange=chr(chNum)
    strFileChange+=chChange
  if(strFile==""):
      break
  outfile.writelines(strFileChange)


inFile.close()
outfile.close()

inFile = open("outTest.txt","r",encoding="UTF-8")
while True:
  strFile = inFile.readline()
  #strFile
  strFileChange=""
  for ch in strFile:
    #암호화화
    chNum=ord(ch)
    chNum=chNum-100
    chChange=chr(chNum)
    strFileChange+=chChange
  if(strFile==""):
      break
  print(strFileChange,end="")

inFile.close()