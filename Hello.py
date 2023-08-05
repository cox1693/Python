print ("Hello")
print (5+3)
a=3
b=5
print (a+b)
for  n in range(0,50):
    print(n)
    if n % 2 == 1:
        print("odd")
    else:
        print("even")
fruitlist =["apple", "orange", "grape", "banana"]
for fruit in fruitlist:
    print(fruit)
c = 5 == 3
d=7>3
print (c)
print (d)
n=0
while n<50:
    print(n)
    n += 1
print (10+3)
y=10
b=3
print (y+b)
fruitlist=["kiwi","apple","pear"]
for fruit in fruitlist:
    print(fruit)
for  n in range(0,60):
    print(n)
    if n % 2 == 1:
        print("odd")
    else:
        print("even")


def addAandB(a,b):
    print("This is a function")
    return a+2*b 

print(addAandB(4,2))

file1 = open('database.txt', 'r')
Lines = file1.readlines()
print(Lines)

for line in Lines: 
  #  print(line)
    column = line.split(",")
   # print(column[1])
    if int(column[1]) > 25:
        print(line)
        
class MarvelSuperHero: #This is the object name

    #These are the attributes
    weight = 100
    Age= 10

    #There are the methods

    def __init__(self,name): #Constructor

        self.HeroName = name

    def Eat(self, kgofFood):
        self.weight = self.weight +kgofFood
        self.Age = 29
        Age1 = 20
        print(Age1)

    def Gain10Pounds(self):
        self.weight += 10

    #This is creating an object
Spiderman = MarvelSuperHero("Spiderman2")
print(Spiderman.HeroName)
print(Spiderman.Age)
Spiderman.Age= 55
print(Spiderman.Age)
print(Spiderman.weight)
Spiderman.weight= 250
print(Spiderman.weight)



