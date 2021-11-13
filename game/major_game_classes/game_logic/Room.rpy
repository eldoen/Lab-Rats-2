init -2 python:
    class Room(renpy.store.object): #Contains people and objects.
        def __init__(self, name = None, formal_name = None, connections = None, background_image= None, objects = None, people = None, actions = None, public = False, map_pos = None,
            tutorial_label = None, visible = True, hide_in_known_house_map = True, lighting_conditions = None):

            if name is None:
                self.name = "Unnamed Room"
            else:
                self.name = name

            if formal_name is None:
                self.formal_name = name
            else:
                self.formal_name = formal_name

            if connections is None:
                self.connections = []
            else:
                self.connections = connections

            if background_image is None:
                self.background_image = "Outside_Background.png"
            else:
                self.background_image = background_image #If a string this is used at all points in the day. If it is a list each entry corrisponds to the background for a different part of the day

            if objects is None:
                self.objects = []
            else:
                self.objects = objects
            self.objects.append(Object("stand",["Stand"], sluttiness_modifier = 0, obedience_modifier = 0)) #Add a standing position that you can always use.

            if people is None:
                self.people = []
            else:
                self.people = people

            if actions is None:
                self.actions = []
            else:
                self.actions = actions #A list of Action objects

            self.on_room_enter_event_list = [] #A list of Actions that are triggered when you enter a location. People events take priority.

            self.public = public #If True, random people can wander here.

            if map_pos is None:
                self.map_pos = [-1,-1] #off screen
            else:
                self.map_pos = map_pos #A tuple of two int values giving the hex coords, starting in the top left. Using this guarantees locations will always tessalate.

            self.visible = visible #If true this location is shown on the map. If false it is not on the main map and will need some other way to access it.
            self.hide_in_known_house_map = hide_in_known_house_map #If true this location is hidden in the house map, usually because their house is shown on the main map.

            self.tutorial_label = tutorial_label #When the MC first enters the room the tutorial will trigger.
            self.trigger_tutorial = True #Flipped to false once the tutorial has been done once
            self.accessable = True #If true you can move to this room. If false it is disabled

            if lighting_conditions is None: #Default is 100% lit all of the time.
                self.lighting_conditions = [[1,1,1], [1,1,1], [1,1,1], [1,1,1], [1,1,1]] #A colour array that tints characters in this location. Perfect default light is 1,1,1
            else:
                self.lighting_conditions = lighting_conditions

            #TODO: add an "appropriateness" or something trait that decides how appropriate it would be to have sex, be seduced, etc. in this location.

        @property
        def identifier(self):
            if not hasattr(self, "_identifier"):
                self._identifier = hashlib.md5(self.name + self.formal_name).hexdigest()
            return self._identifier

        def show_background(self):
            if isinstance(self.background_image, list):
                the_background_image = self.background_image[time_of_day]
            else: #I assume it's a list that contains one string per
                the_background_image = self.background_image

            renpy.scene("master")
            renpy.show(name = self.name, what = the_background_image, layer = "master")

        def link_locations(self,other): #This is a one way connection!
            #self.connections.append(other)
            return

        def link_locations_two_way(self,other): #Link it both ways. Great for adding locations after the fact, when you don't want to modify existing locations.
            # self.link_locations(other)
            # other.link_locations(self)
            return

        def add_object(self,the_object):
            if not the_object in self.objects:
                self.objects.append(the_object)

        def add_person(self,the_person):
            if not self.has_person(the_person):
                self.people.append(the_person)
            #TODO: add situational modifiers for the location

        def remove_person(self,the_person):
            if self.has_person(the_person):
                self.people.remove(the_person)

        def move_person(self,the_person,the_destination):
            if not isinstance(the_destination, Room):
                return
            if not the_destination.has_person(the_person) and self.has_person(the_person):
                self.remove_person(the_person)
                the_destination.add_person(the_person)

        def has_person(self,the_person):
            return the_person in self.people

        def get_person_list(self):
            return self.people

        def get_person_count(self):
            return len(self.people)

        def objects_with_trait(self,the_trait):
            return_list = []
            for object in self.objects:
                if object.has_trait(the_trait):
                    return_list.append(object)
            return return_list

        def has_object_with_trait(self,the_trait):
            if the_trait == "None":
                return True
            for object in self.objects:
                if object.has_trait(the_trait):
                    return True
            return False

        def get_object_with_trait(self, the_trait):
            if self.has_object_with_trait(the_trait):
                return get_random_from_list(self.objects_with_trait(the_trait))
            return None

        def get_object_with_name(self,name): #Use this to get objects from a room when you know what they should be named but don't have an object reference yet (ik
            for obj in self.objects:
                if obj.name == name:
                    return obj
            return None

        def valid_actions(self):
            return __builtin__.len(get_valid_actions())

        def get_valid_actions(self):
            actions = [x for x in self.actions if x.is_action_enabled() or x.is_disabled_slug_shown()]
            actions.sort(key = lambda x: x.priority if x.is_action_enabled() else -1000, reverse = True)
            return actions

        def get_lighting_conditions(self):
            return self.lighting_conditions[time_of_day]
