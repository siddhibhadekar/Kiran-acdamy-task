
from abc import ABC, abstractmethod


# flight class
class Flight:
    def __init__(self, flight_code, airline, source, destination,
                 available_seats, base_fare):
        self.flight_code = flight_code
        self.airline = airline
        self.source = source
        self.destination = destination
        self._available_seats = available_seats
        self.base_fare = base_fare

    @property
    def available_seats(self):
        return self._available_seats

    def book_seats(self, tickets):
        if 0 < tickets <= self._available_seats:
            self._available_seats -= tickets
            return True
        return False

    def display_flight(self):
        print(
            f"{self.flight_code:<12}"
            f"{self.airline:<15}"
            f"{self.source:<15}"
            f"{self.destination:<15}"
            f"{self.available_seats:<10}"
            f"Rs. {self.base_fare}"
        )


# abstract passenger class
class Passenger(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_discount(self):
        pass

    def display_passenger(self):
        print("Passenger Name:", self.name)
        print("Passenger Age:", self.age)


# regular passenger class
class RegularPassenger(Passenger):
    def get_discount(self):
        return 0


# student passenger class
class StudentPassenger(Passenger):
    def get_discount(self):
        return 0.10


# booking class
class Booking:
    def __init__(self, booking_id, flight, passenger, tickets):
        self.booking_id = booking_id
        self.flight = flight
        self.passenger = passenger
        self.tickets = tickets

        self.subtotal = flight.base_fare * tickets
        self.discount = self.subtotal * passenger.get_discount()
        self.total_fare = self.subtotal - self.discount

    def display_summary(self):
        print("\n========== BOOKING SUMMARY ==========")
        print("Booking ID:", self.booking_id)
        print("Flight Code:", self.flight.flight_code)
        print("Airline:", self.flight.airline)
        print("Source:", self.flight.source)
        print("Destination:", self.flight.destination)

        self.passenger.display_passenger()

        if isinstance(self.passenger, StudentPassenger):
            print("Passenger Type: Student")
        else:
            print("Passenger Type: Regular")

        print("Number of Tickets:", self.tickets)
        print("Base Fare per Ticket: Rs.", self.flight.base_fare)
        print("Subtotal: Rs.", f"{self.subtotal:.2f}")
        print(
            f"Discount ({self.passenger.get_discount() * 100:.0f}%): "
            f"Rs. {self.discount:.2f}"
        )
        print("Final Amount: Rs.", f"{self.total_fare:.2f}")
        print("======================================")


# flight booking system class
class FlightBookingSystem:
    def __init__(self):
        self.flights = [
            Flight("PN101", "Kiran Air", "Pune", "Delhi", 20, 4000),
            Flight("MB202", "Sky India", "Mumbai", "Bengaluru", 15, 5000),
            Flight("PN303", "Kiran Air", "Pune", "Hyderabad", 25, 3000)
        ]

        self.bookings = []
        self.next_booking_id = 1001

    # display all flights
    def display_flights(self):
        print("\n================ AVAILABLE FLIGHTS ================")
        print(
            f"{'Flight Code':<12}"
            f"{'Airline':<15}"
            f"{'Source':<15}"
            f"{'Destination':<15}"
            f"{'Seats':<10}"
            f"Base Fare"
        )
        print("-" * 82)

        for flight in self.flights:
            flight.display_flight()

        print("-" * 82)

    # find flight by code
    def find_flight(self, flight_code):
        for flight in self.flights:
            if flight.flight_code.lower() == flight_code.lower():
                return flight
        return None

    # validate booking details
    def validate_booking(self, flight, name, age, tickets):
        if flight is None:
            print("Error: Flight code not found.")
            return False

        if not name.strip():
            print("Error: Passenger name cannot be blank.")
            return False

        if age <= 0:
            print("Error: Age must be greater than zero.")
            return False

        if tickets <= 0:
            print("Error: Number of tickets must be greater than zero.")
            return False

        if tickets > flight.available_seats:
            print("Booking failed: Not enough seats available.")
            return False

        return True

    # book flight
    def book_flight(self):
        self.display_flights()

        flight_code = input("\nEnter flight code: ").strip()
        flight = self.find_flight(flight_code)

        name = input("Enter passenger name: ").strip()

        try:
            age = int(input("Enter passenger age: "))

            passenger_type = input(
                "Passenger type (Regular/Student): "
            ).strip().lower()

            tickets = int(input("Enter number of tickets: "))

        except ValueError:
            print("Error: Enter a valid number for age and tickets.")
            return

        if passenger_type not in ["regular", "student"]:
            print("Error: Enter Regular or Student.")
            return

        if not self.validate_booking(flight, name, age, tickets):
            return

        if passenger_type == "student":
            passenger = StudentPassenger(name, age)
        else:
            passenger = RegularPassenger(name, age)

        if flight.book_seats(tickets):
            booking_id = "BK" + str(self.next_booking_id)

            booking = Booking(
                booking_id, flight, passenger, tickets
            )

            self.bookings.append(booking)
            self.next_booking_id += 1

            print("\nBooking confirmed successfully!")
            booking.display_summary()
        else:
            print("Booking failed: Not enough seats available.")

    # view latest booking
    def view_booking(self):
        if len(self.bookings) == 0:
            print("\nNo confirmed booking available.")
            return

        self.bookings[-1].display_summary()

    # main menu
    def run(self):
        print("\nWelcome to Kiran Air Booking")

        while True:
            print("\n========== MAIN MENU ==========")
            print("1. View Flights")
            print("2. Book Flight")
            print("3. View Booking")
            print("4. Exit")

            choice = input("Enter choice: ").strip()

            if choice == "1":
                self.display_flights()

            elif choice == "2":
                self.book_flight()

            elif choice == "3":
                self.view_booking()

            elif choice == "4":
                print("\nThank you for using Kiran Air Booking!")
                break

            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")


# main program
if __name__ == "__main__":
    app = FlightBookingSystem()
    app.run()
