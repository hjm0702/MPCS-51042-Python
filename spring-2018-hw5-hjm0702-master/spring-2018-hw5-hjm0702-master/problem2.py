from abc import ABC, abstractmethod
import tkinter as tk
from math import sqrt


CANVAS_WIDTH = 100
CANVAS_HEIGHT = 100


def draw_pixel(canvas, x, y, color='#000000'):
    """Draw a pixel at (x,y) on the given canvas"""
    x1, y1 = x - 1, y - 1
    x2, y2 = x + 1, y + 1
    canvas.create_oval(x1, y1, x2, y2, fill=color, outline=color)


def main(shape):
    """Create a main window with a canvas to draw on"""
    master = tk.Tk()
    master.title("Drawing")
    canvas = tk.Canvas(master, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack(expand=tk.YES, fill=tk.BOTH)

    # Render the user-defined shape

    Drawable.draw(shape, canvas)

    # Start the Tk event loop (in this case, it doesn't do anything other than
    # show the window, but we could have defined "event handlers" that intercept
    # mouse clicks, keyboard presses, etc.)
    tk.mainloop()

class Drawable(ABC):
    @abstractmethod
    def __contain__(self):
        pass

    def __and__(self, other):
        return Intersection(self, other)

    def __or__(self, other):
        return Union(self, other)

    def __sub__(self, other):
        return Difference(self, other)

    def draw(self, canvas):
        for x in range(int(canvas['width'])):
            for y in range(int(canvas['height'])):
                if (x-CANVAS_WIDTH/2, CANVAS_HEIGHT/2-y) in self:
                    draw_pixel(canvas, x, y)

class Circle(Drawable):
    def __init__(self, x, y, r):
        self.xcord = x
        self.ycord = y
        self.radius = r
        self.coordinate = []
        for a in range(x-r,x+r):
            for b in range(y-r,y+r):
                if ((int(a)-x)**2+(int(b)-y)**2) <= r**2:
                    self.coordinate.append((a,b))

    def __contain__(self, point):
        return point in self.coordinate

    def __repr__(self):
        return f'Circle({self.xcord},{self.ycord},{self.radius})'

    def __len__(self):
        return len(self.coordinate)
    #
    def __getitem__(self, index):
        return self.coordinate[index]


class Rectangle(Drawable):
    def __init__(self, x0, y0, x1, y1):
        self.xlowerleft = x0
        self.ylowerleft = y0
        self.xupperright = x1
        self.yupperright = y1
        self.coordinate = [(a,b) for a in range(x0,x1) for b in range(y0,y1)]

    def __contain__(self, point):
        return point in self.coordinate

    def __repr__(self):
        return f'Rectangle({self.xlowerleft}, {self.ylowerleft}, {self.xupperright}, {self.yupperright})'

    def __len__(self):
        return len(self.coordinate)
    #
    def __getitem__(self, index):
        return self.coordinate[index]

class Intersection(Drawable):
    '''any subclass???'''
    def __init__(self, shape1, shape2):
        self.shape1 = shape1
        self.shape2 = shape2
        self.coordinate =[x for x in self.shape1.coordinate if x in self.shape2.coordinate]

    def __contain__(self, point):
        return point in self.coordiate

    def __repr__(self):
        return f'Intersection({self.shape1}, {self.shape2})'

    def __len__(self):
        return len(self.coordinate)

    def __getitem__(self, index):
        return self.coordinate[index]

class Union(Drawable):
    '''any subclass???'''
    def __init__(self, shape1, shape2):
        self.shape1 = shape1
        self.shape2 = shape2
        self.coordinate =[]
        for x in self.shape1.coordinate:
            self.coordinate.append(x)
        for x in self.shape2.coordinate:
            self.coordinate.append(x)

    def __contain__(self, point):
        return point in self.coordiate

    def __repr__(self):
        return f'Union({self.shape1}, {self.shape2})'

    def __len__(self):
        return len(self.coordinate)

    def __getitem__(self, index):
        return self.coordinate[index]

class Difference(Drawable):
    '''any subclass???'''
    def __init__(self, shape1, shape2):
        self.shape1 = shape1
        self.shape2 = shape2
        self.coordinate = [x for x in self.shape1.coordinate if x not in self.shape2.coordinate]

    def __contain__(self, point):
        return point in self.coordiate

    def __repr__(self):
        return f'Difference({self.shape1}, {self.shape2})'

    def __len__(self):
        return len(self.coordinate)

    def __getitem__(self, index):
        return self.coordinate[index]

if __name__ == '__main__':
    # Create a "happy" face by subtracting two eyes and a mouth from a head
    head = Circle(0, 0, 40)
    left_eye = Circle(-15, 15, 5)
    right_eye = Circle(15, 15, 5)
    mouth = Rectangle(-10, -15, 9, -5)
    happy_face = head - left_eye - right_eye - mouth

    main(happy_face)
    # print (happy_face)
