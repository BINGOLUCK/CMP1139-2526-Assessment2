"""Decorator class for appointments. This is used to add more functionality"""

class AppointmentDecorator:
    """
    Basic decorator class
    Wraps an appointment object.
    """

    def __init__(self, appointment):
        self.appointment = appointment

    def attend_appointment(self):
        self.appointment.attend_appointment()
    
    def get_notes(self):
        return self.appointment.get_notes()
    
    class VaccinationAppointment(AppointmentDecorator):
        """
        Adds vac notes to an appointment"""

    def atttend_appointment(self):
        # calls the original appointment method
        super().attend_appointment()

        print("Enter Vac notes")
        vaccination = input()

        self.appointment.notes.append(
           f"vaccination= {vaccination}"
        )

        class surgeryDecorator(AppointmentDecorator):
            """
            Adds surgery notes to an appointment"""

    def attend_appointment(self):

        super().attend_appointment()

        print("Enter sugery notes:")
        notes = input()

        self.appointment.notes.append(
            f"surgery= {notes}")