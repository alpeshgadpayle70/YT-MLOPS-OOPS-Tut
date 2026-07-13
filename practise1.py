# create a class
class Employee:
    #magic method, special method, dunder method
    def __init__(self):
        print("1")
        self.id = 123
        self.name = "Parag"
        self.salary = 50000
        print("2")

    #create a function/method
    def Travel(self,designation):
        print("3")
        print(f"The Employee designation is {designation}")


#create a obj
sam = Employee()

#calling a attributes
#print(sam.id)

#calling a method
sam.Travel("Nagpur")
