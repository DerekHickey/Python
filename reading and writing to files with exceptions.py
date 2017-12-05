##try:
####    count = 5/0
####    print(count)
##    count = 0
##
##    infile = open(r"C:\Users\dch67\Documents\mascots.txt", 'r')
##    #r at beginning means read as a raw string
##    c = infile.readline() #priming read
##
##    while c!="":
##        print(c.strip()) #strip away "whitespace" including end of line char
##        c = infile.readline()
##        count += 1
##    infile.close()
##
##except Exception as err: #all purpose exception
####    print(err)
####    
##except IOError as err:
##   print("oops!")
##   print(err)
##
##except:
##    print("other error")
##
##else:
##    print("there are ", count, "mascots in the file")
##
##finally:
##    print("we finally executed the block")
##    
##print("program finished")

#----------------------------------------------------

