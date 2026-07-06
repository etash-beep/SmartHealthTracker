import pandas as pd
import os

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

def checkUserExists():
    file_path="data/user_data.csv"
    if os.path.isfile(file_path):
        df=pd.read_csv(file_path)
        if not df.empty:
            return True
    return False

def getUserName():
    df=pd.read_csv("data/user_data.csv")
    return df["Name"].iloc[0]