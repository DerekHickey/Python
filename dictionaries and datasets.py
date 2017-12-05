##list9 = ['txstate', 'ou', 'alabama','connecticut']
##list10 = [38808, 31250, 37665,32027]
##for i in range(0,len(list9)):
##    print(list9[i], format(list10[i],',.0f'))
##
##
##print('average: ',format(sum(list10)/len(list10),',.0f'))
##print('lowest enroll: ',format(min(list10),',.0f'))
##print('highest enroll: ',format(max(list10),',.0f'))
##


#==========================dictionaries===========================

##d1 = {'txstate':38808, 'ou':31250, 'alabama':37665,'connecticut':32027}
##        #key    value
###dictionary is a set of key value pairs
##
##d1['arkansas'] = 5000
##
##print('d1 = ', d1)
##
##school = input("input your school: ").strip()
##
##print(school)
##
##
##print('enrollment of ', school, 'is ', format(d1[school],',.0f'))
##
##
##try:   
##
##    newschool = input("Enter a new school: ").strip()
##
##    enrollment = int(input("input the school's enrollment: ").strip())
##
##    print(newschool, enrollment)
##
##    d1[newschool] = enrollment
##
##    print(d1)
##
##    print(d1.keys())
##
##    print(d1.values())
##
##    print(d1.items())#returns a list of tuples, each key value pair is a tuple in the list
##
##    d1.clear()
##
##    print(d1)
##    
##except Exception as err:
##    print(err)
##
#============

##d2 = {'tx':[28,17,10],'ca':[40,30,20]}
##
##d2['ny'] = [19,15,5]
##
##
##print(d2)
##
##print(d2.keys())
##
##print(d2.values())
##
###del d2['ca']
##
##print(d2)
##
##state = input('enter a state abbreviation: ')
##
##print('the population of ',state, ' in the 1990 is: ', d2[state][2])

#====================serialization

##import pickle
##
##pfout = open('picklefile.dat', 'wb')
##
##pickle.dump(d2, pfout)
##
##pfout.close()
##
##print("All pickled")
##
##pfin = open('picklefile.dat', 'rb')
##
##pickledd1 = pickle.load(pfin)
##
##print("pickled d1: ", pickledd1)
##
##print(pickledd1['ny'])
##
##pfin.close()


#==========================

l1 = ['curly','larry','moe','larry']

print(l1)

set1 = set(l1)

print(set1)

set2 = {200,100,300}

print(set2)

set1.update(set2)

print(set1)

set3 = set1

print(set3)

#=================================

set4 = {'curly', 'shemp', 'larry'}
set5 = {'curly', 'moe', 'larry'}

##set6 = set4.union(set5)
set6 = set4 | set5

print('set 4: ',set4)
print('set 5: ',set5)
print('set 6-union: ',set6)

##set7 = set4.intersection(set5)

set7 = set4 & set5

print('set 7-intersection: ',set7)

##set8 = set4.difference(set5)
#what is in set 4 but not set 5
set8 = set4 - set5
print('set 8-difference: ',set8)

##set9 = set5.difference(set4)
#what is in set 5 but not set 4
set9 = set5-set4
print('set 9-difference: ',set9)

##set10 = set4.symmetric_difference(set5)
#the differences in both sets

set10 = set4 ^ set5
#caret symbol

print('set 10-symmetric difference: ',set10)

#set is a collection that is mutable

