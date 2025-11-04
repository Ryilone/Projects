# if statments are statments that do some code only if some conditions are true
# Else do something else

Age = int(input("enter your age: "))

if Age >= 100:
    print("you are very old")
elif Age >= 18:
    print("you are now signed up!")
elif Age < 0:
    print("you have not been born yet dummy")
else:
    print("you must be 18+ to sign up")