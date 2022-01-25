init -3 python:
    class DaySchedule():
        def __init__(self, home_location = None):
            self.schedule = [None] * 5
            if isinstance(home_location, Room):
                self.schedule[0] = home_location.identifier
                self.schedule[4] = home_location.identifier

        def __getitem__(self, key):
            return next((x for x in list_of_places if x.identifier == self.schedule[key]), None)

        def __setitem__(self, key, value):
            if isinstance(value, Room):
                self.schedule[key] = value.identifier
            elif isinstance(value, basestring) and any(x for x in list_of_places if x.identifier == value):
                self.schedule[key] = value
            else:
                self.schedule[key] = None

        def __copy__(self):
            new_schedule = DaySchedule()
            new_schedule.schedule = self.schedule.copy()    # make copy of list
            return new_schedule

    class Schedule():
        def __init__(self, home_location = None):
            self.schedule = []
            for _ in range(7):
                self.schedule.append(DaySchedule(home_location))

        def __getitem__(self, key):
            return self.schedule[key]

        def __setitem__(self, key, day_schedule):
            if isinstance(day_schedule, DaySchedule):
                self.schedule[key] = day_schedule

        def __copy__(self):
            new_schedule = Schedule()
            for x in range(7):
                new_schedule.schedule[x] = copy.copy(self.schedule[x]) # call copy function for each day schedule
            return new_schedule

        def clear_schedule(self):
            for x in range(7):
                for y in range(5):
                    self.schedule[x][y] = None

        def get_copy(self):
            return copy.copy(self)
