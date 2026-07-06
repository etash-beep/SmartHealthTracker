from datetime import datetime
import pandas as pd
import os

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

    saveHealthLog(health_data)

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


def getTodayDate():
    return datetime.now().date()
