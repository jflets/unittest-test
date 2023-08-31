from datetime import date, timedelta


class student:
    """A simple student class"""

    def __init__(self, first_name, last_name,):
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naught_list = False

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"