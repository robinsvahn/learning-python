# Create menu
# Create function for each option
# Save budget in a global dictionary

import time

user_choice = 0
money_avaialable = 0.0

categories = {}


def isEnoughMoneyAvailable(negative_change_in_funds: float) -> bool:
    return (money_avaialable - negative_change_in_funds) > 0


def printBudget():
    print("Printing budget....")


def addNewCategory():
    print("Adding new category...")
    global money_avaialable
    global categories

    category_name = input("Välj ett namn till din kategori: ")
    while(category_name in categories.keys()):
        category_name = input(
            f"Kategorin {category_name} finns redan, var vänlig välj ett annat namn: ")

    category_funds = float(
        input(f"Hur mycket pengar får användas för den nya kategorin {category_name}: "))
    while(not isEnoughMoneyAvailable(category_funds)):
        category_funds = float(input(
            f"Det finns inte tillräckligt med pengar för den här kategorin," +
            f"tillgänglig summa är {money_avaialable}, vad ska vi sätta för gräns istället för den nya kategorin? "))

    money_avaialable -= category_funds
    categories[category_name] = category_funds

    print(
        f"Kategorin {category_name} har laggts till med en tillgänglig summa på {category_funds}")


def updateCategory():
    print("Changing category...")


def navigateToChoice(choice: str):
    if(choice == "1"):
        printBudget()
    elif(choice == "2"):
        addNewCategory()
    elif(choice == "3"):
        updateCategory()


# start of program
print("Välkommen till Robins budgetprogram!")
print("********************************************************************")
money_avaialable = int(
    input("Hur mycket pengar är tillförfogande för budgeten? "))
while (not user_choice == "4"):
    print("""********************************************************************
1. Skriv ut kalkyl
2. Lägg till kategori
3. Ändra kategori
4. Avsluta programmet
********************************************************************""")
    user_choice = input("Val: ")
    navigateToChoice(user_choice)

print("Avslutar program... ")
time.sleep(3)
