import pandas as pd
import os
from datetime import datetime,timedelta
from utils import printHeading,calculateTargetCalories,calculateMaintenanceCalories


def weeklyReport():
    printHeading()
    print("\n📅 REPORT SUMMARY")
    print("-" * 40)
    file_path="data/health_logs.csv"
    if not os.path.isfile(file_path):
        print("There are no health logs")
        return
    
    health_df=pd.read_csv(file_path)
    health_df["Date"] = pd.to_datetime(health_df["Date"]).dt.date
    latest_date = health_df["Date"].max()
    last_week = latest_date - timedelta(days=6)
    weekly_df = health_df[health_df["Date"] >= last_week]

    if weekly_df.empty:
        print("No health logs found for the last 7 days.")
        return
    
    user_df=pd.read_csv("data/user_data.csv")
    user=user_df.iloc[0]

    from_date=weekly_df["Date"].iloc[0]
    to_date=weekly_df["Date"].iloc[-1]
    days_logged=weekly_df["Date"].count()

    print(f"{'From':<20}: {from_date}")
    print(f"{'To':<20}: {to_date}")
    print(f"{'Days Logged':<20}: {days_logged}")
    nutritionSummary(weekly_df)
    fitnessSummary(weekly_df)
    weightAnalysis(weekly_df)
    reportHighlights(weekly_df)
    goalComparison(weekly_df,user)
    weeklyInsights(weekly_df,user)

def nutritionSummary(health_df):
    avg_calories=round(health_df["Calories"].mean())
    avg_protein=round(health_df["Protein_g"].mean())
    avg_carbs=round(health_df["Carbohydrates_g"].mean())
    avg_fats=round(health_df["Fats_g"].mean())
    avg_fiber=round(health_df["Fiber_g"].mean())
    
    print("\n🍽 NUTRITION")
    print("-" * 40)
    print(f"{'Average Calories':<25}: {avg_calories} kcal")
    print(f"{'Average Protein':<25}: {avg_protein} g")
    print(f"{'Average Carbohydrates':<25}: {avg_carbs} g")
    print(f"{'Average Fats':<25}: {avg_fats} g")
    print(f"{'Average Fiber':<25}: {avg_fiber} g")

def fitnessSummary(health_df):
    avg_water=round(health_df["Water_L"].mean(),1)
    avg_sleep=round(health_df["Sleep_hr"].mean())
    avg_workout=round(health_df["Workout_Min"].mean())
    avg_steps=round(health_df["Steps"].mean())

    print("\n💪 FITNESS")
    print("-" * 40)
    print(f"{'Average Water':<25}: {avg_water} L")
    print(f"{'Average Sleep':<25}: {avg_sleep} hr")
    print(f"{'Average Workout':<25}: {avg_workout} min")
    print(f"{'Average Steps':<25}: {avg_steps}")

def weightAnalysis(health_df):
    print("\n⚖ WEIGHT ANALYSIS")
    print("-" * 40)

    starting_weight=health_df["Weight_kg"].iloc[0]
    current_weight=health_df["Weight_kg"].iloc[-1]
    highest_weight=health_df["Weight_kg"].max()
    lowest_weight=health_df["Weight_kg"].min()
    weight_change=current_weight-starting_weight

    print(f"{'Starting Weight':<25}: {starting_weight} kg")
    print(f"{'Current Weight':<25}: {current_weight} kg")
    print(f"{'Highest Weight':<25}: {highest_weight} kg")
    print(f"{'Lowest Weight':<25}: {lowest_weight} kg")
    print(f"{'Weight Change':<25}: {weight_change} kg")

def reportHighlights(health_df):
    print("\n📈 HIGHLIGHTS")
    print("-" * 40)

    highest_calories = health_df["Calories"].max()
    lowest_calories = health_df["Calories"].min()
    best_protein = health_df["Protein_g"].max()
    best_steps = health_df["Steps"].max()

    print(f"{'Highest Calories':<25}: {highest_calories} kcal")
    print(f"{'Lowest Calories':<25}: {lowest_calories} kcal")
    print(f"{'Best Protein':<25}: {best_protein} g")
    print(f"{'Best Steps':<25}: {best_steps}")

def goalComparison(health_df,user):
    target_calories=round(calculateTargetCalories(calculateMaintenanceCalories(health_df["Weight_kg"].iloc[-1],user["Height"],user["Age"],user["Gender"],user["Activity Level"]),user["Fitness Goal"]))
    avg_calories=round(health_df["Calories"].mean())
    difference = avg_calories - target_calories

    print(f"{'Target Calories':<25}: {target_calories} kcal")
    print(f"{'Average Calories':<25}: {avg_calories} kcal")
    print(f"{'Difference':<25}: {difference:+} kcal")

    if difference<0:
        print(f"{'Status':<25}: {'Below Target'}")
    elif difference==0:
        print(f"{'Status':<25}: {'Perfect'}")
    else:
        print(f"{'Status':<25}: {'Above Target'}")


def weeklyInsights(health_df,user):
    print("\n🧠 WEEKLY INSIGHTS")
    print("-" * 40)

    avg_protein=round(health_df["Protein_g"].mean())

    if avg_protein >= 150:
        print("✅ Protein intake is excellent.")
    elif avg_protein >= 100:
        print("👍 Protein intake is good.")
    else:
        print("⚠ Increase your protein intake.")

    avg_sleep = round(health_df["Sleep_hr"].mean(), 1)
    if avg_sleep >= 8:
        print("✅ Sleep is excellent.")
    elif avg_sleep >= 7:
        print("👍 Sleep is good.")
    else:
        print("⚠ Try sleeping at least 7 hours daily.")

    avg_water = round(health_df["Water_L"].mean(), 1)
    if avg_water >= 3:
        print("✅ Hydration is good.")
    else:
        print("⚠ Drink more water.")

    avg_steps = round(health_df["Steps"].mean())
    if avg_steps >= 10000:
        print("✅ Excellent daily activity.")
    elif avg_steps >= 7000:
        print("👍 Good activity level.")
    else:
        print("⚠ Increase your daily walking.")