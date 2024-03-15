import turtle

def draw_pifagor_tree(t, branch_len, level):
    if level > 0:
        t.forward(branch_len)
        t.right(45)
        draw_pifagor_tree(t, branch_len * 0.7, level - 1)
        t.left(90)
        draw_pifagor_tree(t, branch_len * 0.7, level - 1)
        t.right(45)
        t.backward(branch_len)

def main():
    level = int(input("Введіть рівень рекурсії: "))
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    draw_pifagor_tree(t, 75, level)
    my_win.exitonclick()

if __name__ == "__main__":
    main()
