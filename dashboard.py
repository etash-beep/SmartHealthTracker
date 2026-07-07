import pandas as pd
import os
from utils import printHeading,calculateBMI,calculateWeightRemaining,getBMICategory,calculateMaintenanceCalories,calculateTargetCalories

def viewDashboard():
    printHeading()

    user_df=pd.read_csv("data/user_data.csv")
    user=user_df.iloc[0]

    file_path="data/health_logs.csv"
    if not os.path.isfile(file_path):
        print("No health logs found")
        print("Please add today's health log first")
        return
    
    health_df=pd.read_csv(file_path)
    today=health_df.iloc[-1]

    print("\n🍽 TODAY'S HEALTH LOG")
    print("-" * 40)
    print(f"{'Calories':<20}: {today['Calories']} kcal")
    print(f"{'Protein':<20}: {today['Protein_g']} gm")
    print(f"{'Carbohydrates':<20}: {today['Carbohydrates_g']} gm")
    print(f"{'Fats':<20}: {today['Fats_g']} gm")
    print(f"{'Fiber':<20}: {today['Fiber_g']} gm")
    print(f"{'Water':<20}: {today['Water_L']} L")
    print(f"{'Sleep':<20}: {today['Sleep_hr']} hours")
    print(f"{'Workout:':20}: {today['Workout_Min']} minutes")
    print(f"{'Steps':<20}: {today['Steps']}")

    print("\n🏋 FITNESS INFORMATION")
    print("-" * 40)
    print(f"{'Current Weight':<20}: {today['Weight_kg']} kg")
    print(f"{'Goal Weight':<20}: {user['Goal Weight']} kg")
    print(f"{'Fitness Goal':<20}: {user['Fitness Goal']}")
    print(f"{'Activity Level':<20}: {user['Activity Level']}")
    bmi=calculateBMI(today["Weight_kg"],user["Height"])
    remaining=calculateWeightRemaining(today["Weight_kg"],user["Goal Weight"])
    print(f"{'Weight Remaining':<20}: {remaining} kg")
    category=getBMICategory(bmi)
    print(f"{'BMI':<20}: {bmi :.2f}")
    print(f"{'BMI Category':<20}: {category}")
    maintenance=calculateMaintenanceCalories(today["Weight_kg"],user["Height"],user["Age"],user["Gender"],user["Activity Level"])
    print(f"{'Maintenance Calories':<20}: {maintenance} kcal")
    target_calories=calculateTargetCalories(maintenance,user["Fitness Goal"])
    print(f"{'Target Calories':<20}: {target_calories} kcal")

    print("\n👤 USER INFORMATION")
    print("-" * 40)
    print(f"{'Name':<20}: {user['Name']}")
    print(f"{'Age':<20}: {user['Age']}")
    print(f"{'Height':<20}: {user['Height']} cm")

    