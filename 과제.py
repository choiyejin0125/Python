import tkinter
import random

#숫자만들기
nums = list(range(10))
random.shuffle(nums)
randomNum = [str(nums[0]), str(nums[1]), str(nums[2])]

count = 0
log = ""

def click_btn():
    global count
    global log

    num1 = entry1.get()
    num2 = entry2.get()
    num3 = entry3.get()

    if count >= 9:
        label_result["text"] = "기회 끝\n정답: " + randomNum[0] + randomNum[1] + randomNum[2]
        return

    if ('0' <= num1 <= '9') and ('0' <= num2 <= '9') and ('0' <= num3 <= '9'):
        if num1 != num2 and num1 != num3 and num2 != num3:
            count = count + 1
            strike = 0
            ball = 0

            if num1 == randomNum[0]:
                strike = strike + 1
            elif num1 == randomNum[1] or num1 == randomNum[2]:
                ball = ball + 1

            if num2 == randomNum[1]:
                strike = strike + 1
            elif num2 == randomNum[0] or num2 == randomNum[2]:
                ball = ball + 1

            if num3 == randomNum[2]:
                strike = strike + 1
            elif num3 == randomNum[0] or num3 == randomNum[1]:
                ball = ball + 1

            if strike == 3:
                result = "정답"
            else:
                if strike > 0 and ball > 0:
                    result = "스트라이크 / 볼"
                elif strike > 0:
                    result = "스트라이크"
                elif ball > 0:
                    result = "볼"
                else:
                    result = "아웃"

            label_result["text"] = result
            log = log + num1 + num2 + num3 + " → " + result + "\n"
            label_log["text"] = log
            label_count["text"] = "남은 기회: " + str(9 - count)
        else:
            label_result["text"] = "중복 없이 입력"
    else:
        label_result["text"] = "숫자만 입력"

# 창 만들기
root = tkinter.Tk()
root.title("야구 게임")
root.geometry("400x450")

label_title = tkinter.Label(root, text="0~9 서로 다른 숫자 3개 입력", font=("맑은고딕", 12))
label_title.place(x=20, y=20)

entry1 = tkinter.Entry(root, width=3)
entry2 = tkinter.Entry(root, width=3)
entry3 = tkinter.Entry(root, width=3)
entry1.place(x=60, y=60)
entry2.place(x=110, y=60)
entry3.place(x=160, y=60)

btn = tkinter.Button(root, text="확인", command=click_btn)
btn.place(x=220, y=58)

label_result = tkinter.Label(root, text="", font=("맑은고딕", 14))
label_result.place(x=20, y=110)

label_count = tkinter.Label(root, text="남은 기회: 9", font=("맑은고딕", 10))
label_count.place(x=20, y=150)

label_log = tkinter.Label(root, text="", font=("맑은고딕", 10), justify="left", anchor="nw")
label_log.place(x=20, y=190, width=360, height=240)

root.mainloop()