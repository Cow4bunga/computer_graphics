import matplotlib.pyplot as plt

plt.title("Bresenham Algorithm for line drawing")
plt.xlabel("X")
plt.ylabel("Y")


def bresenham_line_algo(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x, y = x1, y1

    grad = dy / float(dx)

    # if the slope is not positive, we swap coordinates
    if grad > 1:
        dx, dy = dy, dx
        x, y = y, x
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    error = 2 * dy - dx
    print(f"x = {x}, y = {y}")

    xcoordinates = [x]
    ycoordinates = [y]

    for k in range(2, dx + 2):
        print(f"x = {x}, y = {y}")
        if error > 0:
            if y < y2:
                y += 1
            else:
                y -= 1
            error = error + 2 * (dy - dx)
        else:
            error = error + 2 * dy

        if x < x2:
            x += 1
        else:
            x -= 1

        xcoordinates.append(x)
        ycoordinates.append(y)

    plt.plot(xcoordinates, ycoordinates)
    plt.grid()
    plt.show()


x1 = int(input("Enter first x coordinate:"))
y1 = int(input("Enter first y coordinate:"))
x2 = int(input("Enter last x coordinate:"))
y2 = int(input("Enter last y coordinate:"))

bresenham_line_algo(x1, y1, x2, y2)
