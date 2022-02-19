init -2 python:
    def offer_to_hire_requirement(the_person):
        if the_person.love < 10:
            return False
        elif the_person.has_role(employee_role):
            return False
        elif the_person.love < 20:
            return "Requires: 20 Love"
        elif mc.business.get_employee_count() >= mc.business.max_employee_count:
            return "At employee limit"
        return True

    def setup_employee_stats(the_person): #Centralized function for setting up employee stuff when you hire them
        if the_person.event_triggers_dict.get("employed_since", -1) == -1: # prevent fire / hire loop event triggering
            the_person.event_triggers_dict["employed_since"] = day
            mc.business.listener_system.fire_event("new_hire", the_person = the_person)
            for other_employee in mc.business.get_employee_list():
                town_relationships.begin_relationship(the_person, other_employee) #They are introduced to everyone at work, with a starting value of "Acquaintance"

    def stripper_hire(the_person):
        stripclub_strippers.append(the_person)

    def stripper_replace(the_person): # on_quit function called for strippers to make sure there's always someone working at the club. Also removes them from the list of dancers
        if the_person in stripclub_strippers:
            stripclub_strippers.remove(the_person)

        # add new stripper to replace the one that left
        new_stripper = create_random_person(start_sluttiness = renpy.random.randint(15,30), job = stripper_job)
        new_stripper.generate_home().add_person(new_stripper)


label stranger_hire_result(the_person): #Check to see if you want to hire someone.
    $ the_person.salary = the_person.calculate_base_salary()
    call hire_select_process([the_person, 1]) from _call_hire_select_process_stranger_hire_result
    if isinstance(_return, Person):
        call hire_someone(the_person) from _call_hire_someone_process_stranger_hire_result
        $ the_person.draw_person()
        return True
    else:
        $ the_person.draw_person()
        return False

    return False
