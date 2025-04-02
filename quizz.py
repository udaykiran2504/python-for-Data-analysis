def quiz():
    score = 0
    while True:
        print('welcome to the quizzz ')
        score = 0
        print("answer the following MCQ")
        print('question1: what is the captial city of india?\nA.delhi\nB.hydrabad\nC.vizag\nD,bihar')
        ans1 = input("enter your answer:")
        if ans1 == "a" or ans1 == "A":
            score = score + 1
            print("correct answer your score is ", score)
        else:
            score = score - 1
            print("wrong answer your score is :", score)
        print('question2: who is the PM of india ?\nA.N.modi\nB.A.arjun\nC.G.mahesh babu \nD.D.udaykiran')
        ans2 = input("enter your answer:")
        if ans2 == "a" or ans1 == "A":
            score = score + 1
            print("correct answer your score is ", score)
        else:
            score = score - 1
            print("wrong answer your score is :", score)
        print('question3: who is the PM of india ?\nA.N.modi\nB.A.arjun\nC.G.mahesh babu \nD.D.udaykiran')
        ans2 = input("enter your answer:")
        if ans2 == "a" or ans1 == "A":
            score = score + 1
            print("correct answer your score is ", score)
        else:
            score = score - 1
            print("wrong answer your score is :", score)
        print('question4: who is the PM of india ?\nA.N.modi\nB.A.arjun\nC.G.mahesh babu \nD.D.udaykiran')
        ans3 = input("enter your answer:")
        if ans3 == "a" or ans3 == "A":
            score = score + 1
            print("correct answer your score is ", score)
        else:
            score = score - 1
            print("wrong answer your score is :", score)
        print('question5: who is the PM of india ?\nA.N.modi\nB.A.arjun\nC.G.mahesh babu \nD.D.udaykiran')
        ans4 = input("enter your answer:")
        if ans4 == "a" or ans4 == "A":
            score = score + 1
            print("correct answer your score is ", score)
        else:
            score = score - 1
            print("wrong answer your score is :", score)
        a = input('do you wnat  to take retest yes or no: ')
        if a == 'NO' or a == "no":
            print('quizz of over, thank you for talking the test ')
            break

quiz()


