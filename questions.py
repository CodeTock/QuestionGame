#questions, answers, guesses,check answer,
#-------------------
def new_game():
    guesses=[]
    correct_guesses= 0
    question_num= 1
    for key in questions:
        print("---------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess=input(" enter (A, B, C, or D): ")
        guess=guess.upper()
        guesses.append(guess)

        correct_guesses+=check_answer(questions.get(key),guess)
        question_num+=1
        display_score(correct_guesses,guesses)

#-------------------
def check_answer(answer,guess):
    if answer==guess:
        print("correct")
        return 1
    else:
        print("Wrong")
        return 0
#-------------------
def display_score(correct_guesses,guesses):
    print("----------------")
    print("RESULTS")
    print("----------------")

    print("Answers:",end=" ")
    for i in questions:
        print(questions.get(i),end=" ")
    print()
    print("Guesses:",end=" ")
    for i in guesses:
        print(i,end=" ")
    print()

    score=int((correct_guesses/len(questions))*100)
    print("Your score is " + str(score)+"%")

questions={
    "two times two?":"A",
    "'Tufan' How many letters does the name?":"B",
    "What is the capital city of Turkey?":"C",
    "You like this game?":"A"or"B"or"C"or"D"
}
options=[
    ["A. 4","B. 5","C. what is it?","D. 909090"],
    ["A. I don't know","B. 5","C. what the heck is this name?","D.This is awkward."],
    ["A.Tokyo","B. Berlin","C. Ankara","D. Pekin"],
    ["A.yes","B.yes","C.yes","D.yes"]
]
new_game()