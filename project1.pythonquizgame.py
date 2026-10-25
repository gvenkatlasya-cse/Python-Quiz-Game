#this is my first python project#
def ask_question(question,options,correct_answer):
    print()
    print(question)
    print(options)
    answer=input("Enter you Answer (A/B/C/D)").upper()
    if answer==correct_answer:
        print("Correct Answer,congratulations!")
        return 1
    else:
        print("Wrong Answer,loosed!")
        print("Correct Answer is:", correct_answer)
        return 0
def start_quiz():
    score=0
    print("WELCOME TO PYTHON QUIZE!TEST YOUR KNOWLEDGE")
    score=score + ask_question("1.What is python?","A.A Programming Language  B.A website  C.Computer hardware device  D.Operating system","A")
    score=score + ask_question("2.Which function displays output in python?", "A.scanf() B.input() C.print() D.int()","C")
    score=score + ask_question("3.Identify the data type from the following.","A.scanf() B.list  C.false D.print()","B")
    score=score + ask_question("4.Identify the keyword which is used for the conditional statement.","A.If  B.for  C.print  D.if","D")
    score=score + ask_question("5.Who created python?","A.Dennis Ritchie B.James Gosling  C.Guido van Rossum  D.Bill Gates","C")
    score=score + ask_question("6.Which one of the following is the feature of the python?","A.Easy-to-read syntax  B.It works only on one operating system  C.It cannot perform caluclations  D.It is used only for reading","A")
    score=score + ask_question("7.Which file extension is used for python files?","A. .cpp B. .py  C. .html  D. .java","B")
    score=score + ask_question("8.Which funtion is used to recieve input from the user?","A.print()  B.output() C.scan() D.input()","D")
    score=score + ask_question("9.Which symbol is used to write a single-line comment in python?","A.//  B.#  C./  D./* */","B")
    score=score + ask_question("10.Which of these is a valid python statement to display (Hello World!)?",'A.display("Hello World!")  B.print("Hello World!") C.echo("Hello World!")  D.input("Hello World!")',"B")
    print("QUIZ COMPLETED!\n")
    print("Your final score is:", score,"/10")
    if score>7:
        print("Excellent!")
    elif score>=5:
        print("Good Job!")
    else:
        print("Keep Practicing")
start_quiz()
    
