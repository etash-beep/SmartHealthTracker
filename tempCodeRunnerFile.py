from user import registerUser,checkUserExists,getUserName
from health import addDailyHealthLog
from utils import printHeading
from graphs import showGraphMenu
from dashboard import viewDashboard
from reports import weeklyReport
from health_score import showHealthScore
from predictor import predictWeight
import pandas as pd

def main():
    if not checkUserExists():
        registerUser()

    name=getUserName()
    while True:
        showMenu(name)

        option=int(input("Enter your choice: "))
    
        if option==1:
            addDailyHealthLog()
        elif option==2:
            viewDashboard()
        elif option==3:
            showGraphMenu()
        elif option==4:
            showHealthScore()
        elif option==5:
            healthPrediction()
        elif option==6:
            weeklyReport()
        elif option==8:
            print("\nThank you for using Smart Health Tracker.")
            break
        else:
            print("\n⚠ Feature Coming Soon...\n")


def healthPrediction():
    health_df=pd.read_csv("data/health_logs.csv")
    latest_log=health_df.iloc[-1]
    calories=latest_log["Calories"]
    protein = latest_log["Protein_g"]
    water = latest_log["Water_L"]
    sleep = latest_log["Sleep_hr"]
    workout = latest_log["Workout_Min"]
    steps = latest_log["Steps"]
    current_weight=latest_log["Weight_kg"]
    
    predicted_weight = predictWeight(
        calories,
        protein,
        water,
        sleep,
        workout,
        steps
    )

    print("\n🤖 AI HEALTH PREDICTION")
    print("-" * 40)

    print("Based on your latest health log:\n")

    print(f"{'Calories':<20}: {calories} kcal")
    print(f"{'Protein':<20}: {protein} g")
    print(f"{'Water':<20}: {water} L")
    print(f"{'Sleep':<20}: {sleep} hr")
    print(f"{'Workout':<20}: {workout} min")
    print(f"{'Steps':<20}: {steps}")

    print("-" * 40)
    print(f"{'Predicted Weight':<20}: {predicted_weight:.2f} kg")
    print(f"{'Expected Change':<20}: {predicted_weight-current_weight:+.2f} kg")

    
def showMenu(name):

    printHeading()

    print(f"Welcome back, {name} 👋")
    print("1. Add Daily Health Log")
    print("2. View Dashboard")
    print("3. Generate Graphs")
    print("4. Health Score")
    print("5. Health Prediction (ML)")
    print("6. Weekly Report")
    print("7. Reset User")
    print("8. Exit")


if __name__=="__main__":
    main()