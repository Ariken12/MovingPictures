def man(self, size):
    x = self.x
    y = self.y
    x1 = self.x + size
    y1 = self.y + size
    self.canvas.create_oval()


def sqrt(self, canvas, height, width):
    x = self.x
    y = self.y
    x1 = self.x + width
    y1 = self.y + height
    canvas.create_rectangle(x, y, fill=self.color)
    canvas.create_text(x1, y1 + 2 * (y1 - y), text='This world is mine!', font='Arial')


def sanyka(self, canvas, height, width):
    x = self.x
    y = self.y
    x1 = self.x + width
    y1 = self.y + height
    canvas.create_line(x, y, x, y + (y1 - y) / 2)
    canvas.create_line(x1, y + (y1 - y) / 2, *self.xy[1])
    canvas.create_line(x + (x1 - x) / 2, y, x1, y)
    canvas.create_line(x, y1, x + (x1 - x) / 2, y1)
    canvas.create_line(x + (x1 - x) / 2, y, x + (x1 - x) / 2, y1)
    canvas.create_line(x, y + (y1 - y) / 2, x1, y + (y1 - y) / 2)
    canvas.create_text(x1, y1 + 2 * (y1 - y), text='Hail Furry!!!', font='Arial '+str(height))


def bird(self, canvas, height, width):
    x = self.x
    y = self.y
    self.update_state()
    canvas.create_text(x, y, text=('-.,.-' if self.state == 1 else '_.,._'), font='Arial '+str(height))
