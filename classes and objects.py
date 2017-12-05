###===========Chapter 10 - Classes and Objects=====
##
###classes are "blueprints" for which objects or "instances" are created
###classes contain data attributes or variables and methods or functions that use those attributes for which
###the instantiated objects use, each object is "encapsulated" to prevent unauthorized
###changes to the object
###principles of oop include encapsulation, polymorphism, and inheritance
##
##import coin #coin.py on disk
##
##coin1 = coin.Coin()#create a coin object, instantiating the object
##coin2 = coin.Coin()
##coin3 = coin.Coin()
##
##tossvalue = coin1.get_sideup()
##
##print("before tossing: ", coin1.get_sideup(), coin2.get_sideup(),coin3.get_sideup())
##
##count = 1
##
##for i in range(0,5):
##
##    coin1.toss()
##
##    coin2.toss()
##
##    coin3.toss()
##
##    ##tossvalue = coin1.get_sideup()
##
##    print("after tossing",count,": ", coin1.get_sideup(), coin2.get_sideup(),coin3.get_sideup())
##
##    count += 1
##coinlist = [coin1, coin2, coin3]
##
##print(coinlist)
##
##print("Second item in the list: ", coinlist[1]) #returns the string method
##
###print(coin1)
##
##import pickle
##
##pfout = open('pickledcoin.dat', 'wb')# wb means write as binary file
##
##pickle.dump(coinlist, pfout)
##
##pfout.close()
##
##print("coins are pickled")
##
##pfin = open('pickledcoin.dat', 'rb')#can be used in another file without reinstantiating objects
##
##pickledcoin = pickle.load(pfin)
##
##print("pickledcoin: ", pickledcoin)
##
##for coinz in pickledcoin:
##    print(coinz.get_sideup())

import coin

cr = coin.Rarecoin()

print(cr)

print("initial country: ",cr.get_country())

cr.set_country("Russia")

print("new country: ", cr.get_country())



if isinstance(cr, coin.Coin) == True:
    print("i'm a Coin")
    if isinstance(cr, coin.Rarecoin) == True:
        print("i'm a rarecoin, too")

for i in range(2):
    
    print(cr.get_sideup())

    cr.toss()

coin_country = input('enter country of coin: ')

cr.set_country(coin_country)

print("coin country entry: ", cr.get_country())
