init -3 python:
    ################################
    # mapped list helper functions #
    ################################

    def all_people_in_the_game(excluded_people = [], excluded_locations = []): # Pass excluded_people as array of people [mc, lily, aunt, cousin, alexia]
        return [y for x in list_of_places if x not in excluded_locations for y in x.people if y not in excluded_people]

    def all_locations_in_the_game(excluded_locations = []):
        return [x for x in list_of_places if x not in excluded_locations]

    def all_policies_in_the_game(excluded_policies = []):
        return [x for x in uniform_policies_list + recruitment_policies_list + serum_policies_list + organisation_policies_list + unmapped_policies_list if x not in excluded_policies]

    ##################################################################
    # MappedList - replace object property with function mapped item #
    # Used to prevent circular object references                     #
    ##################################################################

    class MappedList():
        def __init__(self, type, list_func, new_list = []):
            self.type = type
            self.list_func = list_func
            if new_list:
                self.mapped_list = new_list
            else:
                self.mapped_list = []

        def __getitem__(self, key):
            if isinstance( key, slice ) :
                #Get the start, stop, and step from the slice
                return [self[ii] for ii in xrange(*key.indices(len(self)))]
            elif isinstance(key, int):
                if key < 0 : #Handle negative indices
                    key += len( self )
                if key < 0 or key >= len( self ) :
                    raise IndexError
                return next((x for x in self.list_func() if x.identifier == self.mapped_list[key]), None)
            raise TypeError

        def __setitem__(self, key, item):
            if not isinstance(key, int):
                raise TypeError
            if isinstance(item, self.type):
                self.mapped_list[key] = item.identifier

        def __delitem__(self, key):
            if not isinstance(key, int):
                raise TypeError
            del self.mapped_list[key]

        def __repr__(self):
            return repr(self())

        def __call__(self):
            return [x for x in self.list_func() if x.identifier in self.mapped_list]

        def __iter__(self):
            item_list = self.list_func()
            for item in self.mapped_list:
                found = next((x for x in item_list if x.identifier == item), None)
                if found:
                    yield found
                else: # item is no longer in main list (remove it from mapping)
                    self.mapped_list.remove(item)

        def __len__(self):
            return len(self.mapped_list)

        def __contains__(self, item):
            if isinstance(item, self.type):
                return any(x for x in self.mapped_list if x == item.identifier)

        def __add__(self, other):
            if isinstance(other, MappedList):
                return MappedList(self.type, self.list_func, self.mapped_list.copy() + other.mapped_list.copy())
            if isinstance(other, list):
                new_list = self.mapped_list.copy()
                new_list.extend([x.identifier for x in other if isinstance(x, self.type)])
                return MappedList(self.type, self.list_func, new_list)

        def __sub__(self, other):
            if isinstance(other, MappedList):
                return MappedList(self.type, self.list_func, list(set(self.mapped_list.copy())-set(other.mapped_list.copy())))
            if isinstance(other, list):
                new_list = self.mapped_list.copy()
                for item in other:
                    if isinstance(item, self.type) and item.identifier in new_list:
                        new_list.remove(item.identifier)
                return MappedList(self.type, self.list_func, new_list)

        def __iadd__(self, other):
            self.append(other)
            return self

        def __isub__(self, other):
            self.remove(other)
            return self

        def append(self, item):
            if isinstance(item, self.type):
                if not item.identifier in self.mapped_list:
                    self.mapped_list.append(item.identifier)

        def remove(self, item):
            if isinstance(item, self.type):
                if item.identifier in self.mapped_list:
                    self.mapped_list.remove(item.identifier)

        def clear(self):
            self.mapped_list.clear()

        def extend(self, other):
            if isinstance(other, MappedList):
                self.mapped_list.extend(other.mapped_list)
            if isinstance(other, list):
                self.mapped_list.extend([x.identifier for x in other])

        def pop(self, index = -1):
            identifier = self.mapped_list.pop(index)
            return next((x for x in self.list_func() if x.identifier == identifier), None)

        def index(self, item):
            if isinstance(item, self.type):
                return self.mapped_list.index(item.identifier)
            raise ValueError
