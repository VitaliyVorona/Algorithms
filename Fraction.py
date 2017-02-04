class Fraction:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, "/", self.y)

    def __srt__(self):
        return str(self.x) + "/" + str(self.y)

    def __add__(self):
        return self.x + self.y

    def __eq__(self, other):
        selfvalue = self.__add__()
        othervlue = other.__add__()
        if selfvalue < othervlue:
            return True
        elif selfvalue == othervlue: return "Equal"
        else:
            return False
