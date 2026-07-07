from user import registerUser,checkUserExists,getUserName
from health import addDailyHealthLog
from utils import printHeading
from graphs import showGraphMenu
from dashboard import viewDashboard
from reports import weeklyReport
from health_score import showHealthScore

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
            weeklyReport()
        elif option==8:
            print("\nThank you for using Smart Health Tracker.")
            break
        else:
            print("\n⚠ Feature Coming Soon...\n")



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