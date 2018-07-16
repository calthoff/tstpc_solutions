answer = input("Type a number")
try:
    int(answer)
    print(answer)
except:
    print("Please type an integer")