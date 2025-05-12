file = open("test.txt","r",encoding="UTF-8")

# str = file.readline()
# print(str,end="")
# str = file.readline()
# print(str,end="")
# str = file.readline()
# print(str,end="")

# for i in range(0,16,1):
#   str = file.readline()
#   print(str,end="")
# +
# str = file.readline()
# if(str == ""):
#   print("끝?")
# print(str,end="")

# while True:
#   str = file.readline()
#   print(str,end="")
#   if(str==""):
#       break

fileList=file.readlines()
index=1
for strList in fileList :
  print(str(index)+" : "+strList,end="")
  index= index+1


file.close()