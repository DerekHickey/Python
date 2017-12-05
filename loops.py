'''

Jacopini & Bohm

presented paper at compsci conference in Israel in 1966

saying that all proper programs can be written using three control structures

known as the structured program theorem

1. sequence (executing one subprogram after another, ch.2)

2. selection (if then else, ch.3)

3. iteration (looping or repetition, ch.4)


pre-test loop is when condition is tested before loop statements are executed
post-test the condition is tested after loop statements, loop statements are run at least once



'''


##count = 0 #sentinel value or flag variable
##
##
##while count < 5:
##    print("count = ", count)
##    print("count x 2 = ", count*2)
####    count = count + 1
##    count +=1 #augmented assignment operation (include -=, *=, %=, etc.)
##print("Loop finished")

##do_again = 'y'
##while do_again == 'y':
##    sales = float(input("enter sales amount: "))
##    rate = float(input("enter commission rate: "))
##    comm = sales * rate
##
##    print("commission = ", comm)
##    do_again = input("compute another('y' for yes, 'n' for no)")

##print("hello\n " *10)
##
##print("*" *10)


##i = 10
##
##while i > 0:
##    print('*'*i)
##    i -=1
##    
##print('loop finished')
##
##
##i = 1
##
##while i < 11:
##    print('*'*i)
##    i +=1
##    
##print('loop finished')
##
##print('a','b', 'c', sep="--")


##for i in [1,2,3,4,5,6,7,8,9,10]: ## no need to increment with this list
##    print('*'*i)
##    ##i +=1
##    
##
##print("loop finished")
##
##for i in [10,9,8,7,6,5,4,3,2,1]: ## no need to increment with this list
##    print('*'*i)
##
##print("loop finished")
##
##
##for i in range(1,11):#does not include last number
##    print('*'*i)
##
##print ('loop finished')
##
##
##for school in ['txstate', 'ut', 'utsa', 'acc']:
##    #to create tuple use parentheses
##    #lists can mutable or changable, tuples are not
##    print(school)

##school_list1 = ['txstate','ut','utsa','acc']
##for school in school_list1:
##    print(school)
##
##
##for num in range(3, 37, 4):
##    print('num: ',num,'cube of num: ', format(num**3,',.0f'))
##    print("")
##


##for h in range(1,6):
##    print('Hello World!')
##
##
##for h in range(0,5):
##    print('Hello World!')
##
##for h in range(5):
##    print('Hello World!')

##for h in [1,2,3,4,5]:
##    print('Hello World!', end=" ")

##total = 0
##for h in range(1,11):
##    total = total + h**3
##    print('cube of ',h,'is ',h**3)
##
##print("total of the cubes is: ", format(total,',.0f'))
##

##total = 0 #accumulator variable
##num = 0
##do_again = 'y'
##
##while do_again == 'y':
##    num = float(input("Enter a number to add: "))
##    total += num
##    do_again = input("would you like to enter another number?")
##
##print("The total is ",total)

##total = 0 #accumulator variable
##num = 0
##avg = 0
##count = 0
##do_again = 'y'
##
##while do_again != 'n':
##    num = float(input("Enter a number to add: "))
##    count += 1
##    total += num
##    avg = (total/count)
##    do_again = input("would you like to enter another number?")
##
##print("The total is ",total)
##print("The average is ",avg)#or total/count


for i in [50, 100, 70, 102]:
    #print('score is: ', i, "Go Bobcats! "*3)
    print('score is: ', i, ':')
    for x in range(3):
        print('Go Bobcats!')
    
     






    


