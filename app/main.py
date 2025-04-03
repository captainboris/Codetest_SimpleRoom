from model import Room, Apartment, CommonRoom, Building

a_Building = Building()
apartment_101 = Apartment("Boris", 101)
apartment_102 = Apartment("conserveIt", 102)
a_gym = CommonRoom("Gym")
a_library = CommonRoom("Library")

a_Building.adding_additional_rooms(apartment_101)
a_Building.adding_additional_rooms(apartment_102)
a_Building.adding_additional_rooms(a_gym)
a_Building.adding_additional_rooms(a_library)


continue_adding_room = True
while continue_adding_room:
    add_more_room = input("Do you want to add additional room? Y/n: ")
    if add_more_room.lower() == 'y':
        structure_type = input("Which type of room are you adding? Please type in number only. 1: room, 2: apartment, 3: common room ")
        if structure_type == '1':
            a_Building.adding_additional_rooms(Room())
        elif structure_type == '2':
            room_number = input("Please type in apartment number, numbers only. ")
            room_owner = input("Please type in apartment owner, letters only. ")
            a_Building.adding_additional_rooms(Apartment(room_owner, int(room_number)))
        elif structure_type == '3':
            property_type = input("Please type in common room property type, letters only. ")
            a_Building.adding_additional_rooms(CommonRoom(property_type))
        else:
            print("Invalid room type selected. Please choose 1, 2, or 3.")
    else:
        continue_adding_room = False

zone_temp_sp = input("what is the zone temperature set point?")
a_Building.zone_temp_sp_setting(zone_temp_sp)
a_Building.calculate_heat_or_cool_demand()

print(f"Below are the information of the whole building:")
print(f"The global temperature set point is set to {zone_temp_sp}")
for room in a_Building.rooms:

    if isinstance(room, Apartment):
        print(f"Room unique ID: {room.uniqueID}, apartment number {room.room_number}, the owner is {room.owner_name}, zone temperature is: {room.zoneTemp} dgC, needs {room.thermal_demand}.")
    elif isinstance(room, CommonRoom):
        print(f"Room unique ID: {room.uniqueID}, the property type is {room.property_type}, zone temperature is: {room.zoneTemp}dgC, needs {room.thermal_demand}.")
    elif isinstance(room, Room):
        print(f"Room unique ID: {room.uniqueID}, zone temperature is: {room.zoneTemp}dgC, needs {room.thermal_demand}.")