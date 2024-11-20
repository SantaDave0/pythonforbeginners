#make a program that checks whether a user is male or female

#gender, male, female and transgender
#create a variable called gender
gender = input("enter your gender: ")
if(gender == "male"):
    print("user is a man")
elif(gender == "transgender"):
    print("user is transgender")
else:
    print("the user is a woman")