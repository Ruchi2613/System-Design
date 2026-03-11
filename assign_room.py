from guest_details import Guest
from guest_status import RelationStatus
from room_status import RoomStatus
from room_types import RoomTypes
from rooms import Room
from typing import List
from billing import Billing
from active_room import RoomActive

# This class manages the whole hotel system


class Manage:
    def __init__(self):
        # list of all guests
        self.guest = List[Guest]

        # list of all rooms
        self.rooms: List[Room] = []


        # list of current active bookings
        self.rooms_active: List[RoomActive] = []


    # assign room
    def assign_room(self, guest: Guest, nights: int):

        for room in self.rooms:
            if room.is_available():
                if guest.get_bed_count() == room.get_beds():
                    room.checkin_room()
                    active_room = RoomActive(guest, room, nights)
                    self.rooms_active.append(active_room)
                    print(f"{guest.get_guest_name()} booked {room.get_room_type().value} for {nights} nights")
                    return active_room

        print("Room not available")
        return None

    # checkout room
    def guest_checkout_room(self,guest: Guest):
        for active in self.rooms_active:
            if active.get_guest().get_guest_id == guest.get_guest_id():
                room = active.get_room()
                room.checkout_room()
                self.rooms_active.remove(active)
                print(f"{guest.get_guest_name()} checked out from {room.get_room_type().value}")

                return
        


    



    



    




        

    


