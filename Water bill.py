def rate_for(m3):
    if m3 <= 10:
        return 8.00
    elif m3 <= 20:
        return 12.00
    else:
        return 18.00
 
 
def main():
    total = 0.0
    print("Enter m3 consumed for each month. Type 'exit' to stop.")
    while True:
        entry = input("m3 consumed: ").strip()
        if entry.lower() == "exit":
            break
        try:
            m3 = float(entry)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        rate = rate_for(m3)
        charge = m3 * rate
        total += charge

        print(f"Month charge: ${charge:.2f} MXN")
 
    print(f"Total: ${total:.2f} MXN")
 
 
if __name__ == "__main__":
    main()