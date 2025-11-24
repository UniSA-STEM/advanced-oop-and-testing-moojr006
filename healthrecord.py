'''
File: healthrecord.py
Description: A brief description of this Python module.
Author: Jason Moore
ID: 110456746
Username: moojr006
This is my own work as defined by the University's Academic Integrity Policy.
'''
from datetime import datetime


class HealthRecord:
    def __init__(self, animal_name):
        self.__animal_name = animal_name
        self.__records = []

    def get_name(self):
        return self.__animal_name

    def get_records(self):
        return self.__records

    def get_most_recent_record(self):
        if len(self.__records) == 0:
            raise IndexError("No records found")
        else:
            return self.__records[-1]


    def __record_entry(self, title: str, severity: str, date_argument: datetime):
        self.__records.append((title, severity, date_argument))

    def record_entry(self, title: str, severity: str):
        date_argument = datetime.today()
        self.__record_entry(title, severity, date_argument)

    def __report(self):
        count = 1
        health = []
        health.append(f"Health report for {self.get_name()}")
        health.append("=" * 70)
        for record in self.__records:

            health.append(f"{count}. {record[2].strftime('%Y-%m-%d %H:%M:%S')}, Severity: {record[1]}, Title: {record[0]}")
            count += 1
        health.append("=" * 70)

        return "\n".join(health)

    def report(self):
        return self.__report()


    name = property(get_name)




