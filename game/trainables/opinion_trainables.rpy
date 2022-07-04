init -2 python:
    def train_learn_opinion_requirement(the_person):
        if the_person.has_unknown_opinions():
            return True
        else:
            return "Unknown Opinions"

    def train_strengthen_opinion_requirement(the_person):
        if the_person.get_opinion_topics_list(include_unknown = False, include_hate = False, include_love = False):
            return True
        else:
            return "Known Moderate Opinion"

    def train_weaken_opinion_requirement(the_person):
        if the_person.get_opinion_topics_list(include_unknown = False):
            return True
        else:
            return "Known Opinion"

label train_learn_opinion_label(the_person):
    mc.name "Let's talk about you, what do you have strong feelings about?"
    the_person "Me? Oh, I don't know..."
    menu:
        "Tell me a normal opinion" if the_person.has_unknown_opinions(sexy_opinions = False):
            mc.name "Really, tell me anything at all."
            $ sexy_opinion = False

        "Tell me a sexy opinion" if the_person.has_unknown_opinions(normal_opinions = False):
            mc.name "Really, I promise I won't tell anyone else. You must have something interesting to share."
            $ sexy_opinion = True

    "You keep prompting [the_person.possessive_title] to share more information."

    if sexy_opinion:
        $ revealed_opinion = the_person.get_random_opinion(include_known = False, include_normal = False, include_sexy = True)
    else:
        $ revealed_opinion = the_person.get_random_opinion(include_known = False)

    if revealed_opinion:
        $ the_person.discover_opinion(revealed_opinion)
        "She can't resist for long. You listen as she tells you her opinion about [revealed_opinion]."
        if sexy_opinion:
            the_person "I hope that wasn't too personal to share..."
            mc.name "No, that's exactly what I wanted to know about. Thank you [the_person.title]."
        else:
            the_person "I hope that's what you wanted to hear about..."
            mc.name "It was perfect, thank you [the_person.title]."
        return True

    "[the_person.title] seems happy to share her opinions with you after some prompting."
    "Unfortunately, she doesn't have anything to tell you that you don't already know."
    return False

init 0 python:
    def build_opinion_change_menu(person, positive = True):
        opinion_list = person.get_opinion_topics_list(include_unknown = False)
        show_list = [[], []]
        list_name = ["Negative Opinion", "Positive Opinion"]
        for topic in opinion_list:
            score = person.get_opinion_score(topic)
            name = opinion_score_to_string(score) + " " + topic
            if positive and score in [-1, 1]:
                show_list[0 + (0 if score < 0 else 1)].append([name.title(), topic])
            elif not positive:
                show_list[0 + (0 if score < 0 else 1)].append([name.title(), topic])

        menu_list = []
        for i in [0, 1]:
            if show_list[i]:
                target_list = sorted(show_list[i], key = lambda x: x[1])
                target_list.insert(0, list_name[i])
                menu_list.append(target_list)

        menu_list.append(["Other", ["Never Mind","Never Mind"]])
        return menu_list

label train_strengthen_opinion_label(the_person): #TODO: Only have this enabled if she has a known moderate opinion
    mc.name "I want to talk to you about something."
    the_person "Okay, what do you want to talk about?"

    if mod_installed:
        call screen enhanced_main_choice_display(build_menu_items(build_opinion_change_menu(the_person, True)))
    else:
        call screen main_choice_display(build_opinion_change_menu(the_person, True))
    $ player_choice = _return

    if not player_choice == "Never Mind":
        mc.name "I think you have the right idea, but you could take it even further..."
        "[the_person.possessive_title] listens attentively as you talk to her."
        $ the_person.strengthen_opinion(player_choice)
        "After a while you feel confident you have strengthened her opinion."
        return True

    mc.name "On second thought, never mind."
    "She shrugs, completely unbothered."
    return False


label train_weaken_opinion_label(the_person): #TODO; Only have this enabled if you know of an opinion
    mc.name "I want to talk to you about something."
    the_person "Okay, what do you want to talk about?"

    if mod_installed:
        call screen enhanced_main_choice_display(build_menu_items(build_opinion_change_menu(the_person, False)))
    else:
        call screen main_choice_display(build_opinion_change_menu(the_person, False))
    $ player_choice = _return

    if not player_choice == "Never Mind":
        mc.name "You've got it all wrong, you need to think about this some more."
        mc.name "Here, let me explain it to you..."
        "[the_person.possessive_title] listens attentively while you mould her opinions of [player_choice]."
        $ the_person.weaken_opinion(player_choice)
        "When you're finished you feel confident that you have weakened her opinion."
        return True

    mc.name "On second thought, never mind."
    "She shrugs, completely unbothered."
    return False


init 0 python:
    def build_opinion_training_list(person, sexy_list):
        if sexy_list:
            opinion_train_options = the_person.get_sexy_opinions_list()
        else:
            opinion_train_options = the_person.get_normal_opinions_list()

        for known_opinion in person.get_opinion_topics_list(include_unknown = False):
            if known_opinion in opinion_train_options:
                opinion_train_options.remove(known_opinion) #Remove opinions we already know about.
        return sorted(opinion_train_options, key = lambda x: x)

    def build_opinion_training_menu(person, sexy_list):
        option_list = []
        for train_option in build_opinion_training_list(person, sexy_list):
            option_list.append([train_option.title(), train_option])

        if sexy_list:
            option_list.insert(0, "Sexy Opinions")
        else:
            option_list.insert(0, "Opinions")
        option_list.append(["Never Mind","Never Mind"])
        return [option_list]

label train_new_opinion_label(the_person, sexy_list = False):
    mc.name "I want to talk to you about something."
    the_person "Okay, what do you want to talk about?"

    if mod_installed:
        call screen enhanced_main_choice_display(build_menu_items(build_opinion_training_menu(the_person, sexy_list)))
    else:
        call screen main_choice_display(build_opinion_training_menu(the_person, sexy_list))
    $ player_choice = _return

    if not player_choice == "Never Mind":
        mc.name "Let's talk about [player_choice]."
        if the_person.get_opinion_score(player_choice) == 0:
            "[the_person.possessive_title] nods and listens attentively as you explain to her what her opinion should be."
            menu:
                "Create a positive opinion of [player_choice]":
                    $ the_person.create_opinion(player_choice)

                "Create a negative opinion of [player_choice]":
                    $ the_person.create_opinion(player_choice, start_positive = False)
            "It takes some time, but after a long conversation you feel confident you've put a strong opinion in [the_person.title]'s mind."
            return True
        else:
            the_person "[player_choice!c]? Yeah, I have some thoughts about that..."
            $ the_person.discover_opinion(player_choice)
            "It quickly becomes clear that [the_person.possessive_title] already has an opinion about [player_choice]."
            "You'll need a different approach if you want to change an opinion she has already formed."
            return False

    mc.name "On second thought, never mind."
    "She shrugs, completely unbothered."
    return False
