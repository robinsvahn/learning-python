import time

user_choice = 0
budget_limit = 0.0

categories = {}


def getMoneyAvailable() -> float:
    money_left = budget_limit
    for value in categories.values():
        money_left -= value

    return money_left


def getFloatFromInput(text: str) -> float:
    user_input = input(text)
    while not user_input.isnumeric():
        user_input = input(
            "Ogiltig input, var vänlig välj ett positivt numeriskt värde: ")
    return float(user_input)


def isEnoughMoneyAvailable(negative_change_in_funds: float) -> bool:
    return (getMoneyAvailable() - negative_change_in_funds) >= 0


def printBudget():
    budget_expenses = 0
    width = 15
    print("Din budget:")
    print("-----------------------------------")
    for key, value in categories.items():
        print(f"{key : <{width}} | {value} SEK")
        budget_expenses += value
    print("-----------------------------------")
    print(f"{'Tillgångar' : <{width}} | {budget_limit} SEK")
    print(f"{'Kostnader' : <{width}} | {budget_expenses} SEK")
    print("-----------------------------------")
    print(f"{'Pengar över' : <{width}} | {budget_limit - budget_expenses} SEK")


def addNewCategory():
    global categories

    new_category_name = input("Välj ett namn till din kategori: ")
    while new_category_name in categories.keys():
        new_category_name = input(
            f"Kategorin {new_category_name} finns redan, var vänlig välj ett annat namn: ")

    category_funds = getFloatFromInput(
        f"Hur mycket pengar får användas för den nya kategorin {new_category_name}: ")
    while not isEnoughMoneyAvailable(category_funds):
        category_funds = getFloatFromInput(
            f"Det finns inte tillräckligt med pengar för den här kategorin," +
            f"tillgänglig summa är {getMoneyAvailable()}, vad ska vi sätta för gräns istället för den nya kategorin? ")

    categories[new_category_name] = category_funds

    print(
        f"Kategorin {new_category_name} har laggts till med en tillgänglig summa på {category_funds}")


def updateCategory():
    global categories

    category_to_be_updated = input("Vilken kategori vill du ändra? ")
    while category_to_be_updated not in categories.keys():
        category_to_be_updated = input(f"Kategorin {category_to_be_updated} finns inte i budgeten," +
                                       " om du glömt vilka kateogrier som finns, skriv '?': ")
        if(category_to_be_updated == "?"):
            print("Kategorierna är:")
            for category in categories.keys():
                print(category)
            category_to_be_updated = input("Vilken kategori vill du ändra? ")

    category_changed = False
    while not category_changed:
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
            category_changed = True
            print(
                f"Kategorin har updaterats, namn: {new_category_name} gräns: {categories[new_category_name]}")

        elif(valueToBeChanged == "gräns"):
            new_category_limit = getFloatFromInput(
                "Vad ska kategorins gräns ändras till? ")
            while(not isEnoughMoneyAvailable(new_category_limit)):
                new_category_limit = getFloatFromInput(
                    f"Det finns inte tillräckligt med pengar för den här kategorin," +
                    f"tillgänglig summa är {getMoneyAvailable()}, vad ska vi sätta för gräns istället för den nya kategorin? ")

            categories[category_to_be_updated] = new_category_limit
            category_changed = True
            print(
                f"Kategorin har updaterats, namn: {categories[category_to_be_updated]} gräns: {new_category_limit}")


def navigateToChoice(choice: str):
    if(choice == "1"):
        printBudget()
    elif(choice == "2"):
        addNewCategory()
    elif(choice == "3"):
        updateCategory()


def startMainMenu():
    print("Välkommen till Robins budgetprogram!")


print("********************************************************************")
budget_limit = getFloatFromInput(
    "Hur mycket pengar får användas för budgeten? ")
while not user_choice == "4":
    print("""********************************************************************
Var vänlig välj tjänst: 

1. Skriv ut kalkyl
2. Lägg till kategori
3. Ändra kategori
4. Avsluta programmet
********************************************************************""")
    user_choice = input("Val: ")
    navigateToChoice(user_choice)

print("Avslutar program... ")
time.sleep(3)

# start of program
try:
    startMainMenu()
except ValueError:
    print("Something unexpected happened, we're rebooting the system...")
    time.sleep(2)
    startMainMenu()
