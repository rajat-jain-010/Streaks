# if you are doing "n" que a day and i am doing "m" question a day then how much question one has to increment to bypass other by x question in d days
import math


def bypasser(noOfQuestionsP1, noOfQuestionsP2, days, bypassLimit,moreQuestionPerformer):
    totalQuestionDone = moreQuestionPerformer*days
    
    noOfQuestionTOBypass = bypassLimit + totalQuestionDone
    
    questionOtherHasToDo = noOfQuestionTOBypass/days
    
    roundOfValue = math.ceil(questionOtherHasToDo)
    
    print(f" mimimum {questionOtherHasToDo} or {roundOfValue} questions  daily to progress ahead by atleast {bypassLimit} questions in {days} days .")
    

p1Questions = int(input("how much quesion person one does ::> "))
p2Questions = int(input("how much quesion person one does ::> "))

moreQuestions = p1Questions if (p1Questions>p2Questions) else p2Questions

bypassLimit = int(input("how much more question u want in particular days enter question no ::> "))
days = int(input(f"how much days u need to bypass the other by {bypassLimit} questions ::> "))

bypasser(p1Questions, p2Questions, days, bypassLimit, moreQuestions)
