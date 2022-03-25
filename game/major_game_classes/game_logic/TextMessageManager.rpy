init -2 python:
    class TextMessageManager(): #Manages text conversations you've had with other girls. Also stores information for other phone related stuff
        def __init__(self): #TODO: Add support for manufacturing a message history.
            self.message_history = {} # A dict that stores entries of Person:[HistoryEntry,HistoryEntry...] representing your recorded conversation with this girl.
            self.current_message = None # Set to a tuple of [who, what] when someone texts you, allowing for it to be displayed immediately (instead of after the statement is passed into history). Should be
            #TODO: Then figure out how we are gong to store pictures, videos, allow custom avatar pics, ect. We could either store them as .pngs, or store all the required parameters (including outfit).

        def register_number(self, person): #Now just used to keep track of whose number we know
            if not self.has_number(person):
                self.message_history[person.identifier] = []
                self.add_system_message(person, "Added " + person.name + " " + person.last_name + " to contacts.")

        def add_message(self, person, history_entry):
            self.register_number(person)
            self.message_history[person.identifier].append(history_entry)
            # auto delete old messages
            while len(self.message_history[person.identifier]) > 15:
                del self.message_history[person.identifier][0]

        def add_non_convo_message(self, person, the_message, as_mc = False): #Allows you to add an entry to the log without it having to appear as dialogue.
            new_entry = renpy.character.HistoryEntry() #TODO: Check if this results in double entries (it might be grabbed by the history callback immediately)
            if as_mc:
                new_entry.who = mc.name
            else:
                new_entry.who = person.title
            new_entry.what = the_message
            self.add_message(person, new_entry)


        def add_system_message(self, person, the_message): #Adds a history entry that does not have a "who" variable set. Use to add phone messages like "[SENT A PICTURE]".
            new_entry = renpy.character.HistoryEntry()
            new_entry.who = None
            new_entry.what = the_message
            self.add_message(person, new_entry)

        def get_person_list(self):
            return sorted([x for x in all_people_in_the_game() if x.identifier in self.message_history], key = lambda x: x.name)

        def has_number(self, person):
            return person.identifier in self.message_history

        def get_message_list(self, person):
            if self.has_number(person):
                return self.message_history[person.identifier]
            else:
                return []
