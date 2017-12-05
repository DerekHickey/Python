def summit(a,b):# a and b are parameters
    return a + b #value-returning function because of return

##print(summit(2,5) + 3)
##    #in parenthesis of function is the argument, used when function is called

#---------------------------------------------

##def greeting(): #value returning function
##    return 'Hello World!'
##
##print(greeting())
##
##def greeting():#does not return value
##    print('Hello World!')
##
##greeting

#---------------------------------------------

##cel = float(input("please enter a celsius temperature: "))
##
##fahren = (9/5)*cel + 32
##
##print('The farhenheit temperature conversion is ', format(fahren,'.02f'))

#------------------------------------------------
SALES_TAX = .0825 #python constant convention - not a 'true' constant


def conversion(celsius):
    #return 9/5*celsius + 32
    f = 9/5*celsius + 32
    return f
#the scope of f and celsius are function wide, are not defined outside of function
c = float(input("Enter a celsius temperature: "))

print('The farhenheit conversion is',format(conversion(c),'.1f'))

#---------------------------------------------------

##
##import random
##
##def rand(): #no argument function, no parameters
##    return random.randint(1,100)
##
##def main(): #non value returning function are called void functions
##    count = 0
##    while count < 7:
##        print(rand())
##        count += 1
##
##main()

#--------------------------------------------------





