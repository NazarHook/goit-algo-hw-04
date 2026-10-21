import turtle


def koch_curve(t: turtle.Turtle, length: float, level: int) -> None:
    """Малює криву Коха заданого рівня рекурсії."""
    if level == 0:
        t.forward(length)
        return

    length /= 3
    for angle in (60, -120, 60, 0):
        koch_curve(t, length, level - 1)
        t.left(angle)


def snowflake(t: turtle.Turtle, length: float, level: int) -> None:
    """Малює сніжинку Коха з трьох кривих."""
    for _ in range(3):
        koch_curve(t, length, level)
        t.right(120)


def main() -> None:
    while True:
        try:
            level = int(input("Введіть рівень рекурсії (ціле число >= 0): "))
            if level >= 0:
                break
        except ValueError:
            pass
        print("Некоректне значення, спробуйте ще раз.")

    screen = turtle.Screen()
    screen.title("Сніжинка Коха")
    screen.tracer(0)

    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(-200, 110)
    t.pendown()

    snowflake(t, 400, level)

    screen.update()
    turtle.done()


if __name__ == "__main__":
    main()
