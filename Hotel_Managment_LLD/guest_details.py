from guest_status import RelationStatus
from room_types import RoomTypes

class Guest:
    def __init__(self,name:str, guest_id: int, address: str,r_status: RelationStatus, beds_types:RoomTypes, bed_count: int):
        self.name = name
        self.guest_id = guest_id
        self.address = address
        self.r_status = r_status # relationship status

        # room preference
        self.beds_types = beds_types
        self.bed_count = bed_count


    def get_guest_name(self):
        return self.name
    
    def get_bed_count(self):
        return self.bed_count
    
    def get_guest_id(self):
        return self.guest_id
    

    def get_guest_address(self):
        return self.address
    

    def get_guest_relationship_status(self):
        return self.r_status
    

    # return full guest details
    def get_details(self):
        return f"Guest name: {self.name}, ID: {self.guest_id}, Address: {self.address}, Relationship: {self.r_status.value}"    
