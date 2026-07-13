def main():
    grades = []
 
    
    print("Enter grades one by one. Type 'done' when finished.")
    while True:
        entry = input("Grade: ").strip()
        if entry.lower() == "done":
            break
        try:
            grade = float(entry)
            grades.append(grade)
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")
 
    if len(grades) == 0:
        print("No grades entered. Please enter at least one grade.")
        return
 
    average = sum(grades) / len(grades)
    status = "Passed" if average >= 7.0 else "Failed"
 
    print(f"Average: {average:.2f} — {status}")
 
 
if __name__ == "__main__":
    main()
 