def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"
 
 
def main():
    print("Enter weight and height for each person. Type 'exit' at the weight prompt to stop.")
    while True
        weight_input = input("Weight (kg): ").strip()
        if weight_input.lower() == "exit":
            break
        try:
            weight = float(weight_input)
        except ValueError:
            print("Invalid weight. Please enter a number.")
            continue
 
        height_input = input("Height (m): ").strip()
        try:
            height = float(height_input)
        except ValueError:
            print("Invalid height. Please enter a number.")
            continue
 
        bmi = weight / (height ** 2)
        category = classify_bmi(bmi)
 
        print(f"BMI: {bmi:.2f} — {category}")
 
 
if __name__ == "__main__":
    main()