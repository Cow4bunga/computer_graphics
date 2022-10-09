import matplotlib.pyplot as plt

plt.title("Bresenham Algorithm for circle drawing")
plt.xlabel("X")
plt.ylabel("Y")

xcoordinates = []
ycoordinates = []


def draw_ellipse(xc, yc, x, y):
    plt.plot(xc + x, yc + y, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="red")
    plt.plot(xc - x, yc + y, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="red")
    plt.plot(xc + x, yc - y, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="red")
    plt.plot(xc - x, yc - y, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="red")


def bresenham_circle_algo(xcenter, ycenter, rx, ry):
    x = 0
    y = ry

    d1 = ((ry * ry) - (rx * rx * ry) + (0.25 * rx * rx))
    dx = 2 * x * ry * ry
    dy = 2 * y * rx * rx

    draw_ellipse(xcenter, ycenter, x, y)
    while dy > dx:
        draw_ellipse(xcenter, ycenter, x, y)
        if d1 < 0:
            x = x + 1
            dx = dx + (2 * ry * ry)
            d1 = d1 + dx + (ry * ry)
        else:
            x = x + 1
            y = y - 1
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            d1 = d1 + dx - dy + (ry * ry)

    d2 = (((ry * ry) * ((x + 0.5) * (x + 0.5))) +
          ((rx * rx) * ((y - 1) * (y - 1))) -
          (rx * rx * ry * ry))

    while y>=0:
        draw_ellipse(xcenter, ycenter, x, y)
        if d2 > 0:
            y=y-1
            dy = dy - (2 * rx * rx)
            d2 = d2 - dy + (rx * rx)
        else:
            x = x + 1
            y = y - 1
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            d2 = d2 + dx - dy + (rx * rx)

    plt.grid()
    plt.show()


def main():
    rx = int(input("Enter the radius for x: "))
    ry = int(input("Enter the radius for y: "))
    xcenter = int(input("Enter the x coordinate of a center point: "))
    ycenter = int(input("Enter the y coordinate of a center point: "))
    bresenham_circle_algo(xcenter, ycenter, rx, ry)


if __name__ == "__main__":
    main()
