"""
class Animal:
    def __init__(self):
        self.name="zimbo"
    def speak(self):
        print(f"{self.name} makes sound")
class Dog(Animal):
    def __init__(self,breed):
        super().__init__()
        self.breed=breed
    def speak(self):
        super().speak()
        print(f"{self.name} barks.it is {self.breed}")

dog=Dog("Golden Retriever")
dog.speak()
"""

"""
class grandfather:
    def __init__(self,name):
        self.name=name
    def story(self):
        print(f"{self.name} tell a story")
class parent(grandfather):
    def play(self):
        print(f"{self.name} is playing cassino")
class child(parent):
    def study(self):
        print(f"{self.name} is studying for mbbs")
a=child("charlie puth")
b=parent("papa")
c=grandfather("grandpa")
a.study()
b.play()
c.story()
"""
import math
class area:
    def __init__(self,a=None,r=None):
        self.a=a
        self.r=r
class area_of_circle(area):
    def ac(self):
        return math.pi*self.r*self.r
class area_of_square(area):
    def a_s(self):
        return self.a*self.a  

area_circle=area_of_circle(r=4)
area_square=area_of_square(a=2)

print(area_circle.ac())
print(area_square.a_s())