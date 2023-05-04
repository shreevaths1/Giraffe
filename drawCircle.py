import matplotlib.pyplot as plt


class Circle:
    def __init__(self, radius, color):
        self.dradius = radius
        self.color = color

    def addRadius(self, r):
        self.dradius = self.dradius + r
        return self.dradius

    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.dradius, fc=self.color))
        plt.axis('scaled')
        plt.show()
