import random as rand

def randomcolor():
    global rand
    a = str(hex(int(rand.randint(0, 16777215)))).replace('0x', '')
    while len(a) < 6:
        a = '0' + a
    return '#' + a

class Unit:
    def __init__(self, x=0, y=0, size_x=0, size_y=0, vx=0, vy=0, ax=0, ay=0, m=1, color='#000000'):
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y
        self.vx = vx
        self.vy = vy
        self.ax = ax
        self.ay = ay
        self.m = m
        self.min_c = self.max_c = None
        self.min_v = self.max_v = None
        self.min_a = self.max_a = None
        self.color = color
        self.state = 0

    def update_state(self, max=2):
        self.state += 1
        if self.state > max:
            self.state = 0

    def __filter(self, x, a, b):
        min_range = min(a, b)
        max_range = max(a, b)
        range = max_range - min_range
        if x > max_range:
            return max_range
        elif x < min_range:
            return min_range
        else:
            return x

    def move(self, random=False):
        if self.max_c is not None and self.min_c is not None:
            if not random:
                self.x = self.__filter(self.x + self.vx, self.min_c, self.max_c)
                self.y = self.__filter(self.y + self.vy, self.min_c, self.max_c)
            elif random:
                self.x = self.__filter(self.x + rand.randint(0, int(self.max_c)), self.min_c, self.max_c)
                self.y = self.__filter(self.y + rand.randint(0, int(self.max_c)), self.min_c, self.max_c)
        else:
            self.x += self.vx
            self.y += self.vy

    def impuls(self, random=False):
        if self.max_v is not None and self.min_v is not None:
            if not random:
                self.vx = self.__filter(self.vx + self.ax, self.min_v, self.max_v)
                self.vy = self.__filter(self.vy + self.ay, self.min_v, self.max_v)
            elif random:
                self.vx = self.__filter(self.vx + rand.randint(int(self.min_v), int(self.max_v)),
                                        self.min_v,
                                        self.max_v)
                self.vy = self.__filter(self.vy + rand.randint(int(self.min_v), int(self.max_v)),
                                        self.min_v,
                                        self.max_v)
        else:
            self.vx += self.ax
            self.vy += self.ay
