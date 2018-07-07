
# def enum(**named_values):
#      return type('Enum', (), named_values)


# Gender = enum(MALE='male', FEMALE='female', N_A='n/a')



''' INPUTS (assuming imperial inputs) '''
print("BODY DATA CALCULATOR \n    >> You will be asked several questions about your gender, weight, height, age, and activity level. \nBased on your entries, the program will calculate results for you about your resting metabolic rate (RMR), \ntotal calorie expenditure, thermal effect of food, and how much water you should be drinking. \n Please note that we respect your privacy, this data is not saved.  \n")

gender = 'None'


# while gender not in (Gender.MALE, Gender.FEMALE, Gender.N_A):
#     gender = str(raw_input("What's Your Gender? \n    >> Please type your gender as 'MALE' or 'FEMALE' and press RETURN: "))
    # print checkGender()



def checkGender():
    if gender.upper()[0] == "M": 
        if gender.upper() == "MAN" or gender.upper() == "MALE":
            return 0
        else:
            return 'You entered ' + str(gender) + ' but I think you meant \'MAN\'...is that correct?'
    if gender.upper()[0] == "W":
        if gender.upper() == "WOMAN" or gender.upper() == "FEMALE":
            return 0
        else:
            return 'You entered ' + str(gender) + ' but I think you meant \'WOMAN\'...is that correct?'
    else:
        return '    >> ERROR: Sorry, but you need to choose "man" or "woman"... Try Again'


while checkGender() is not 0:
    gender = str(raw_input("What's Your Gender? \n    >> Please type your gender as 'MAN' or 'WOMAN' and press RETURN: "))
    print checkGender()

raw_weight = 1

def checkWeight():
    if (raw_weight > 40) and (raw_weight < 400):
        return 0
    else:
        return ("    >> ERROR: Normal weights are between 41 and 399. You appear to have entered: " + str(raw_weight))

while checkWeight() is not 0:
    raw_weight = int(input("What's Your Weight? \n    >> Please type your weight in POUNDS and press RETURN: ")) 
    print checkWeight()


raw_height = 1

def checkHeight():
    if (raw_height > 40) and (raw_height < 96):
        return 0
    else:
        return("    >> ERROR: Normal heights are between 40 inches and 96 inches. You appear to have entered: " + str(raw_height))

while checkHeight() is not 0:
    raw_height = int(input("What's Your Height? \n    >> Please type your height in INCHES and press RETURN: ")) 
    print checkHeight()

def calcBMI():
    bmi = ((raw_weight /2.2) / (raw_height * 0.0254)**2)
    return bmi

def checkBMI():
    bmi = calcBMI()

    if bmi > 13 and bmi < 85:
        print('Great, now that we have your height and weight, we can calculate your BMI: ')
        print(bmi)
        if bmi < 18:
            print('Your BMI puts you in the underweight category')
        if bmi >= 18 and bmi <25:
            print('You\'re BMI puts you in the normal category')
        if bmi >= 25:
            print('You\'re considered overweight.')

    else:
        print("    >> ERROR: Your BMI is " + str(bmi) + " which isn't in a normal range...please try again...: ")
        raw_weight = int(input("What's Your Weight? \n    >> Please type your weight in POUNDS and press RETURN: ")) 
        raw_height = int(input("What's Your Height? \n    >> Please type your height in INCHES and press RETURN: ")) 

checkBMI()

weight = raw_weight / 2.2
height = raw_height * 2.54

age = int(input("What's Your Age? \n    >> Please type your age in YEARS and press RETURN: "))

body_fat_percentage = raw_input("Do you know your Body Fat %? \n    >> If you know it, please type it as a value eg. '5'. If you don't know, press RETURN: ")
if body_fat_percentage:
    body_fat_percentage = int(body_fat_percentage)
if not body_fat_percentage:
    body_fat_percentage = None

activity_level = str(raw_input("How active are you? \n    >> Please type your activity level by typing one of the following options: \n    'Sedentary' 'Lightly Active' 'Moderately Active' 'Very Active' 'Extremely Active': ")).upper()


''' Calculating Thermal Effect of Food (calories burned from digestion) TEF '''
def calcTEF(rmr):
    tef = rmr * .01
    return round(tef, 2)

''' Calculating Physical Activity Factor PAF '''
def calcPAF(rmr):
    if activity_level[0] == "S":
        paf = (rmr * 1.2) - rmr
    if activity_level[0] == "L":
        paf = (rmr * 1.375) - rmr
    if activity_level[0] == "M":
        paf = (rmr * 1.55) - rmr
    if activity_level[0] == "V":
        paf = (rmr * 1.725) - rmr
    if activity_level[0] == "E":
        paf = (rmr * 1.9) - rmr
    return round(paf, 2)

''' Calculating Resting Metabolic Rate RMR '''
def calcRMR():
    if body_fat_percentage is None:
        if gender.upper()[0] == "M":
            rmr = ( weight*13.75 ) + ( height*5 ) - ( age*6.76 ) + 66
            calcTEF(rmr)
            calcPAF(rmr)
        if gender.upper()[0] == "W":
            rmr = ( weight*9.56 ) + ( height*1.85 ) - ( age*4.68 ) + 655
            calcTEF(rmr)
            calcPAF(rmr)
    if body_fat_percentage is not None:
        rmr =  ( ( (100 - body_fat_percentage) * weight ) / 100 ) * 21.6 + 370
        calcTEF(rmr)
        calcPAF(rmr)
    return round(rmr, 2)

# print calcRMR()

''' Calculating Total Daily Energy Expenditure '''
def calcTDEE():
    rmr = calcRMR()
    paf = calcPAF(rmr)
    tef = calcTEF(rmr)
    tdee = rmr + paf + tef 
    return round(tdee, 2)

''' Calculating Recommended Water Intake '''
def calcWaterIntake():
    min = weight*.5
    max = weight*.8 
    water_intake = ("You should drink a total of " +str(min) + " oz min and " +str(max)+" oz max of water each day")
    return water_intake

''' Print Results '''
def printResults():
    print("Thanks for taking the time to enter your information! None of your information has been saved; we respect your privacy. \n")
    rmr = calcRMR()
    print("Your Resting Metabolic Rate is " + str(rmr) + " calories.\n")
    paf = calcPAF(rmr)
    print("Because you are " + str(activity_level) + " your Physical Activity Calorie Burn is: " + str(paf) + "\n")
    tef = calcTEF(rmr)
    print("TEF (Thermal Effect of Food): " + str(tef) + " -- that's how many calories you burn just by digesting your food!\n")
    tdee = calcTDEE()
    print("Your total daily calorie expenditure is: " + str(tdee) +"\n")
    water = calcWaterIntake()
    print water

def calcBodyData():
    print("\n")
    printResults()
calcBodyData()

