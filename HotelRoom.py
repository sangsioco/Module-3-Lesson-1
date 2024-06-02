hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}

# to check if a room is available
def is_available(hotel, room_number):
    return hotel.get(room_number, {}).get("status") == "available"

# to book a room 
def book_room(hotel, room_number):
    if is_available(hotel, room_number):
        customer_name = input("Enter customer name: ")
        hotel[room_number]["status"] = "booked"
        hotel[room_number]["customer"] = customer_name
        print(f"Room {room_number} booked successfully for {customer_name}.")
    else:
        print(f"Room {room_number} is not available. Please try a different room.")

# to checkout from room
def checkout(hotel, room_number):
    if room_number in hotel:
        if hotel[room_number]["status"] == "booked":
            customer_name = hotel[room_number]["customer"]
            hotel[room_number]["status"] = "available"
            hotel[room_number]["customer"] = ""
            print(f"{customer_name} successfully checked from room {room_number}.")
        else:
            print(f"Room {room_number} is already available.")
    else:
        print(f"Room {room_number} does not exist.")
	
# to display a room
def display_rooms(hotel):
    print("Room Status:")
    for room, details in hotel.items():
        print(f"Room {room}: {details['status']}, Customer: {details['customer'] or 'None'}")

while True:
    print("\nHotel Management System")
    print("\n1. Book Room\n2. Checkout\n3. Display Room\n4. Exit")
    choice = input("Enter your choice: ")    

    if choice == "1":
        room = input("Enter room number to book:")
        book_room(hotel_rooms, room)
    elif choice == "2":
        room = input("Enter room number to checkout: ")
        checkout(hotel_rooms, room)
    elif choice == "3":
        display_rooms(hotel_rooms)
    elif choice == "4":
        print("Exiting system")
        break
    else:
        print("Invalid choice. Try again.")
