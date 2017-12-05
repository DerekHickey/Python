'''

Program 6 Written by Derek Hickey

'''

courses = {'CIS3389':['0342', 'Keefe', '10:00 a.m.'],'CS101':[3004, 'Haynes', '8:00 a.m.'],
           'CS102':[4501, 'Alvarado', '9:00 a.m.'],'CS103':[6755, 'Rich', '10:00 a.m.'],
           'NT110':[1244, 'Burke', '11:00 a.m.'], 'CM241':[1411, 'Lee', '1:00 p.m.']}


try:


        entry = input("Enter a course or enter n to quit: ").upper()
                
        while entry != 'N':

                    print('Course Number: ', entry)
                    print('Room Number: ', courses[entry][0])
                    print('Instructor: ', courses[entry][1])
                    print('Meeting Time: ', courses[entry][2])
                    entry = input("Enter another course or enter n to quit: ").upper()


except Exception as err:
        print('invalid course number')




    
    
