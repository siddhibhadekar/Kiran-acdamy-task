
while True:
    print("\n===== CAB BOOKING CHATBOT =====")
    print("1. Book Ride")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nSelect Cab Type:")
        print("1. Auto - Rs.12/km")
        print("2. Sedan - Rs.18/km")
        print("3. SUV - Rs.25/km")

        cab_choice = input("Enter cab choice: ")

        if cab_choice == "1":
            cab_type = "Auto"
            rate = 12
        elif cab_choice == "2":
            cab_type = "Sedan"
            rate = 18
        elif cab_choice == "3":
            cab_type = "SUV"
            rate = 25
        else:
            print("Invalid cab choice!")
            continue

        print("\nSelect Route:")
        print("1. Pune Station to Shivajinagar - 5 km")
        print("2. Swargate to Kothrud - 8 km")
        print("3. Hinjawadi to Wakad - 10 km")

        route_choice = input("Enter route choice: ")

        if route_choice == "1":
            source = "Pune Station"
            destination = "Shivajinagar"
            distance = 5
        elif route_choice == "2":
            source = "Swargate"
            destination = "Kothrud"
            distance = 8
        elif route_choice == "3":
            source = "Hinjawadi"
            destination = "Wakad"
            distance = 10
        else:
            print("Invalid route choice!")
            continue

        fare = rate * distance

        print("\n===== RIDE DETAILS =====")
        print("Cab Type:", cab_type)
        print("Source:", source)
        print("Destination:", destination)
        print("Distance:", distance, "km")
        print("Rate: Rs.", rate, "per km")
        print("Total Fare: Rs.", fare)

        print("\n1. Confirm & Share OTP")
        print("2. Cancel Ride")

        confirm = input("Enter your choice: ")

        if confirm == "2":
            print("Ride cancelled successfully!")
            print("No OTP has been shared.")
            continue

        elif confirm == "1":
            import random

            otp = random.randint(1000, 9999)

            print("\nYour OTP is:", otp)
            print("OTP shared successfully.")
            print("Cancellation is NOT allowed after OTP sharing.")
            print("Your ride is confirmed!")

        else:
            print("Invalid choice! Ride cancelled.")
            print("No OTP has been shared.")

    elif choice == "2":
        print("\nThank you for using Cab Booking Chatbot!")
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please select 1 or 2.")
1