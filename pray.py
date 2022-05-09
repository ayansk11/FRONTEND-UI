class Birds:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Sparrow', 'Robin', 'Duck']
 
 
    def printMembers(self):
        print('Printing members of the Birds class')
        for member in self.members:
           print('\t%s ' % member)


from animal import Mammals
from animal import Birds
from animal import Flowers
 
# Create an object of Mammals class & call a method of it
myMammal = Mammals()
myMammal.printMembers()
 
# Create an object of Birds class & call a method of it
myBird = Birds()
myBird.printMembers()

myFlow=Flowers()
myFlow.printMembers()


class meth_overload:

    def product(self,a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            print( "Area of the triangle =", a*b*c)
        elif a!=None and b!=None:
            print( "Area of the rectabngle =", a*b)
        elif a!=None:
            print( "Area of the circle", a*a*3.14)
            
obj=meth_overload()
obj.product(3.2)
obj.product(3,5)
obj.product(3, 6, 6)

class Sample:

   x=20
   @classmethod
   def modify(cls):
      print(" I am in modify function:",cls.x)
      cls.x+=1
      
s1=Sample()
s2=Sample()
print( " X in S1" ,s1.x)
print( " X in S2" ,s2.x)
s1.modify()
print( " X in S1" ,s1.x)
print( " X in S2" ,s2.x)
s2.modify()
print( " X in S1" ,s1.x)
print( " X in S2" ,s2.x)

class Person:

    def _init_(self, first, last):
        self.firstname = first
        self.lastname = last
    def Name(self):
        return self.firstname + " " + self.lastname

class Student(Person):

    def _init_(self, first, last, id):
        Person._init_(self,first, last)
        self.id = id
    def getStudent(self):
        return self.Name() + ", " +  self.id

p = Person("Zeenat", "Khan")
e = Student("Sarah", "Shaikh", "25")

print(p.Name())
print(e.getStudent())
print(e.Name())

class Father:

    def _init_(self,property1=0):
        self.property1=property1

def display(self):
        print( "\nFather's property",self.property)

class Son(Father):

    def _init_(self,property1=0,property2=0):
        super()._init_ (property1)
        self.property2=property2

    def display(self):
         print( "\nSon's property =",self.property1 + self.property2)
         
s=Son(2000000,300000)
s.display()
