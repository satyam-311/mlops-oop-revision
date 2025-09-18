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
              
            
        