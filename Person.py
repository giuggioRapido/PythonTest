class Person:
    def __init__(self, name):
        self.name = name

    def greet(self, person):
        print "Hi, " + person.name, "it's me, " + self.name + "."