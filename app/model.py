import uuid
import random

class Room:
    def __init__(self):
        self.uniqueID = uuid.uuid4()
        self.zoneTemp = random.randint(10, 40)
        self.thermal_demand = "Nothing"

class Apartment(Room):
    def __init__(self, owner_name, room_number):
        super().__init__()
        self.owner_name = owner_name
        self.room_number = room_number

class CommonRoom(Room):
    def __init__(self, property_type):
        super().__init__()
        property_types = ['Gym', 'Library', 'laundry']
        self.property_type = property_type

class Building:
    def __init__(self):
        self.thermal_demand = None
        self.zone_temp_sp = None
        self.zone_temp_SP = 20
        self.rooms = []

    def zone_temp_sp_setting(self, zone_temp_sp):
        self.zone_temp_sp = zone_temp_sp

    def adding_additional_rooms(self, room):
        self.rooms.append(room)

    def calculate_heat_or_cool_demand(self):
        for room in self.rooms:
            if room.zoneTemp < self.zone_temp_SP:
                room.thermal_demand = "heating"
            elif room.zoneTemp > self.zone_temp_SP:
                room.thermal_demand = "cooling"
