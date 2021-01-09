import random

def hangman(word):
    wrong = 0
    stages=["",
            "_______     ",
            "|      |    ",
            "|      O    ",
            "|      |    ",
            "|     /|\   ",
            "|    /   \  ",
            ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("welcome to HangMan!")

    while wrong < len(stages) - 1:
       
        msg="\nplease sguest one letter\n"
        char=input(msg) 
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong+=1
        print(" ".join(board))
        e=wrong+1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("you win")
            print(" ".join(board))
            win=True
            break
    if not win:
        print("\n".join(board))
        print("You lose. The answer is {}".format(word))


x=["letter","dazone","panda"]
hangman(x[random.randint(0,2)])


