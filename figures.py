import matplotlib.pyplot as plt

plt.title("Bresenham Algorithm for circle drawing")
plt.xlabel("X")
plt.ylabel("Y")

xcoordinates = []
ycoordinates = []


def draw_circle(xc, yc, x, y):
    plt.plot(xc + x, yc + y, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="red")
    plt.plot(xc - x, yc + y, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="red")
    plt.plot(xc + x, yc - y, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="red")
    plt.plot(xc - x, yc - y, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="red")
    plt.plot(xc + y, yc + x, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="red")
    plt.plot(xc - y, yc + x, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="red")
    plt.plot(xc + y, yc - x, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="red")
    plt.plot(xc - y, yc - x, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="red")


def bresenham_circle_algo(xcenter, ycenter, r):
    x = 0
    y = r

    d = 3 - (2 * r)

    draw_circle(xcenter, ycenter, x, y)
    while y >= x:
        # xcoordinates.append(x)
        # ycoordinates.append(-y)
        # xcoordinates.append(y)
        # ycoordinates.append(-x)
        # xcoordinates.append(y)
        # ycoordinates.append(x)
        # xcoordinates.append(x)
        # ycoordinates.append(y)
        # xcoordinates.append(-x)
        # ycoordinates.append(y)
        # xcoordinates.append(-y)
        # ycoordinates.append(x)
        # xcoordinates.append(-y)
        # ycoordinates.append(-x)
        # xcoordinates.append(-x)
        # ycoordinates.append(-y)
        x = x + 1
        if d > 0:
            y = y - 1
            d = d + (4 * (x - y)) + 10
        else:
            d = d + (4 * x) + 6
        draw_circle(xcenter, ycenter, x, y)

    plt.grid()
    plt.show()


def main():
    r = int(input("Enter the radius: "))
    xcenter = int(input("Enter the x coordinate of a center point: "))
    ycenter = int(input("Enter the y coordinate of a center point: "))
    bresenham_circle_algo(xcenter, ycenter, r)


if __name__ == "__main__":
    main()
