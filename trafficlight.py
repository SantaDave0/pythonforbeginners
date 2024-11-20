#red, indigo and green
#color of the light
#red =stop
#green = go
#indigo = wait

color = input("enter the color: ")
if(color.lower() == "red"):
    print("STOP")

elif(color.lower() == "green"):
    print("GO")

elif(color.lower() == "indigo"):
    print("Wait")


else:
    print("invalid input")
    