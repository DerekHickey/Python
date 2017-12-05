## Program 5 Derek Hickey

try:
    
    name= input("Please enter the name of examinee: ")
    
    correct_answers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']

    i = 0

    infile = open("answers.txt", 'r')
        
    student_answers = infile.readlines()
    infile.close()


    correct = 0
    incorrect = 0
    incorrect_list = []

    while i < len(correct_answers):
        student_answers[i] = student_answers[i].rstrip("\n")
        
        if student_answers[i] == correct_answers[i]:
            correct +=1
            
        else:
            incorrect +=1
            incorrect_list.append(i+1)

        i += 1


    score = correct/(incorrect+correct)

    if score >= .75:
        message = "You passed the exam!"
    else:
        message = "Sorry, you did not pass the exam"
        
    print("Name of Examinee: ", name)

    print('Score: ', score* 100,"%")

    print(message)

    print("Number of correct: ", correct)

    print("Number of incorrect: ", incorrect)

    print("Questions missed: ", incorrect_list)

except IOError:
    print("file not found")

except Exception as err:
    print(err)

    

