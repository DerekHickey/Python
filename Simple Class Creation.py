'''

Program 7 by Derek Hickey

'''


import random

class Coin: 

    
   

    def __init__(self):
        self.__sideup = 'Heads'
        self.__programmer = 'CIS Student'
    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'
    

    def get_sideup(self):
        return self.__sideup
    

    def set_programmer(self, prog):
        self.__programmer = prog
        
    def get_programmer(self):
        return self.__programmer
