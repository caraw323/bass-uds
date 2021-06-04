print("Welcome to the Bass UDS randomiser")

PatientName = input("Please enter the patients full name: ")
OCL = input("Does " + PatientName + " have OCL? Y or N: ")
if OCL == "y":
    a = 1
elif OCL == "n":
    a = 0
else:
    OCL = input("Invalid answer. Does " + PatientName + " have OCL? Please type Y or N: ")
if OCL == "y":
    a = 1
elif OCL == "n":
    a = 0
Unesc = input("Does " + PatientName + " have unescorted OCL? Y or N: ")
if Unesc == "y":
    b = 1
elif Unesc == "n":
    b = 0
else:
    Unesc = input("Invalid answer. Does " + PatientName + " have unescorted OCL? Please type Y or N: ")
if Unesc == "y":
    b = 1
elif Unesc == "n":
    b = 0
Drughistory = input("Does " + PatientName + " have a history of substance use? Y or N: ")
if Drughistory == "y":
    c = 1
elif Drughistory == "n":
    c = 0
else:
    Drughistory = input("Invalid answer. Does " + PatientName + " have a history of substance use? Please type Y or N: ")
if Drughistory == "y":
    c = 1
elif Drughistory == "n":
    c = 0

if a == 1 and b == 1 and c == 1:
    print(PatientName + " needs to have a weekly UDS.")
    # add PatientName to List 1 (Weekly)
elif (a == 0 and b == 0 and c == 1) or (a == 1 and b == 0 and c == 1):
    print(PatientName + " needs to have a monthly UDS.")
    # add PatientName to List 2 (Monthly)
elif a == 1 and b == 1 and c == 0:
    print(PatientName + " needs to have a 3 monthly UDS.")
    # add PatientName to List 3 (3Monthly)
else:
    print(PatientName + " needs to have a 6 monthly UDS.")
    # add PatientName to List 4 (6Monthly)
