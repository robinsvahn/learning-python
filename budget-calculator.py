# Create menu
# Create function for each option
# Save budget in a global dictionary

# start of program
user_choice = 0
money_avaialable = 0

print("Välkommen till Robins budgetprogramm")
print("**********************************")
money_avaialable = int(
    input("Hur mycket pengar är tillförfogande för budgeten? "))
while (not user_choice == "4"):
    print("""**********************************
    1. Skriv ut kalkyl
    2. Lägg till kategori
    3. Ändra kategori
    4. Avsluta programmet
    **********************************""")
    user_choice = input("Val: ")
