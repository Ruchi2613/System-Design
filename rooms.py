from room_types import RoomTypes
from room_status import RoomStatus

class Room:
    def __init__(self, room_id, room_type: RoomTypes, beds: int):
        self.room_id = room_id
        self.room_type = room_type
        self.beds = beds
        # when room created it is available
        self.room_status = RoomStatus.AVAILABLE

    def get_room_id(self):
        return self.room_id
    

    def get_room_type(self):
        return self.room_type
    

    def get_beds(self):
        return self.beds
    

    def is_available(self):
        return self.room_status == RoomStatus.AVAILABLE
    

    def checkin_room(self):
        self.room_status = RoomStatus.RESERVED
    
    def checkout_room(self):
        self.room_status = RoomStatus.AVAILABLE

    
