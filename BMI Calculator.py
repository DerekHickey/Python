'''

Program 2

BMI calculator

This program was created by Derek Hickey

Texas State id A04654178

'''

yourname = input("please enter your name: ")

yourweight = int(input("please enter your weight in pounds: "))

yourheight = int(input("please enter your height in inches: "))

bmiscore = float(yourweight * 703/yourheight**2)

if bmiscore < 18.5:
    yourbmi = str("below normal")
else:
    if bmiscore >=18.5 and bmiscore < 25:
        yourbmi = str("normal")
    else:
        if bmiscore >=25:
            yourbmi = str("above normal")

print("Results for " + yourname)
print("Height: " + str(yourheight))
print("Weight: " + str(yourweight))
print("BMI: " + format(bmiscore, '.1f'))
print("your BMI is " + yourbmi)



##if bmiscore < 18.5:
##    yourbmi = str("below normal")
##elif bmiscore > 25:
##    yourbmi = str("above normal")
##else:
##        yourbmi = str("normal")
##
