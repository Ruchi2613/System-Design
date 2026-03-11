from datetime import date
from guest_details import Guest
from rooms import Room


# This class represents an ACTIVE booking
# means guest currently staying in a room

class RoomActive:

    def __init__(self, guest_info: Guest, room_info: Room, nights: int):

        self.guest_info = guest_info
        self.room_info = room_info

        # checkin date
        self.checkin_date = date.today()

        # how many nights guest will stay
        self.nights = nights

    # return guest
    def get_guest(self):
        return self.guest_info

    # return room
    def get_room(self):
        return self.room_info

    # return nights
    def get_nights(self):
        return self.nights

    # return booking details
    def get_details(self):

        guest_name = self.guest_info.get_guest_name()
        room_type = self.room_info.get_room_type().value

        return f"{guest_name} checked into {room_type} for {self.nights} nights"