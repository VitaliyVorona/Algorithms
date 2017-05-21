import turtle


def seq3np1(x):
    if x == 1:
        return x
    count = 0
    while x != 1:
        count += 1
        if x % 2 == 0:
            x //= 2
        else:
            x = x * 3 + 1
    return count


wn = turtle.Screen()
wn.setworldcoordinates(-50, -50, 50, 50)

alex = turtle.Turtle()
alex.pensize(3)
alex.pencolor('red')

for start in range(seq3np1(7)):
    alex.penup()
    alex.forward(1)
    alex.left(90)
    alex.pendown()

wn.mainloop()
