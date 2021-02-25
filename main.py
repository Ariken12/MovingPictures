from Subject import Unit, randomcolor
from figures import *
from tkinter import *
import time


def main():
    wndw = Tk()
    H = 700
    W = 700
    wndw.geometry("{0}x{1}+300+300".format(W, H))
    wndw.resizable(False, False)
    height = H
    width = W
    canvas = Canvas(wndw)
    canvas.configure(width=width, height=height)
    canvas.pack()

    unit = Unit(canvas)
    unit.x, unit.y = 100, 100
    unit.size_x, unit.size_y = 30, 30
    unit.vx, unit.vy = 1, 5
    unit.ax, unit.ay = 0, 0
    unit.max_v = 10
    unit.min_v = -10
    unit.max_c = min(height, width) - max(unit.size_x, unit.size_y)
    unit.min_c = 0

    for i in range(100000000):
        canvas.delete('all')
        unit.impuls(random=True)
        unit.move()
        sqrt(unit, canvas, unit.size_x, unit.size_y)
        print(unit.x, unit.y, unit.vx, unit.vy, time.clock())
        canvas.configure()
        wndw.update()
        time.sleep(0.03)


if __name__ == '__main__':
    main()
