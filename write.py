outfile = open("outTest.txt","w",encoding="UTF-8")

# outStr="안녕하세요."
# outfile.writelines(outStr+"\n")
# outStr="반갑습니다."
# outfile.writelines(outStr+"\n")
while True :
  outStr=input("내용입력 ==> ")
  #"끝"이라고 입력 하면 종료
  if outStr=='끝':
    break
  outfile.writelines(outStr+"\n")





outfile.close()

