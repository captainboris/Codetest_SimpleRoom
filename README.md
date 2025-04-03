# Building Zone thermal Demand Application
This Python script simulates a simple thermal calling system for a building with various types of rooms (generic rooms, apartments, and common rooms). It calculates heating or cooling demands based on each room's temperature relative to a predefined set point.

## Versions
The final form of the program should be running under a python flask framework and the file structure is been designed in this way. However because of the tight schedule, current version program can only support running during CLI. All useful python programs are under .app folder.

## Features
Room management: adding additional rooms with various types: room, apartment, common rooms (e.g, gyms, libraries)
Zone Temperature Setpoint: Allow users input zone temperature setpoint
Thermal Demand Calculation: Determine cooling or heating demand based on a comparasion of real time (simulated) zone temperature and zone temperature setpoint
Unique Identifiers: A unique ID is generated for each room in hte building as a random ID

## Dependencies
1. Python 3.x
2. Python standard libraries: uuid, random

## Usage:
```
cd app
python main.py
```

## Coding Structure
### Classes
1. Room: Parent class provides unique ID, random temperature, and a thermal demand
2. Apartment: Sub-class of room, added owner_name and room_number
3. CommonRoom: Sub-class of room, added property_type
4. Building: A class that contains a list of rooms

### Methods
1. Building.adding_additional_rooms(): Adds rooms to the building
2. Building.calculate_heat_or_cool_demand(): Updates thermal demands for all rooms

## Example Output
```
Do you want to add additional room? Y/n: y
Which type of room are you adding? Please type in number only. 1: room, 2: apartment, 3: common room 3
Please type in common room property type, letters only. library
Do you want to add additional room? Y/n: y
Which type of room are you adding? Please type in number only. 1: room, 2: apartment, 3: common room 2
Please type in apartment number, numbers only. 103
Please type in apartment owner, letters only. Alex
Do you want to add additional room? Y/n: n
what is the zone temperature set point?23
Below are the information of the whole building:
The global temperature set point is set to 23
Room unique ID: 541048f3-b032-44a6-966e-4d8e648de31f, apartment number 101, the owner is Boris, zone temperature is: 33 dgC, needs cooling.
Room unique ID: 4d826b23-1962-4a20-817d-babaf0b832e8, apartment number 102, the owner is conserveIt, zone temperature is: 10 dgC, needs heating.
Room unique ID: 6de9533f-e8bc-4197-9569-22e483f57cd0, the property type is Gym, zone temperature is: 15dgC, needs heating.
Room unique ID: ae8b76a1-b237-4c6c-8046-6d6f9a8ead19, the property type is Library, zone temperature is: 33dgC, needs cooling.
Room unique ID: 8a6be3a8-11ff-4858-8340-7191c08a8384, the property type is library, zone temperature is: 11dgC, needs heating.
Room unique ID: da57e02c-521c-4c82-9b3b-4bd3515ecb76, apartment number 103, the owner is Alex, zone temperature is: 36 dgC, needs cooling.
```

## Limitations
1. Input vaildation is minimum e.g., there is no checks of duplicate apartment number or wrong type of inputs
2. There is no error handling logics

## Possible Improvements
1. Input Validation
2. Error Handling
3. Containerization
4. Packed in flask framework so user don't have to rely on CLI
5. User information can be saved in a csv or a SQL database and stored in a secure place
