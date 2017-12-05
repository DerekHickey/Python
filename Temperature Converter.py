'''

Program 4 Programmed by Derek Hickey

'''



def conversion(x):
    f = (9/5)*x + 32
    return f

infile = open(r"C:\Users\cis_developer\Downloads\Celsius.txt", 'r')

c = infile.readline()

print("Celsius to Fahrenheit - Derek Hickey, programmer\n")
print("Celsius Temperature\tFahrenheit Temperature")

while c!="":
    celsius = float(c)
    print(format(celsius,'.01f'), "\t\t\t", format(conversion(celsius),'.01f'))
    c = infile.readline()

infile.close()




