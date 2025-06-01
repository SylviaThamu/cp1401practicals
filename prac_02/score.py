import random

def main():
    score = float(input("Enter score: "))
    result = determine_score_result(score)
    print(result)

    random_score = random.randint(0, 100)
    print(f"Random score: {random_score}")
    print(determine_score_result(random_score))


def determine_score_result(score):
    """Return a message based on the score value."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()