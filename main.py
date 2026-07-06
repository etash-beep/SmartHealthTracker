from user import registerUser,checkUserExists,getUserName
from health import addDailyHealthLog
from utils import printHeading
from graphs import showGraphMenu
from dashboard import viewDashboard

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
        
        elif option==7:
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
    print("4. Health Prediction (ML)")
    print("5. Weekly Report")
    print("6. Reset User")
    print("7. Exit")


if __name__=="__main__":
    main()
