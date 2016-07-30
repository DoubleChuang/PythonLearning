class Rectangle(object):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def perimeter(self):
        return 2 * (self.length+self.width)
    def area(self):
        return self.length * self.width

rec=Rectangle(4,2)
print rec.perimeter()
print rec.area()