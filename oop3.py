class Person:
    #class attribute
    #name = "Tesh"
    #age = 15
    #nationality ="Kenya"

#constructor concept/defining a constructor
    def __init__(self,name,age,nationality):
        print("This is constructor")
        self.name= name
        self.age = age
        self.nationality = nationality

    def full_details(self):
        return(f"{self.name} is {self.age}years and lives in {self.nationality}")
#print(Person.name)    

details = Person("Tesh","15","Kenya")
print(details.name)
print(details.age)
print(details.nationality)
print(details.full_details())



