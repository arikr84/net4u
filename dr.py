class Doctors:
    def __init__(self, name, specialization, availability_days, availability_hours, clinic_location):
        self.name = name
        self.specialization = specialization
        self.availability_days = availability_days
        self.availability_hours = availability_hours
        self.clinic_location = clinic_location


    def invitation(self, specialization, name, availability_days, availability_hours):
        print("Found 1 " + specialization + " doctor(s): \nName: " + name + "\nAvailability Days: " + availability_days + "\nAvailable Hours: " + availability_hours)

# dr idan amit
# idan eyes and hands
# dr idan free only on sunday\ only 1 hour is blocked and he works from 1 to 5
# dr amit free monday 14:00
# idan Haifa
# amit Holon
# From the user input understand what doctor he needs
# print all the details about the doctor
# reserve the room and print it
