init -2 python:
    class Clothing_Images(renpy.store.object): # Stores a set of images for a single piece of clothing in a single position. The position is stored when it is put into the clothing object dict.
        breast_sizes = ["AA","A","B","C","D","DD","DDD","E","F","FF"]

        def __init__(self,clothing_name,position_name,is_top, body_dependent = True):
            self.images = {}
            self.clothing_name = clothing_name #Used for some debugging, not needed for the actual game logic.
            self.position_name = position_name #Used so we can access the correct .zip file

            for body in ["standard_body","thin_body","curvy_body","standard_preg_body"] if body_dependent else ["standard_body"]:
                for breast in self.breast_sizes if is_top else ["AA"]:
                    if clothing_name:
                        image_name = clothing_name+"_"+position_name+"_"+body+"_"+breast+".png"
                        self.images[body + "_" + breast] = image_name

        def get_image(self, body_type, breast_size = "AA" ): #Generates a proper Image object from the file path strings we have stored previously. Prevents object bloat by storing large objects repeatedly for everyone.
            index_string = body_type + "_" + breast_size
            if index_string in self.images:
                return VrenZipImage(self.position_name, self.images[index_string])

            return Image("character_images/empty_holder.png")

        def get_image_name(self, body_type, breast_size = "AA" ): #Generates a proper Image object from the file path strings we have stored previously. Prevents object bloat by storing large objects repeatedly for everyone.
            index_string = body_type + "_" + breast_size
            if index_string in self.images:
                return self.images[index_string]
            return "empty_holder.png"

    class Facial_Accessory_Images(renpy.store.object):
        supported_faces = ["Face_1","Face_2","Face_3","Face_4","Face_5","Face_6","Face_7","Face_8","Face_9","Face_11","Face_12","Face_13","Face_14",]
        supported_emotions = ["default","sad","happy","angry","orgasm"]

        def __init__(self,accessory_name,position):
            self.images = {}
            self.position_name = position
            self.special_modifiers = {self.position_name:"blowjob","kissing":"kissing"} #As of v0.35 all positions support the blowjob modifier so we can have good looking gags and a wider variety of facial expressions.

            for face in self.supported_faces:
                for emotion in self.supported_emotions:
                    self.images[face + "_" + emotion] = accessory_name + "_" + position + "_" + face + "_" + emotion + ".png" # Save the file string so we can generate a proper image from it easily later.
                    if position in self.special_modifiers:
                        self.images[face + "_" + emotion + "_" + self.special_modifiers[position]] = accessory_name + "_" + position + "_" + face + "_" + emotion + "_" + self.special_modifiers[position] + ".png"

        def get_image(self, face, emotion, special_modifier = None):
            index_string = face + "_" + emotion
            global mobile_zip_dict
            file = mobile_zip_dict[self.position_name]
            if special_modifier is not None:
                if index_string+"_"+special_modifier in file.namelist():
                    index_string += "_" + special_modifier #We only want to try and load special modifier images if they exist. Otherwise we use the unmodified image to avoid a crash. This lets us omit images we do not plan on actually using, such as glasses not needing blowjob poses.

            return VrenZipImage(self.position_name, self.images[index_string])

        def get_image_name(self, face, emotion, special_modifier = None):
            index_string = face + "_" + emotion
            global mobile_zip_dict
            file = mobile_zip_dict[self.position_name]
            if special_modifier is not None:
                if index_string+"_"+special_modifier in file.namelist():
                    index_string += "_" + special_modifier #We only want to try and load special modifier images if they exist. Otherwise we use the unmodified image to avoid a crash. This lets us omit images we do not plan on actually using, such as glasses not needing blowjob poses.

            return self.images[index_string]
