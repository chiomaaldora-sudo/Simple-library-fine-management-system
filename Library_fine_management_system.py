def calculate_fine():
    days = int(input("Enter number of overdue days: "))
    rate_per_day = 20
    fine = days * rate_per_day
    print("Total library fine:", fine)

def main():
    while True:
        print("1. Calculate Fine")
        print("2. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            calculate_fine()
        elif choice == "2":
            break
        else:
            print("Invalid option")

main()
