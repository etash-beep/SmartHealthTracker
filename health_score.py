import pandas as pd
import os
from utils import calculateBMI
from utils import calculateTargetCalories,calculateMaintenanceCalories

def calculateBMIScore(bmi):
    if bmi>=18.5 and bmi<=24.9:
        return 20
    elif (bmi>=17 and bmi<=18.5 ) or (bmi>=25 and bmi<=27):
        return 15
    elif (bmi>=16 and bmi<17 ) or (bmi>27 and bmi<=30):
        return 10
    else:
        return 5
    
def calculateProteinScore(avg_protein):
    if avg_protein>=150:
        return 20
    elif 120<=avg_protein<150:
        return 15
    elif 90<=avg_protein<120:
        return 10
    else:
        return 5
    
def calculateWaterScore(avg_water):
    if avg_water>=3:
        return 15
    elif 2.5<=avg_water<3:
        return 10
    elif avg_water<2.5:
        return 5

def calculateSleepScore(avg_sleep):
    if avg_sleep>=8:
        return 15
    elif 7<=avg_sleep<8:
        return 10
    else:
        return 5

def calculateWorkoutScore(avg_workout):
    if avg_workout>=60:
        return 10
    elif 40<=avg_workout<60:
        return 7
    else:
        return 3
    
def calculateCalorieScore(avg_calories,target_calories):
    difference=abs(avg_calories-target_calories)
    if difference<=100:
        return 20
    elif difference<=250:
        return 15
    elif difference<=400:
        return 10
    else:
        return 5

def calculateHealthScore(health_df,user):
    bmi_score=calculateBMIScore(calculateBMI(health_df["Weight_kg"].iloc[-1],user['Height']))
    avg_protein=health_df["Protein_g"].mean()
    avg_water=health_df["Water_L"].mean()
    avg_sleep=health_df["Sleep_hr"].mean()
    avg_workout=health_df["Workout_Min"].mean()
    avg_calories=health_df["Calories"].mean()
    target_calories=round(calculateTargetCalories(calculateMaintenanceCalories(health_df["Weight_kg"].iloc[-1],user["Height"],user["Age"],user["Gender"],user["Activity Level"]),user["Fitness Goal"]))
   
    protein_score = calculateProteinScore(avg_protein)
    water_score = calculateWaterScore(avg_water)
    sleep_score = calculateSleepScore(avg_sleep)
    workout_score = calculateWorkoutScore(avg_workout)
    calorie_score = calculateCalorieScore(avg_calories, target_calories)

    total_score=bmi_score+protein_score+water_score+sleep_score+workout_score+calorie_score
    if total_score>=90:
        rating="Excellent"
    elif 75<=total_score<90:
        rating="Good"
    elif 60<=total_score<75:
        rating="Average"
    else:
        rating="Need Improvement"

    bmi=calculateBMI(health_df["Weight_kg"].iloc[-1],user['Height'])

    return {
        "total_score":total_score,
        "rating":rating,
        "bmi":bmi,
        "target_calories":target_calories,
        "average_calories":avg_calories,
        "bmi_score":bmi_score,
        "protein_score":protein_score,
        "water_score":water_score,
        "sleep_score":sleep_score,
        "workout_score":workout_score,
        "calorie_score":calorie_score
    }

def showHealthScore():
    if not os.path.isfile("data/health_logs.csv"):
        print("No health logs found.")
        return

    if not os.path.isfile("data/user_data.csv"):
        print("No user found.")
        return
    
    health_df=pd.read_csv("data/health_logs.csv")
    user_df=pd.read_csv("data/user_data.csv")
    user=user_df.iloc[0]
    scores=calculateHealthScore(health_df,user)

    print("\n🏆 HEALTH SCORE")
    print("-" * 40)

    print(f"{'Overall Score':<25}: {scores['total_score']} / 100")
    print(f"{'BMI Score':<25}: {scores['bmi_score']} / 20")
    print(f"{'Calorie Score':<25}: {scores['calorie_score']} / 20")
    print(f"{'Protein Score':<25}: {scores['protein_score']} / 20")
    print(f"{'Water Score':<25}: {scores['water_score']} / 15")
    print(f"{'Sleep Score':<25}: {scores['sleep_score']} / 15")
    print(f"{'Workout Score':<25}: {scores['workout_score']} / 10")
    print(f"{'Overall Rating':<25}: {scores['rating']}")