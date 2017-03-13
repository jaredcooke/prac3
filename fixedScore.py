def main():
    score = float(input("Enter score: "))
    text = result(score)
    print(text)


def result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"

main()