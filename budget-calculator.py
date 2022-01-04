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
    for key, value in categories.items():
        print(f"{key} {'|' : >5} {value : >5}")


def addNewCategory():
    global money_avaialable
    global categories

    new_category_name = input("Välj ett namn till din kategori: ")
    while new_category_name in categories.keys():
        new_category_name = input(
            f"Kategorin {new_category_name} finns redan, var vänlig välj ett annat namn: ")

    category_funds = float(
        input(f"Hur mycket pengar får användas för den nya kategorin {new_category_name}: "))
    while not isEnoughMoneyAvailable(category_funds):
        category_funds = float(input(
            f"Det finns inte tillräckligt med pengar för den här kategorin," +
            f"tillgänglig summa är {money_avaialable}, vad ska vi sätta för gräns istället för den nya kategorin? "))

    money_avaialable -= category_funds
    categories[new_category_name] = category_funds

    print(
        f"Kategorin {new_category_name} har laggts till med en tillgänglig summa på {category_funds}")


def updateCategory():
    global categories
    global money_avaialable

    category_to_be_updated = input("Vilken kategori vill du ändra? ")
    while(category_to_be_updated not in categories.keys()):
        category_to_be_updated = input(f"Kategorin {category_to_be_updated} finns inte i budgeten," +
                                       " om du glömt vilka kateogrier som finns, skriv '?': ")
        if(category_to_be_updated == "?"):
            print("Kategorierna är:")
            for category in categories.keys():
                print(category)
            category_to_be_updated = input("Vilken kategori vill du ändra? ")

    cateogry_changed = False
    while not cateogry_changed:
        print(
            f"Du har valt kategorin {category_to_be_updated}, dess gräns är satt till {categories[category_to_be_updated]}")
        valueToBeChanged = input(
            "Vad vill du ändra, skriv namn för namnet, eller gräns för gränsen: ")

        if(valueToBeChanged == "namn"):
            new_category_name = input("Vad ska kategorins namn bytas till? ")
            while(new_category_name in categories.keys()):
                new_category_name = input(
                    f"Kategorin {new_category_name} finns redan, var vänlig välj ett annat namn: ")

            categories[new_category_name] = categories[category_to_be_updated]
            categories.pop(category_to_be_updated)
            cateogry_changed = True
            print(
                f"Kategorin har updaterats, namn: {new_category_name} gräns: {categories[new_category_name]}")

        elif(valueToBeChanged == "gräns"):
            new_category_limit = input(
                "Vad ska kategorins gräns ändras till? ")
            while(not isEnoughMoneyAvailable(new_category_limit)):
                new_category_limit = float(input(
                    f"Det finns inte tillräckligt med pengar för den här kategorin," +
                    f"tillgänglig summa är {money_avaialable}, vad ska vi sätta för gräns istället för den nya kategorin? "))

            categories[category_to_be_updated] = new_category_limit
            cateogry_changed = True
            print(
                f"Kategorin har updaterats, namn: {categories[category_to_be_updated]} gräns: {new_category_limit}")


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
