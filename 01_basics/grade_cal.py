score = int(input("Please enter your score: "))
if score > 33 and score < 60 :
    print("you are pass 'C' grade")
elif score >= 60 and score < 80 :
    print("you are pass 'B' grade")
elif score >= 80 and score < 90 :
    print("you are pass 'A' grade")
elif score >= 90 and score <= 100 :
    print("you are pass 'A+' grade")
elif score < 0 or score > 100 :
    print("Please enter a valid score")
else :
    print("you are fail")        
