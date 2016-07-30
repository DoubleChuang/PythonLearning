class Cat(object):
    def __init__(self, name):
        self.name=name
    def shout(self):
        print 'Meow'
    def rename(self,new_name):
        self.name=new_name
    def introduce_my_self(self):
        print 'Hello,my name is {0}!'.format(self.name)

my_cat=Cat('Kitty')
print my_cat.name
my_cat.shout()
my_cat.introduce_my_self()
