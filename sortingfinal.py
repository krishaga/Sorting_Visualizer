import turtle
import random
import time

# Screen
wn = turtle.Screen()
wn.title("Sorting Visualiser")
wn.setup(width=1200, height=700)
wn.tracer(0)

# Background
def display_vis():
    dispbg = turtle.Turtle()
    dispbg.color("grey")
    dispbg.fillcolor("#DAECFF")
    dispbg.speed(0)
    dispbg.hideturtle()
    dispbg.penup()
    dispbg.width(4)
    dispbg.goto(-412.5, 266)
    dispbg.pendown()
    dispbg.begin_fill()
    for i in range(2):
        dispbg.forward(831.5)
        dispbg.right(90)
        dispbg.forward(569)
        dispbg.right(90)
    dispbg.end_fill()
    wn.update()

# Initialization
a = []
l = []
d = 8
pen = [0] * 4
writer = [0] * 4

write_time = turtle.Turtle()
write_time.hideturtle()

# Hiding Turtle
def hide_turtle():
    for i in range(4):
        pen[i].reset()
        pen[i].hideturtle()
        writer[i].reset()
        writer[i].hideturtle()
    wn.update()

# Showing Turtle
def show_turtle():
    function_button()

# Generating Lines
def generate_lines():
    global d, a, l
    for i in range(100):
        line_turtle = turtle.Turtle()
        line_turtle.hideturtle()
        line_turtle.shape("square")
        line_turtle.color("cyan")
        alen = random.uniform(0.1, 28)
        line_turtle.shapesize(stretch_len=alen, stretch_wid=0.2)
        l.append(alen)
        line_turtle.speed(0)
        line_turtle.left(90)
        line_turtle.penup()
        res_len_sel = 300 - (alen * 10)
        line_turtle.goto((-400 + d), -res_len_sel)
        line_turtle.showturtle()
        a.append(line_turtle)
        d += 8
    d = 8
    wn.update()

# Selection Sort
def sel_sort():
    for i in range(100):
        a[i].color("#FF1100")
        var = a[i].xcor()
        length = l[i]
        pos = i

        res_len_sel = res_len_strd = 300 - (l[i] * 10)

        for j in range(i + 1, 100):
            if l[j] < length:
                length = l[j]
                var = a[j].xcor()
                res_len_strd = 300 - (l[j] * 10)
                pos = j
            a[j].color("cyan")

        a[pos].color("green")
        a[pos].goto(a[i].xcor(), -res_len_strd)
        a[i].goto(var, -res_len_sel)
        a[i], a[pos] = a[pos], a[i]
        l[i], l[pos] = l[pos], l[i]
        wn.update()

# Bubble Sort
def bub_sort():
    for i in range(99):
        for j in range(99 - i):
            a[j].color("red")
            var = a[j].xcor()
            vara = a[j + 1].xcor()
            if l[j] > l[j + 1]:
                a[j].setx(vara)
                a[j + 1].setx(var)
                a[j], a[j + 1] = a[j + 1], a[j]
                l[j], l[j + 1] = l[j + 1], l[j]
            a[j].color("cyan")
            a[j + 1].color("green")
        wn.update()
    a[0].color("green")
    wn.update()

# Clearing Screen
def clear_screen():
    global a, l
    for line_turtle in a:
        line_turtle.clear()
        line_turtle.hideturtle()
    del a[:]
    del l[:]
    generate_lines()

# Generating Buttons
def generate_buttons(x, y, obj, msg):
    pen[obj] = turtle.Turtle()
    pen[obj].hideturtle()
    pen[obj].penup()
    pen[obj].goto(x - 80, y - 20)
    pen[obj].pendown()
    pen[obj].color("#52A1FA")
    pen[obj].begin_fill()
    for i in range(2):
        pen[obj].fd(160)
        pen[obj].left(90)
        pen[obj].fd(40)
        pen[obj].left(90)
    pen[obj].end_fill()
    writer[obj] = turtle.Turtle()
    writer[obj].hideturtle()
    writer[obj].penup()
    writer[obj].goto(x, y - 7.5)
    writer[obj].write(msg, font=('Verdana', 12, 'normal'), align="center")
    wn.update()

# Generating Buttons
def function_button():
    generate_buttons(-300, 300, 0, "Create New Lines")
    generate_buttons(-100, 300, 1, "Selection Sort")
    generate_buttons(100, 300, 2, "Bubble Sort")
    generate_buttons(300, 300, 3, "Clear Screen")

# Time Taken
def write_timeTaken(t):
    global write_time
    write_time.hideturtle()
    write_time.penup()
    write_time.goto(0, -325)
    write_time.write("Time Taken: " + str(t), font=('Verdana', 12, 'normal'), align="center")
    wn.update()

# Checking Screen Click
def checki(x, y):
    write_time.clear()
    if x > (-380) and x < (-220) and y > 280 and y < 320:
        hide_turtle()
        clear_screen()
        show_turtle()
    elif x > (-180) and x < (-20) and y > 280 and y < 320:
        hide_turtle()
        t1 = time.time()
        sel_sort()
        t2 = time.time()
        write_timeTaken(t2 - t1)
        show_turtle()
    elif x > 20 and x < 180 and y > 280 and y < 320:
        hide_turtle()
        t1 = time.time()
        bub_sort()
        t2 = time.time()
        write_timeTaken(t2 - t1)
        show_turtle()
    elif x > 220 and x < 380 and y > 280 and y < 320:
        hide_turtle()
        clear_screen()
        show_turtle()

# Screen
display_vis()

# Generating Buttons
function_button()
turtle.onscreenclick(checki)
turtle.listen()

turtle.done()