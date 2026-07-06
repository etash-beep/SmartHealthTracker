def printHeading():
    print("="*40)
    print(" SMART HEALTH TRACKER ".center(40))
    print("="*40)

def calculateBMI(weight,height):
    height=height/100
    return float(weight/(height**2))

def calculateWeightRemaining(current_weight,goal_weight):
    return goal_weight-current_weight

def getBMICategory(bmi):
    if bmi<18.5:
        return "Underweight"
    elif bmi<25:
        return "Normal Weight"
    elif bmi<40:
        return "Overweight"
    else:
        return "Obese"
    
def calculateMaintenanceCalories(weight,height,age,gender,activity_level):
    activity_factors = {
    "Sedentary": 1.2,
    "Light": 1.375,
    "Moderate": 1.55,
    "Active": 1.725,
    "Very Active": 1.9
    }
    if gender=="Male":
        bmr=10*weight+6.25*height-5*age+5
    else :
        bmr=10*weight+6.25*height-5*age-161

    factor=activity_factors[activity_level]
    return round(bmr*factor)