class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print(f"{self.name} make sound") 
       
class Dog(Animal):
    def __init__(self,behaviour):
        self.behaviour=behaviour
    def speak(self):
        print(f"buddy barks.He is {self.behaviour}")
        
               
#animal=Animal("Genric Animal")
#animal.speak() 
dog=Dog("friendly")
dog.speak() 
    
   