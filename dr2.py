from net4u.dr import Doctors

idan = Doctors("Idan", "eyes", "Sunday", ['13:00', '14:00', '15:00', '16:00', '17:00'], "Haifa")
amit = Doctors("Amit", "arms", "Monday", "14:00", "Holon")


specialization = input("What specialization you searching doctor for?: ").lower()
while specialization != "eyes" and specialization != "arms":
    specialization = input("Please enter 'arms' or 'eyes': ").lower()


if specialization == amit.specialization:
    amit.invitation(idan.specialization, amit.name, amit.availability_days, str(', '.join(amit.availability_hours)))
    day = input("\nEnter a day from the available days in the list: [" + amit.availability_days + "]: ").lower()
    while day != "sunday":
        if day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday":
            day = input("Doctor " + amit.name + " is only working on Sunday").lower()
        else:
            day = input(day + " is not a valid day. Please enter a valid day").lower()
else:
    idan.invitation(idan.specialization, amit.name, idan.availability_days, str(', '.join(idan.availability_hours)))
    day = input("\nEnter a day from the available days in the list: [" + idan.availability_days + "]: ").lower()
    while day != "sunday":
        if day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday":
            day = input("Doctor " + idan.name + " is only working on Sunday").lower()
        else:
            day = input(day + " is not a valid day. Please enter a valid day").lower()






