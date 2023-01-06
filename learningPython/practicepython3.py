#IF,  IF-ELSE, IF-ELIF-ELSE STATEMEMTS
#Suppose you are a university student, and to pass the examination, you need to score 50 and above. If your score is 50 and above, print you have passed your exam

# IF STATEMENT

examScore = int(input("Enter your score:"))
if examScore >= 50: 
    print("You passed")
    print("Congratulations")

if examScore < 50:
    print("You failed")
    print("You can do better next time")

#IF-ELSE STATEMENT

examScore = int(input("Enter your score:"))
if examScore >= 50:
    print("You passed")
    print("Congratulations")

else:
    print("You failed")
    print("You can do better next time")

#IF-ELIF-ELSE

examScore = int(input("Enter your score:"))
if examScore > 100 or examScore < 0:
    print("Please enter a valid score between 0 - 100")

elif  examScore >= 50:
    print("You passed")
    print("Congratulations")

else:
    print("You failed")
    print("You can do better next time")




