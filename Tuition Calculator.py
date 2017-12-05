'''

Derek Hickey A04654178 Program 3 - CIS 3389

Based on the "College Tuition" program on page 163 of the text:

At one college, the tuition for a full-time student is $8,000 per semester. It has been

announced that the tuition will increase by 3 percent each year for the next 5 years. Write

a program with a loop that displays the projected semester tuition amount for the next 5

years.

In addition: 


Let the user input the current tuition amount, input the yearly growth rate, and number of years. 



'''


tuition =  float(input("Please enter your tuition per semester: "))

years = int(input("Please enter the number of years: "))

rate = float(input("Please enter the yearly growth rate: "))

count = 0

#print('Initial Tuition: ', tuition, 'Year: ', years)

for count in range(0,years+1):
    print('Projected Tuition: $', format(tuition,',.02f'), 'Year: ', count)
    ##count +=1
    tuition += (tuition * rate)
    
   
    
