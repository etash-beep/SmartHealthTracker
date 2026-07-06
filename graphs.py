import pandas as pd
import matplotlib.pyplot as plt
import os


def showGraphMenu():
    while True:
        print("1. Weight vs Date")
        print("2. Calories vs Date")
        print("3. Protein vs Date")
        print("4. Sleep vs Date")
        print("5. Water vs Date")
        print("6. Workout vs Date")
        print("7. Steps vs Date")
        print("8. Show All Graphs")
        print("9. Back")

        choice=int(input("Enter your choice:"))

        if choice==1:
            generateGraph("Weight_kg","Weight vs Date","Weight in kg")
        elif choice==2:
            generateGraph("Calories","Calories vs Date","Calories in kcal")
        elif choice==3:
            generateGraph("Protein_g","Protein vs Date","Protein in g")
        elif choice==4:
            generateGraph("Sleep_hr","Sleep vs Date","Sleep in hr")
        elif choice==5:
            generateGraph("Water_L","Water vs Date","Water in L")
        elif choice==6:
            generateGraph("Workout_Min","Workout vs Date","Workout in mins") 
        elif choice==7:
            generateGraph("Steps","Steps vs Date","Steps")
        elif choice==8:
            generateGraph("Weight_kg","Weight vs Date","Weight in kg")
            generateGraph("Calories","Calories vs Date","Calories in kcal")
            generateGraph("Protein_g","Protein vs Date","Protein in g")
            generateGraph("Sleep_hr","Sleep vs Date","Sleep in hr")
            generateGraph("Water_L","Water vs Date","Water in L")
            generateGraph("Workout_Min","Workout vs Date","Workout in mins")
            generateGraph("Steps","Steps vs Date","Steps")
        elif choice==9:
            break
        else:
            print("Invalid Choice")

def generateGraph(column_name,title,y_label):

    file_path="data/health_logs.csv"
    if not os.path.isfile(file_path):
        print("No health logs found.")
        return

    df=pd.read_csv(file_path)
    x=df["Date"]
    y=df[column_name]
    
    plt.figure(figsize=(8,5))
    plt.plot(x,y,marker="o",linewidth=2)
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel(y_label)
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"graphs/{column_name}.png")
    plt.show()
