class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def Display(self):
        print("name:",self.name)
        print("age:",self.age)
class Employee(Person):
    def __init__(self,name,age,empno,address):
        super().__init__(name,age)
        
        self.empno=empno;
        self.address=address;
    def Display(self):
        super().Display()
        print("Empno:",self.empno)
        print("Address:",self.address)
e1=Employee("shahala",20,103,"kerala")
e1.Display()
