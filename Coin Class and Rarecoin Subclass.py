import random

class Coin: #super or parent or base class

    def __init__(self):
        self.__sideup = 'Heads' #double underscore makes it private
    #initialization method called when constructor is called
        self.__country = 'US'
    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'
    #setter or mutator method, has an assignment operator

    def get_sideup(self):
        return self.__sideup
    #getter or accessor method, has a return keyword

    def __str__(self):
        return "Hi, I am a Coin object aren't I cute"

    def get_country(self):
        return self.__country

    def set_country(self, newcountry):
        self.__country = newcountry



#========================================

class Rarecoin(Coin):#inherits methods and variables of the Coin class
    #sub or derived class
    

    def __str__(self):
        return "I'm a rare coin, and I am special"
        #if no string method then coin's default string method will be called
        #method overriding, an example of runtime polymorphism
        #has an "is a" relationship with superclass

