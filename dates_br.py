from datetime import datetime


class DatesBR:
    def __init__(self):
        self.register_moment = datetime.today()

    def __str__(self):
        return self.format_data()

    def format_data(self):
        date_formatted = self.register_moment.strftime("%d/%m/%Y %H:%M")
        return date_formatted

    def register_time(self):
        register_time = datetime.today() - self.register_moment
        return register_time
