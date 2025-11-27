'''
File: healthrecord.py
Description: HealthRecord class that logs Animal data.
Author: Jason Moore
ID: 110456746
Username: moojr006
This is my own work as defined by the University's Academic Integrity Policy.
'''
from datetime import datetime


class HealthRecord:
    severity = ["low", "medium", "high"]
    def __init__(self, animal_name):
        """Instantiate HealthRecord name of animal that is being recorded.

        Initialise:
            __records: An empty list of tuples that is used for each log entry.
        """
        self.__animal_name = animal_name
        self.__records = []

    def get_name(self):
        """Returns name of HealthRecord."""
        return self.__animal_name

    def get_records(self):
        """Returns records of HealthRecord."""
        return self.__records

    def get_most_recent_record(self):
        """Returns the latest record entry added to __records."""
        if len(self.__records) == 0:
            return None
        else:
            return self.__records[-1]


    def __record_entry(self, title: str, severity: str, date_argument: datetime):
        """Appends a record entry to __records.

        Args:
            title: a string briefly describing the record entry.
            severity: a string indicating a low, medium, or high severity.
            date_argument: datetime.today() method to accurately log record generation.
            """
        self.__records.append((title, severity, date_argument))

    def record_entry(self, title: str, severity: str):
        """Wrapper method that validates input for __record_entry."""
        severity = severity.lower()
        try:
            if severity in HealthRecord.severity:
                date_argument = datetime.today()
                self.__record_entry(title, severity, date_argument)
            else:
                raise ValueError(f"Invalid severity")
        except ValueError as e:
            print(f"ValueError: {e}. Received {severity} instead.")
            print(f"Valid severities are: {HealthRecord.severity}")



    def __report(self):
        """Return report of all records in __records.

        Contains record number, date, severity, and title.

        Return:
            str: A user-friendly report of records entered.
        """
        count = 1
        health = []
        health.append(f"\nHealth report for {self.get_name()}")
        health.append("=" * 70)
        for record in self.__records:

            health.append(f"{count}. {record[2].strftime('%Y-%m-%d %H:%M:%S')}, Severity: {record[1]}, Title: {record[0]}")
            count += 1
        health.append("=" * 70)

        return "\n".join(health)

    def report(self):
        """Wrapper method for __report"""
        return self.__report()


    name = property(get_name)
    records = property(get_records)




