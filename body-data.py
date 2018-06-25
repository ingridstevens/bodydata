''' INPUTS (assuming imperial inputs) '''

gender = str(raw_input("Please enter your gender as 'MAN' or 'WOMAN' and press enter: ")).upper()
while gender.upper() not in ("MAN", "WOMAN"):
    print('    >> ERROR: Sorry, but you need to choose "man" or "woman"... Try Again')
    gender = str(raw_input("Please enter your gender as 'MAN' or 'WOMAN' and press enter: ")).upper()

weight = int(input("Please enter your weight in POUNDS and press enter: ")) / 2.2
height = int(input("Please enter your height in INCHES and press enter: ")) * 2.54
age = int(input("Please enter your age in YEARS and press enter: "))

body_fat_percentage = raw_input("If you know it, please enter your body fat % (if not, press enter): ")
if body_fat_percentage:
    body_fat_percentage = int(body_fat_percentage)
if not body_fat_percentage:
    body_fat_percentage = None

activity_level = str(raw_input("Please enter your activity level by typing one of the following options: 'Sedentary' 'Lightly Active' 'Moderately Active' 'Very Active' 'Extremely Active': ")).upper()

''' Calculating Thermal Effect of Food (calories burned from digestion) TEF '''
def calcTEF(rmr):
    tef = rmr * .01
    return tef

''' Calculating Physical Activity Factor PAF '''
def calcPAF(rmr):
    if activity_level == "SEDENTARY":
        paf = (rmr * 1.2) - rmr
    if activity_level == "LIGHTLY ACTIVE":
        paf = (rmr * 1.375) - rmr
    if activity_level == "MODERATELY ACTIVE":
        paf = (rmr * 1.55) - rmr
    if activity_level == "VERY ACTIVE":
        paf = (rmr * 1.725) - rmr
    if activity_level == "EXTREMELY ACTIVE":
        paf = (rmr * 1.9) - rmr
    return paf 

''' Calculating Resting Metabolic Rate RMR '''
def calcRMR():
    if body_fat_percentage is None:
        if gender == "MAN":
            rmr = ( weight*13.75 ) + ( height*5 ) - ( age*6.76 ) + 66
            calcTEF(rmr)
            calcPAF(rmr)
        if gender == "WOMAN":
            rmr = ( weight*9.56 ) + ( height*1.85 ) - ( age*4.68 ) + 655
            calcTEF(rmr)
            calcPAF(rmr)
    if body_fat_percentage is not None:
        rmr =  ( ( (100 - body_fat_percentage) * weight ) / 100 ) * 21.6 + 370
        calcTEF(rmr)
        calcPAF(rmr)
    return rmr

''' Calculating Total Daily Energy Expenditure '''
def calcTDEE():
    rmr = calcRMR()
    paf = calcPAF(rmr)
    tef = calcTEF(rmr)
    tdee = rmr + paf + tef 
    return tdee

''' Calculating Recommended Water Intake '''
def calcWaterIntake():
    min = weight*.5
    max = weight*.8 
    water_intake = ("You should drink a total of " +str(min) + " oz min and " +str(max)+" oz max of water each day")
    return water_intake

def printResults():
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

