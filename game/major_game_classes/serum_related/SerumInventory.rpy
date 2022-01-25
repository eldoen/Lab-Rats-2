init -2 python:
    class SerumInventory(renpy.store.object): #A bag class that lets businesses and people hold onto different types of serums, and move them around.
        def __init__(self,starting_list = None):
            if starting_list is None:
                self.serums_held = []
            else:
                self.serums_held = starting_list ##Starting list is a list of tuples, going [SerumDesign,count]. Count should be positive.

        def get_serum_count(self, serum_design):
            for design in self.serums_held:
                if design[0] == serum_design:
                    return design[1]
            return 0

        def get_any_serum_count(self):
            if not self.serums_held:
                return 0
            return __builtin__.sum(list(zip(*self.serums_held))[1])

        def get_matching_serum_count(self, check_function): #Hand a function to the inventory and get a count of the number of serums that match that requirement.
            count = 0
            for design in self.get_serum_type_list():
                if check_function(design):
                    count += self.get_serum_count(design)
            return count

        def get_max_serum_count(self): #Returns the count of the highest group of serums you have available.
            if not self.serums_held:
                return 0
            return __builtin__.max(list(zip(*self.serums_held))[1])

        def change_serum(self, serum_design,change_amount): ##Serum count must be greater than 0. Adds to stockpile of serum_design if it is already there, creates it otherwise.
            found = False
            for design in self.serums_held:
                if design[0] == serum_design and not found:
                    design[1] += __builtin__.int(change_amount)
                    found = True
                    if design[1] <= 0:
                        self.serums_held.remove(design)

            if not found:
                if change_amount > 0:
                    self.serums_held.append([serum_design, __builtin__.int(change_amount)])


        def get_serum_type_list(self): ## returns a list of all the serum types that are in the inventory, without their counts.
            if not self.serums_held:
                return []
            return list(zip(*self.serums_held))[0]

        def get_highest_serum_count(self):
            # sort the list; get the last tuple [-1]; get the design [0]
            if not self.serums_held:
                return None
            return sorted(self.serums_held,key=lambda x:x[1])[-1][0]
