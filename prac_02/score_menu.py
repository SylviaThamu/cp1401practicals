    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))

    choice = get_menu_choice()
    while choice != "Q":
        if choice == "G":
            print(determine_score_result(score))
        elif choice == "S":
            print_stars(score)
        choice = get_menu_choice()
    print("Goodbye.")


def get_menu_choice():
    print("\nMenu:")
    print("(G)et result")
    print("(S)how stars")
    print("(Q)uit")
    choice = input(">>> ").upper()
    return choice


def determine_score_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_stars(score):
    print("*" * int(score))


main()
