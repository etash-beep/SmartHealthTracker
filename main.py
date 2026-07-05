import pandas as pd
import os
from datetime import datetime

def getTodayDate():
    return datetime.now().date()


def main():
    if not checkUserExists():
        registerUser()

    name=getUserName()
    while True:
        showMenu(name)

        option=int(input("Enter your choice: "))
    
        if option==1:
            health_data=addDailyHealthLog()
            saveHealthLog(health_data)
        elif option==7:
            print("Thank you for using Smart Health Tracker.")
            break
        else:
            print("Feature Coming Soon")

def getUserName():
    df=pd.read_csv("data/user_data.csv")
    return df["Name"].iloc[0]

def saveHealthLog(health_data):
    file_path="data/health_logs.csv"

    if not os.path.isfile(file_path):
        df=pd.DataFrame([health_data])
        df.to_csv(file_path,index=False)
        return
    else:
        df=pd.read_csv(file_path)
        today=getTodayDate()
        
        if today in df["Date"].values:
            choice = input("Today's log already exists. Update it? (Y/N): ")
            if choice.upper()=="Y":
                row=df[df["Date"]==today].index[0]
                df.loc[row]=health_data
                df.to_csv(file_path, index=False)
            else:
                return
        else:
            new_df=pd.DataFrame([health_data])
            df=pd.concat([df,new_df],ignore_index=True)
            df.to_csv(file_path, index=False)


def showMenu(name):

    print("="*40)
    print(" SMART HEALTH TRACKER ".center(40))
    print("="*40)

    print(f"Welcome back, {name} 👋")
    print("1. Add Daily Health Log")
    print("2. View Dashboard")
    print("3. Generate Graphs")
    print("4. Health Prediction (ML)")
    print("5. Weekly Report")
    print("6. Reset User")
    print("7. Exit")


def registerUser():
    name=input("Enter Name:")
    age=int(input("Enter Age:"))
    gender=input("Enter Gender:")
    height_cm=float(input("Enter Height:"))
    current_weight_kg=float(input("Enter Current Weight:"))
    goal_weight_kg=float(input("Enter Goal Weight:"))
    activity_level=input("Enter Activity Level:")
    fitness_goal=input("Enter yout fitness goal:")

    details={
        "Name":name,
        "Age":age,
        "Gender":gender,
        "Height_cm":height_cm,
        "Current_Weight_kg":current_weight_kg,
        "Goal_Weight_kg":goal_weight_kg,
        "Activity Level":activity_level,
        "Fitness Goal":fitness_goal
    }

    df=pd.DataFrame([details])
    df.to_csv("data/user_data.csv",index=False)

    print("\n User Registered Successfully")

def getUserName():
    df=pd.read_csv("data/user_data.csv")
    return df["Name"].iloc[0]

def addDailyHealthLog():
    date=getTodayDate()
    weight=float(input("Enter your weight in kgs:"))
    calories=int(input("Enter calories consumed:"))
    protein=int(input("Enter the amount of protein consumed today:"))
    carbs=int(input("Enter the amount of carbohydrates consumed today:"))
    fat=int(input("Enter the amount of fat consumed today:"))
    fiber=int(input("Enter the amount of fiber consumed today:"))
    water=float(input("Enter the amount of water consumed today:"))
    sleep=int(input("How many hours did you slept at night:"))
    workout=int(input("How many minutes did you workout today:"))
    steps=int(input("How many steps did you waled today:"))

    health_data={
        "Date":date,
        "Weight_kg":weight,
        "Calories":calories,
        "Protein_g":protein,
        "Carbohydrates_g":carbs,
        "Fats_g":fat,
        "Fiber_g":fiber,
        "Water_L":water,
        "Sleep_hr":sleep,
        "Workout_Min":workout,
        "Steps":steps
    }

    return health_data

def checkUserExists():
    file_path="data/user_data.csv"
    if os.path.isfile(file_path):
        df=pd.read_csv(file_path)
        if not df.empty:
            return True
    return False

if __name__=="__main__":
    main()
