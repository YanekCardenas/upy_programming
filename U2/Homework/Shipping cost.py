def shipping_cost(weight, distance):
    if distance <= 100:
        return 50.00 if weight <= 5 else 80.00
    else:
        return 120.00 if weight <= 5 else 200.00
 
 
def main():
    total = 0.0
    print("Enter weight and distance for each package. Type 'exit' at the weight prompt to stop.")
    while True:
        weight_input = input("Weight (kg): ").strip()
        if weight_input.lower() == "exit":
            break
        try:
            weight = float(weight_input)
        except ValueError:
            print("Invalid weight. Please enter a number.")
            continue
 
        distance_input = input("Distance (km): ").strip()
        try:
            distance = float(distance_input)
        except ValueError:
            print("Invalid distance. Please enter a number.")
            continue
 
        cost = shipping_cost(weight, distance)
        total += cost
 
        print(f"Shipping cost: ${cost:.2f} MXN")
 
    print(f"Total: ${total:.2f} MXN")
 
 
if __name__ == "__main__":
    main()