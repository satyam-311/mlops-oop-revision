class Employe:
    def __init__(self):
        print(id(self))
        #print('started  to executing data or attributes')
        self.id = "smerf342"
        self.dep = "SDE"
        self.salary = 50000
        #print("Attribute are intiated")
    
    def travel(self,destination):
        print(f"employe is travelling to{destination}")    

sam = Employe()
print(id(sam))
"""
shaktimaan=Employe()
print(id(shaktimaan))
#sam.travel(' kerla')
#print(type(sam))
#print(sam.id)
#sam.travel(" kerla")
"""
sam.name="sam kumar"
print(sam.name)
       