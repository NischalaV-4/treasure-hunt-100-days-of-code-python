print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("this game consists of 5 levels.")
print("in order to find the treasure and win the game you need to surpass 5 levels")

direction = input("LEVEL 1 :let us know in which direction you would like to go (i)left (ii)right")
if direction=="right" or direction=="Right" :
    print("wrong direction!you fell into a cave and now getting chased by lion")
else:
    print("LEVEL 2:RIDDLE")
    riddle1=input("what has hands But cannot clap?")
    if riddle1=="clock":
        print("you are right!!here comes the next level:")
        print("LEVEL 3:PATTERN RECOGNITION")
        next_num=int(input("enter the next number 11,22,33,44,_"))
        if next_num==55:
            print("good job")
            print("LEVEL 4:FIND THE CORRECT ORDER OF LETTERS AND TYPE THE WORD")
            word=input("mdoran:guess the word.")
            if word=="Random" or word=="random":
                print("that's right")
                print("LEVEL 5:THE LAST ROUND")
                colour=input("choose between three doors yellow,red or blue")
                if colour=="yellow" or colour=="Yellow":
                    print("hurray you found the treasure.You won the game!!")
                else :
                    print("you fell into trap!!")
            else:
                print("sorry wrong guess!!")
        else:
            print("Incorrect pattern")
    else:
        print("Wrong answer to the riddle.")



