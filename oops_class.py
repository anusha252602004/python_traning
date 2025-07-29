class Person():
    cityName = "mumbai" 
    def printName(self,name):
        print(name)
class Anusha(Person):
    def printDetails(self):
        print("some message")
class day(Person):
    def printDetails(self):
        print("some message")
obj = Anusha()
obj.cityName = "new city"
obj.printName("Anusha")
obj = day()
obj.cityName = "new city"
obj.printName("day")