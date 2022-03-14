def printProgressBar(a, b) :
    percentage = a / b * 100
    bar = "#" * int(percentage // 2) + " " * int(50 - percentage // 2)
    print(f'\033[34mLoading... {bar} | {round(percentage, 2)}%\t{str(a).zfill(len(str(b)))}/{b}', end='\r')
# Loading #################################################  | 98.7%  9872/10000


def isKorean(text) :
    korCount = 0
    for i in text :
        if (ord(i) >= ord("ㄱ") and ord(i) <= ord("ㅣ")) or (ord(i) >= ord("가") and ord(i) <= ord("힣")) :
            korCount += 1
    if korCount == 0 :
        return False
    elif korCount == len(text) :
        return True
    else :
        print("한글은 영어, 숫자, 특수기호와 함께 사용이 불가능합니다.")
        quit()