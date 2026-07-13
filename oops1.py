# intiate a class
class employee:
    #special method/magic method/dunder method - constructor
    def __init__(self):
        print("started excuting attributes data\n")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("attributes/data have been intiated")
     
    #Create function/method
    def travel(self, designation):
        print("This travel function was called manually")
        print(f"Employee is now travelling to {designation}")

         
# creating an a obj/instance of the class
sam=employee() 

#printing the attributes
print(type(sam))

#calling a method  
#sam.travel("Kerela")