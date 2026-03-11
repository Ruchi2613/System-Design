from assign_room import Manage
from rooms import Room
from room_types import RoomTypes
from guest_details import Guest
from guest_status import RelationStatus
from billing import Billing


def main():

    hotel = Manage()

    # create rooms
    room1 = Room(101, RoomTypes.BEDROOM, 2)
    room2 = Room(102, RoomTypes.DUPLEX, 3)

    hotel.rooms.append(room1)
    hotel.rooms.append(room2)

    # create guest
    guest1 = Guest(
        "Ruchi",
        1,
        "Seattle",
        RelationStatus.SINGLE,
        RoomTypes.BEDROOM,
        2
    )

    # guest stays for 3 nights
    nights = 3

    booking = hotel.assign_room(guest1, nights)

    if booking:

        # create billing
        bill = Billing(nights)

        total = bill.total_amount()

        room_type = booking.get_room().get_room_type().value

        print("\n----- BILL DETAILS -----")

        print("Guest Name:", guest1.get_guest_name())
        print("Room Type:", room_type)
        print("Nights Stayed:", nights)
        print("Total Amount Paid: $", total)


if __name__ == "__main__":
    main()