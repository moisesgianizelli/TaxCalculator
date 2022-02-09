
def mortgagePayment():
    rate = 0.05 / 12
    durationInMonths = 30.0 * 12

    loan = float(input("enter the amount of the loan you have taken out:"))

    formulaPart1 = loan * rate
    formulaPart2 = (1 + rate) ** durationInMonths
    formulaPart3 = (1 + rate) ** durationInMonths - 1

    mortgage = formulaPart1 * formulaPart2 / formulaPart3
    return mortgage


# asks and stors the county you live in.
def propertyLocation():
    location = input("What county do you live in:")
    return location


# ask if you live in a private house or a social house.
def privateOrSocialHouse():
    isHouseSocialOrPrivate = input("Enter if your house is a private house or a social house:")
    return isHouseSocialOrPrivate


# checks if your property is in dublin or not and calculates allowance if needed.
def allowancesPropertyLocation():
    personsPropertyLocation = propertyLocation()

    if personsPropertyLocation == 'dublin' or personsPropertyLocation == 'Dublin':
        propertyValue = float(input("enter the value of your property:"))
        if propertyValue < 500000:
            allowancesFromThePropertyValue = propertyValue * 0.154


        else:
            allowancesFromThePropertyValue = propertyValue * 0.082

    else:
        allowancesFromThePropertyValue = 0

    return allowancesFromThePropertyValue


# calculates allowance based on 3 times the morage of a houes if the house is a private house.
def allowanceFromMonthlyPayment():
    typeOfHouse = privateOrSocialHouse()

    if typeOfHouse == 'private' or typeOfHouse == 'Private':

        monthlyMortgagePayment = mortgagePayment()

        allowancesFromMonthlyPayment = monthlyMortgagePayment * 3

    else:
        allowancesFromMonthlyPayment = 0

    return allowancesFromMonthlyPayment


# add up the allowances and prints them out to two decimal places.
def totalAllowances():
    mortgageAllowancePayment = allowanceFromMonthlyPayment()
    propertyValueAllowance = allowancesPropertyLocation()

    if (mortgageAllowancePayment == 0 and propertyValueAllowance == 0):
        formatedTotalAllowance = 0

    elif (mortgageAllowancePayment == 0 and propertyValueAllowance > 0):
        totalAllowance = mortgageAllowancePayment + propertyValueAllowance
        formatedTotalAllowance = format(totalAllowance, ".2f")

    elif (mortgageAllowancePayment > 0 and propertyValueAllowance == 0):
        totalAllowance = mortgageAllowancePayment + propertyValueAllowance
        formatedTotalAllowance = format(totalAllowance, ".2f")


    elif (mortgageAllowancePayment > 0 and propertyValueAllowance > 0):
        totalAllowance = mortgageAllowancePayment + propertyValueAllowance
        formatedTotalAllowance = format(totalAllowance, ".2f")

    return formatedTotalAllowance


# calculates the property tax and desplays it to the nearist euro.
def propertyTax():
    propertyTax = float(input("Enter the amount your property costs: "))

    if (propertyTax <= 300000):
        totalTaxDue = propertyTax * 0.002
        formattotalTaxDue = format(totalTaxDue, ".0f")

    elif (propertyTax > 300000 and propertyTax <= 500000):
        totalTaxDue = propertyTax * 0.0025
        formattotalTaxDue = format(totalTaxDue, ".0f")

    elif (propertyTax > 500000 and propertyTax <= 1000000):
        totalTaxDue = propertyTax * 0.003
        formattotalTaxDue = format(totalTaxDue, ".0f")

    elif (propertyTax > 1000000):
        totalTaxDue = propertyTax * 0.0035
        formattotalTaxDue = format(totalTaxDue, ".0f")
    return formattotalTaxDue


def mainPropertyTax():
    print("Calculate your allowance. ")
    theTotalAllowance = totalAllowances()

    print("Calculate your property tax.")
    yourPropertyTax = propertyTax()

    print("your property tax is:")
    print("€", yourPropertyTax)

    print("your allowancs is:")
    print("€", theTotalAllowance)


# this function is used to process the calculations of the transportation for students.
def processtransportcost():
    loopForFirstLevelStudentKm = True
    loopForSecondLevelStudentKm = True
    loopForFirstLevelStudents = True
    loopForSecondLevelStudents = True
    firstlevelstudentsnumber = 0
    secondlevelstudentsnumber = 0
    totaltransportcost = 0
    firstLevelfamilyAllowance = 390
    secondLevelfamilyAllowance = 940
    firstLevelMinKm = 3.2
    secondLevelMinkm = 4.8

    # this loop will read in the number of students for first level
    while loopForFirstLevelStudents == True:
        try:
            firstlevelstudentsnumber = int(input("Enter Number of First Level Students "))

            if firstlevelstudentsnumber >= 0:
                loopForFirstLevelStudents = False
            elif (firstlevelstudentsnumber < 0):
                print("You must enter a Valid Number")
        except ValueError:
            print("You must enter a Valid Number")
            # this loop will read in the km for first level students
    while loopForFirstLevelStudentKm:
        try:
            firstLevelstudentsKm = float(input("Enter First Level students Km or -1 to finish "))
            if firstLevelstudentsKm < firstLevelMinKm and firstLevelstudentsKm > 0:
                firstlevelstudentsnumber -= 1
                print("Student do not Qualify for subsidised Transport ")
            if firstLevelstudentsKm < -1:
                print("You must enter a Valid Number ")
            elif firstLevelstudentsKm == -1:
                loopForFirstLevelStudentKm = False
        except ValueError:
            print("You must enter a Valid Number ")
            break
            # this loop will read in the number of students for second level
    while loopForSecondLevelStudents == True:
        try:
            secondlevelstudentsnumber = int(input("Enter Number of Second Level Students "))
            if secondlevelstudentsnumber >= 0:
                loopForSecondLevelStudents = False
            elif (secondlevelstudentsnumber < 0):
                print("You must enter a Valid Number ")
        except ValueError:
            print("You must enter a Valid Number ")
            # this loop will read in the km for second level students
        while loopForSecondLevelStudentKm:
            try:
                secondLevelstudentsKm = float(input("Enter Second Level students Km or -1 to finish "))
                if secondLevelstudentsKm < secondLevelMinkm and secondLevelstudentsKm > 0:
                    secondlevelstudentsnumber -= 1
                    print("Student do not Qualify for subsidised Transport ")
                if secondLevelstudentsKm < -1:
                    print("You must enter a Valid Number ")
                elif secondLevelstudentsKm == -1:
                    loopForSecondLevelStudentKm = False
            except ValueError:
                print("You must enter a Valid Number ")

                # thi block of code will calculate the total owed and display it together with the savings if there is any
        if firstlevelstudentsnumber <= 2 and secondlevelstudentsnumber <= 2:
            totaltransportcost = firstlevelstudentsnumber * 100 + secondlevelstudentsnumber * 350
            print("The Amount Due is ", totaltransportcost)
            return

        elif firstlevelstudentsnumber >= 3 and secondlevelstudentsnumber >= 3:
            firstlevelstudentsnumber -= 2
            secondlevelstudentsnumber -= 2
            totaltransportcost = firstlevelstudentsnumber * 80 + 200 + secondlevelstudentsnumber * 300 + 700
            savings = totaltransportcost - secondLevelfamilyAllowance
            print("The Amount Due is ", secondLevelfamilyAllowance, "You are saving", savings)
            return

        elif firstlevelstudentsnumber > 0 and secondlevelstudentsnumber >= 3:
            firstlevelstudentsnumber -= 2
            secondlevelstudentsnumber -= 2
            totaltransportcost = firstlevelstudentsnumber * 80 + 200 + secondlevelstudentsnumber * 300 + 700
            savings = totaltransportcost - secondLevelfamilyAllowance
            print("The Amount Due is ", secondLevelfamilyAllowance, "You are saving", savings)
            return

        if firstlevelstudentsnumber > 2 and firstlevelstudentsnumber <= 4:
            firstlevelstudentsnumber -= 2
            totaltransportcost = firstlevelstudentsnumber * 80 + 200
            print("The Amount Due is ", totaltransportcost)
            return

        elif firstlevelstudentsnumber >= 5:
            firstlevelstudentsnumber -= 2
            totaltransportcost = firstlevelstudentsnumber * 80 + 200
            savings = totaltransportcost - firstLevelfamilyAllowance
            print("The Amount Due is ", firstLevelfamilyAllowance, "You are saving", savings)
            return

        if secondlevelstudentsnumber <= 2:
            totaltransportcost += secondlevelstudentsnumber * 350
            print("The Amount Due is ", totaltransportcost)

        elif secondlevelstudentsnumber >= 3:
            secondlevelstudentsnumber -= 2
            totaltransportcost = secondlevelstudentsnumber * 300 + 700
            savings = totaltransportcost - secondLevelfamilyAllowance
            print("The Amount Due is ", secondLevelfamilyAllowance, "You are saving", savings)

        elif firstlevelstudentsnumber <= 2:
            totaltransportcost += firstlevelstudentsnumber * 100
            print("The Amount Due is ", totaltransportcost)

        # calling the Function


def mainProcesstransporcost():
    processtransportcost()



# Set function
def usageCalculation():

    BASIC_USAGE = 213000
    FIVE_OR_MORE_ADULTS_EXTRA_USAGE = 30000
    CHARGE_RATE = 3.70

    litresConsumption = float(input("Enter in litres household consumption: "))
    numberOfAdults = int(input("Enter number of adults: "))
    numberOfChildren = int(input("Enter number of children: "))
    basicUsage = BASIC_USAGE
    # put allowance
    if numberOfAdults >= 5:
        basicUsage += FIVE_OR_MORE_ADULTS_EXTRA_USAGE
        if numberOfChildren - 2 > 0:
            basicUsage += (numberOfChildren - 2) * 5000
    elif numberOfAdults >= 3:
        basicUsage += 20000
        if numberOfChildren - 2 > 0:
            basicUsage += (numberOfChildren - 2) * 7000
    #set math
    extraUsage = litresConsumption - basicUsage
    chargeBepaid = extraUsage * CHARGE_RATE
    if chargeBepaid < 0:
        chargeBepaid = 0
    #print variables

    print("")
    print("Note: There is no charge if the volume does not excess basic usage + allowances")
    print("")
    print("##  You have consumed: ", litresConsumption, "Litres")
    print("##  Your allowance is: ", basicUsage, "Litres")
    print("##  Charge to be paid in euro: ", "€", format(chargeBepaid, ".2f"))
    print("")

def mainUsageCalculation():
    usageCalculation()

def main():
    # opening banner
    print("###############################")
    print("# Choose which program to run #")
    print("###############################")

    print("Type 1 for Property Tax.")
    print("Type 2 for School Transport.")
    print("Type 3 for Water Charges.")

    programChoise = int(input("Please enter 1,2 or 3 :"))

    # 1,2 or 3 is inputted and depending on the input it will pick one of the three options below.

    if programChoise == 1:
        print("You have chosen property tax.")
        mainPropertyTax()
    elif programChoise == 2:
        print("You have chosen school transport.")
        mainProcesstransporcost()
    elif programChoise == 3:
        print("you have chosen water charge.")
        mainUsageCalculation()

    runAgain = input(print("Would You like to use the other programs available : [yes,no]"))
    # if the input is yes the code will be run again if no it will print the closing tag.
    if runAgain == 'yes' or runAgain == 'Yes':
        main()
        # the closing tag.
    else:
        print("thank you for using this prosram ")
        print("###############################")
        print("#          GOOD BYE           #")
        print("###############################")


main()
