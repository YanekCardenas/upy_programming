WINTER = (12, 1, 2)
SPRING = (3, 4, 5)
SUMMER = (6, 7, 8)
FALL = (9, 10, 11)
 
 
def classify_season(month):
    if month in WINTER:
        return "Winter"
    elif month in SPRING:
        return "Spring"
    elif month in SUMMER:
        return "Summer"
    elif month in FALL:
        return "Fall"
    return None
 
 
def main():
    print("Enter a month number (1-12). Type 'exit' to stop.")
    while True:

        entry = input("Month: ").strip()
        if entry.lower() == "exit":
            break
        try:
            month = int(entry)
        except ValueError:
            print("Invalid month. Please enter a number between 1 and 12.")
            continue
 

        if month < 1 or month > 12:

            print("Invalid month. Please enter a number between 1 and 12.")
            continue
 
        season = classify_season(month)

        print(season)
 
 
if __name__ == "__main__":
    main()