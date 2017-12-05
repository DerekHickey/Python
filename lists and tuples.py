##list1 = [1,2,3]
##
##tuple1= (4,5,6)
##
##print(list1)
##
##print(tuple1)
##
##list2_from_tuple1 = list(tuple1)
##
##tuple2_from_list1 = tuple(list1)
##
##print(tuple2_from_list1)
##
##print(list2_from_tuple1)

##list3 = list1 + ['a','b']
##
##list4 = list1 *3
##
##print(list4)
##print(list3)


##print("length list1: ",len(list1))
##
##tot = sum(list1)
##
##print("total =",tot, "average= ", tot/len(list1))
##
##list5 = list1 + [4]
##
##print(list5)
##
##
####append
##
##list5.append(16)
##
##list6 = list5

##list7 = [2,5,8,9,4]
##
##print(list7)
##
##list7.sort()#permanently changes list
##
##print("low to high ", list7)
##
##list7.reverse()
##
##print("high to low ", list7)
##
##list8 = [12,5,18,9,14]
##
##print(sorted(list8))#sorted function does not permanently change list

list9 = ['txstate','ou','alabama','connecticut']

#list9.sort()

#print(list9)

#print(list9[2])
#print(list8 + list9)

##i = 0
##while i < len(list9):
##    print(list9[i])
##    i +=1
##x = 0
##
##while x <= len(list9) - 1:
##    print(list9[x])
##    x +=1
##
##for y in list9:
##    print(y)

#list9.remove('alabama')

##list10 = [38808, 31250, 37665, 32027]
##
##print(list9[0],list10[0])
##
##print(list9[1],list10[1])
##
##print(list9[2],list10[2])
##
##print(list9[3],list10[3])
##
##
##i = 0
##
##while i < len(list9):
##    print(list9[i], list10[i])
##    i += 1 
##
##for x in range(0,len(list9)):#will work without 0
##    print(list9[x],list10[x])
##
##print('average: ',format(sum(list10)/len(list10),',.0f'))
##print('lowest enrollment: ',format(min(list10),',.0f'))
##print('highest enrollment: ',format(max(list10),',.0f'))

##list11 = [i for i in range(1,51,2)] #list comprehension
##
##print(list11)
##
##print([i for i in range(1,51,2)if i % 7 == 0])#numbers divisible by 7



list12 = [[0]*3 for i in range(5)] #initialize two dimensional list

list12[3][1] = 17

print(list12)

print(list12[3])

list12[3] = 17

print(list12)

