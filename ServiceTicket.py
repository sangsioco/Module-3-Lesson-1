service_tickets = {
    "Ticket 001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket 002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

# to open a new service ticket
def open_ticket(tickets, ticket_number, customer, issue):
    if ticket_number not in tickets:
        tickets[ticket_number] = {"Customer": customer, "Issue": issue, "Status": "open"}
        print(f"Ticket {ticket_number} opened successfully for {customer}.")
    else:
        print(f"Ticket {ticket_number} already exists.")

# to update the status of an existing ticket
def update_ticket_status(tickets, ticket_number, new_status):
    if ticket_number in tickets:
        tickets[ticket_number]["Status"] = new_status
        print(f"Status of Ticket {ticket_number} updated to {new_status}.")
    else:
        print(f"Ticket {ticket_number} does not exist.")

# to display all tickets or filter by status
def display_tickets(tickets, status=None):
    if status:
        filtered_tickets = {ticket: details for ticket, details in tickets.items() if details["Status"] == status}
        if filtered_tickets:
            print(f"Tickets with status '{status}':")
            for ticket, details in filtered_tickets.items():
                print(f"Ticket {ticket}: Customer - {details['Customer']}, Issue - {details['Issue']}")
        else:
            print(f"No tickets found with status '{status}'.")
    else:
        print("All Tickets:")
        for ticket, details in tickets.items():
            print(f"Ticket {ticket}: Customer - {details['Customer']}, Issue - {details['Issue']}")

while True:
    print("\nService Ticket System")
    print("\n1. Open Ticket\n2. Update Ticket\n3. Display Ticket\n4. Exit")
    choice = input("Enter your choice: ")    

    if choice == "1":
        ticket_number = input("Enter ticket number: ")
        customer = input("Enter customer name: ")
        issue = input("Enter issue description: ")
        open_ticket(service_tickets, ticket_number, customer, issue)
    elif choice == "2":
        ticket_number = input("Enter ticket number to update: ")
        new_status = input("Enter new status (open/closed): ")
        update_ticket_status(service_tickets, ticket_number, new_status)
    elif choice == "3":
        status_filter = input("Enter status to filter by (leave blank for all tickets): ")
        display_tickets(service_tickets, status_filter)
    elif choice == "4":
        print("Exiting system")
        break
    else:
        print("Invalid choice. Try again.")
