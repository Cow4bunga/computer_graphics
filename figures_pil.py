import PIL.Image
import PIL.ImageDraw

points = set()


def add_pixel(xc, yc, x, y):
    points.add((xc + x, yc + y))
    points.add((xc - x, yc + y))
    points.add((xc + x, yc - y))
    points.add((xc - x, yc - y))
    points.add((xc + y, yc + x))
    points.add((xc - y, yc + x))
    points.add((xc + y, yc - x))
    points.add((xc - y, yc - x))


def bresenham_algo_circle(xc, yc, radius):
    d = 3 - (2 * radius)
    points.clear()
    x = 0
    y = radius
    # running through each octant
    while x <= y:
        x = x + 1
        if d < 0:
            d = d + (4 * x) + 6
        else:
            y = y - 1
            d = d + (4 * (x - y)) + 10
        add_pixel(xc, yc, x, y)
    return points


def main():
    size = int(input("Enter the size of a canvas: "))
    radius = int(input("Enter the radius: "))
    xcenter = int(input("Enter the x coordinate of a center point: "))
    ycenter = int(input("Enter the y coordinate of a center point: "))

    canvas = PIL.Image.new("RGB", (size, size), (0, 0, 0))
    draw = PIL.ImageDraw.Draw(canvas)
    p = bresenham_algo_circle(xcenter, ycenter, radius)

    for point in p:
        draw.point((size / 2 + point[0], size / 2 + point[1]), (255, 255, 255))
    canvas.show()


if __name__ == "__main__":
    main()
