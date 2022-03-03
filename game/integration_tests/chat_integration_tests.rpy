init 1 python:
    integration_test_labels.append("test_chat_actions")

label test_chat_actions():
    $ test_person = mom
    "Testing general description ways."
    mom "This should be normal dialogue."
    $ renpy.say(mom, "This is statement equiavlent dialogue.")
    menu:
        "Dialogue displayed correctly.":
            pass

        "Test failed.":
            return False


    "Testing chat actions. Appropriate dialogue should be triggered, energy spent, ect."
    call small_talk_person(test_person) from _call_small_talk_person_4
    menu:
        "Small talk triggered correctly.":
            pass

        "Test failed.":
            return False

    "Testing complementing person."
    call compliment_person(test_person) from _call_compliment_person
    menu:
        "Complement triggered correctly.":
            pass

        "Test failed.":
            return False

    "Testing flirt with person."
    call flirt_person(test_person) from _call_flirt_person_1
    menu:
        "Flirt triggered correctly.":
            pass

        "Test failed.":
            return False

    "Testing date person."
    call date_person(test_person) from _call_date_person
    menu:
        "Date properly triggered.":
            pass

        "Test failed.":
            return False


    "Testing grope."
    call grope_person(test_person) from _call_grope_person
    menu:
        "Grope properly triggered.":
            pass

        "Test failed.":
            return False

    "Testing comannd person."
    call command_person(test_person) from _call_command_person
    menu:
        "Command properly triggered.":
            pass

        "Test failed.":
            return False


    return True
