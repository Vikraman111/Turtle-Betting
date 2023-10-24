from turtle import Turtle,Screen
import random
colors = ["violet","indigo","blue","green","yellow","orange","red"]
all_turt = []

flag = False
scr = Screen()
scr.setup(width=500, height = 400)
user_bet = scr.textinput(title = "Make your bet",prompt="Bet on which color will win\nviolet indigo blue green yellow orange red\n CHECK YOUR TERMINAL FOR RESULTS!")
for i in range(7):
    new_turt = Turtle()
    new_turt.penup()
    new_turt.color(colors[i])
    new_turt.shape("turtle")
    new_turt.goto(-230, 150 - (40 * i))
    all_turt.append(new_turt)

#Make Race Start Only After Bet Has Been Made
if user_bet:
    flag = True
while flag:
    for j in all_turt:
        if j.xcor() > 230:
            flag = False
            win_color = j.pencolor()
            if win_color == user_bet:
                print("YOU WIN")
            else:
                print(f"You Lost\nWinning turtle was {win_color}")
        dist= random.randint(0,10)
        j.forward(dist)





scr.exitonclick()
