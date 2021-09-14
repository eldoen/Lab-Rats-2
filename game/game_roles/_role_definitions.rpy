# This file holds the initialization information and general storyline info for all of the roles in the game. Individual roles and individual files.
init -1 python:
    pay_strip_pose_list = [["Turn around","walking_away"],["Turn around and look back","back_peek"],["Hands down, ass up","standing_doggy"],["Be flirty","stand2"],["Be casual","stand3"],["Strike a pose","stand4"],["Move your hands out of the way","stand5"]]

    def prostitute_requirement(the_person):
        if mc.business.funds < 200:
            "Not enough cash"
        elif the_person.sexed_count >= 1:
            "She's worn out. Maybe later."
        else:
            return True

    def pay_strip_scene_build_strip_menu_items(the_person, strip_willingness):
        menu_items = [] #Tuple of menu things.
        # High obedience characters are more willing to be told to strip down (although they still expect to be paid for it)
        # Low obedience characters will strip off less when told but can be left to run the show on their own and will remove some.
        for item in the_person.outfit.get_unanchored():
            if not item.is_extension:
                (willingness, price, taboo_break) = pay_strip_scene_calculate_willingness_and_price(the_person, strip_willingness, item)

                taboo_break_string = ""
                if taboo_break:
                    taboo_break_string = " {image=gui/extra_images/taboo_break_token.png}"

                if willingness >= 100 - the_person.obedience:
                    if price < mc.business.funds:
                        display_string = "Strip " + item.name + taboo_break_string + "\n$" + str(price)
                    else:
                        display_string = "Strip " + item.name + taboo_break_string + "\nNot enough money (disabled)"

                    menu_items.append([display_string, [item,price]])

                else:
                    menu_items.append(["Strip " + item.name + "\nToo Slutty (disabled)", [item,-1]])

        menu_items.append(["Just watch","Watch"])
        menu_items.append(["Tell her to pose","Pose"])
        menu_items.append(["Finish the show","Finish"])
        return menu_items

    def pay_strip_scene_calculate_willingness_and_price(the_person, strip_willingness, tease_item):
        test_outfit = the_person.outfit.get_copy()
        test_outfit.remove_clothing(tease_item)
        willingness = the_person.effective_sluttiness(["underwear_nudity"]) + (5*the_person.get_opinion_score("not wearing anything")) - test_outfit.slut_requirement
        taboo_break = None

        if test_outfit.vagina_visible() and the_person.has_taboo("bare_pussy"):
            price = (strip_willingness - willingness) * 10
            taboo_break = "bare_pussy"
        elif test_outfit.tits_visible() and the_person.has_taboo("bare_tits"):
            price = (strip_willingness - willingness) * 10
            taboo_break = "bare_tits"
        elif test_outfit.underwear_visible() and the_person.has_taboo("underwear_nudity"):
            price = (strip_willingness - willingness) * 5
            taboo_break = "underwear_nudity"
        elif willingness >= 30: #She's slutty enough to do it for free!
            price = 0
        elif willingness >= 10:
            price = (strip_willingness - willingness) * 1
        else:
            price = (strip_willingness - willingness) * 3

        if price < 0:   # make sure price is never less than 0
            price = 0

        price = math.ceil((price/5.0))*5 #Round up to the next $5 increment
        return (willingness, price, taboo_break)

    def pay_strip_scene_get_pose(picked_pose):
        pose_menu_tuple = []
        for pose_tuple in pay_strip_pose_list:
            if not pose_tuple[1] == picked_pose:
                pose_menu_tuple.append(pose_tuple)
        pose_menu_tuple.append(["Never mind.",None])
        return renpy.display_menu(pose_menu_tuple,True,"Choice")

    def get_employee_role_actions():
        #EMPLOYEE ACTIONS#
        move_employee_action = Action("Move her to a new division", move_employee_requirement, "move_employee_label",
            menu_tooltip = "Move her to a new division, where her skills might be put to better use.")
        employee_complement_action = Action("Compliment her work", employee_complement_requirement, "employee_complement_work",
            menu_tooltip = "Offer a few kind words about her performance at work. Increases happiness and love, dependent on your charisma.")
        employee_insult_action = Action("Insult her work", employee_insult_requirement, "insult_recent_work",
            menu_tooltip = "Offer a few choice words about her performance at work. Lowers love and happiness, but is good for instilling obedience.")
        employee_pay_cash_action = Action("Pay her a cash bonus", employee_pay_cash_requirement, "employee_pay_cash_bonus",
            menu_tooltip = "A bonus in cold hard cash is good for obedience and happiness. The larger the reward the greater the effect.")
        employee_performance_review = Action("Start a performance review {image=gui/heart/Time_Advance.png}", employee_performance_review_requirement , "employee_performance_review",
            menu_tooltip = "Bring her to your office for a performance review. Get her opinion about her job, reward, punish, or fire her as you see fit. Can only be done once every seven days.")
        employee_paid_serum_test = Action("Test serum\n{color=#ff0000}{size=18}Costs: $100{/size}{/color}", employee_paid_serum_test_requirement, "employee_paid_serum_test_label",
            menu_tooltip = "Pay her to willingly take a dose of serum, per company policy.")
        employee_unpaid_serum_test = Action("Test serum", employee_unpaid_serum_test_requirement, "employee_unpaid_serum_test_label",
            menu_tooltip = "Give her a dose of serum to test on herself, per company policy.")
        employee_punishment = Action("Punish her", employee_punishment_hub_requirement, "employee_punishment_hub",
            menu_tooltip = "Punish her for any violations of company policy.", priority = 5)
        employee_generate_infraction = Action("Invent an infraction", employee_generate_infraction_requirement, "employee_generate_infraction_label",
            menu_tooltip = "Company policy here is so complicated it's nearly impossible to go a day without violating some minor rule. If you were paranoid, you might think it was written that way on purpose...")

        return [employee_paid_serum_test, employee_unpaid_serum_test, employee_complement_action, employee_insult_action, employee_pay_cash_action, employee_performance_review, move_employee_action, employee_punishment, employee_generate_infraction]

    def get_head_researcher_actions():
        #HEAD RESEARCHER ACTIONS#
        improved_serum_unlock = Action("Ask about advancing your research", improved_serum_unlock_requirement, "improved_serum_unlock_label",
            menu_tooltip = "Your basic initial research can only take you so far. You will need a breakthrough to discover new serum traits.", priority = 10)

        visit_nora_intro = Action("Visit Nora to try and advance your research", visit_nora_intro_requirement, "nora_intro_label",
            menu_tooltip = "Have your head researcher reach out to your old mentor to see if she can help advance your research.", priority = 10)

        advanced_serum_unlock_stage_1 = Action("Ask about advancing your research", advanced_serum_stage_1_requirement, "advanced_serum_stage_1_label",
            menu_tooltip = "Another breakthrough will unlock new serum traits.", priority = 10)

        advanced_serum_unlock_stage_3 = Action("Present with recording of prototype serum test", advanced_serum_stage_3_requirement, "advanced_serum_stage_3_label",
            menu_tooltip = "Your new head researcher will have to take over now, and this recording should help them.", priority = 10)

        futuristic_serum_unlock_stage_1 = Action("Ask about advancing your research", futuristic_serum_stage_1_requirement, "futuristic_serum_stage_1_label",
            menu_tooltip = "You will need another breakthrough to unlock new serum traits.", priority = 10) #First time you ask about it

        futuristic_serum_unlock_stage_2 = Action("Talk about the test subjects", futuristic_serum_stage_2_requirement, "futuristic_serum_stage_2_label",
            menu_tooltip = "Your head researcher needs willing, dedicated test subjects to advance your research any further.", priority = 10) #Talk to her to either select test subjects or get a refresher on what you need.

        fire_head_researcher_action = Action("Remove her as head researcher", fire_head_researcher_requirement, "fire_head_researcher",
            menu_tooltip = "Remove her as your head researcher so you can select another. Without a head researcher your R&D department will be less efficient.")

        return [fire_head_researcher_action,improved_serum_unlock,advanced_serum_unlock_stage_1, visit_nora_intro, advanced_serum_unlock_stage_3,futuristic_serum_unlock_stage_1, futuristic_serum_unlock_stage_2]

    def get_company_model_role_actions():
        #MODEL ACTIONS#
        model_ad_photo_list = Action("Shoot pictures for an advertisement {image=gui/heart/Time_Advance.png}", model_photography_list_requirement, "model_photography_list_label", priority = 5)

        fire_model_action = Action("Remove her as your company model", fire_model_requirment, "fire_model_label",
            menu_tooltip = "Remove her as your company model so you can give the position to someone else. Effects from existing ad campaigns will continue until they expire.")

        return [model_ad_photo_list, fire_model_action]

    def get_alexia_role_actions():
        #ALEXIA ACTIONS#
        alexia_ad_reintro = Action("Order photography equipment\n{color=#ff0000}{size=18}Costs: $500{/size}{/color}", alexia_ad_suggest_reintro_requirement, "alexia_ad_suggest_reintro_label")

        alexia_ad_photo_intro = Action("Shoot pictures for business cards {image=gui/heart/Time_Advance.png}", alexia_photography_intro_requirement, "alexia_photography_intro_label") #This vent leads to Alexia being given the model role.

        return [alexia_ad_reintro, alexia_ad_photo_intro]

    def get_sister_role_actions():
        #SISTER ACTIONS#
        sister_reintro_action = Action("Ask if she needs extra work", sister_reintro_action_requirement, "sister_reintro_label",
            menu_tooltip = "She was eager to make some money before, maybe she still is.")

        sister_serum_test_action = Action("Ask her to test serum", sister_serum_test_requirement, "sister_serum_test_label",
            menu_tooltip = "Have your sister test serum for you. Over time she will become more comfortable following your orders and making deals with you.")


        sister_strip_reintro_action = Action("Ask if she would strip for pay", sister_strip_reintro_requirement, "sister_strip_reintro_label",
            menu_tooltip = "She was eager to make some money, maybe she will be willing to strip for you if you pay her.")

        sister_strip_action = Action("Ask her to strip for you", sister_strip_requirement, "sister_strip_label",
            menu_tooltip = "Have your sister strip for you, in exchange for some money.", priority = 5)

        sister_boobjob_give_serum_action = Action("Give her some breast enhancement serum", sister_boobjob_give_serum_requirement, "sister_give_boobjob_serum_label",
            menu_tooltip = "Give your sister some serum, which she thinks will grow her boobs.", priority = 10)

        sister_boobjob_ask_action = Action("Talk to her about getting implants", sister_get_boobjob_talk_requirment, "sister_get_boobjob",
            menu_tooltip = "Talk to your sister about the implants she wants to get.", priority = 10)

        sister_mom_girlfriend_blessing_action = Action("Talk to her about Mom", mom_girlfriend_ask_blessing_requirement, "mom_girlfriend_sister_blessing",
            menu_tooltip = "Try and convince her to give you and Mom her blessing.", priority = 100)

        sister_girlfriend_return_action = Action("Give her the news", sister_girlfriend_return_requirement, "sister_girlfriend_return",
            menu_tooltip = "Tell her how your conversation with Mom went.", priority = 100)

        return [sister_reintro_action, sister_serum_test_action, sister_strip_reintro_action, sister_strip_action, sister_boobjob_give_serum_action, sister_boobjob_ask_action, sister_mom_girlfriend_blessing_action, sister_girlfriend_return_action]


    def get_mother_role_actions():
        #MOTHER ACTIONS#
        mother_offer_make_dinner = Action("Offer to make dinner {image=gui/heart/Time_Advance.png}", mom_offer_make_dinner_requirement, "mom_offer_make_dinner_label",
            menu_tooltip = "Earn some good will by making dinner for your mother and sister.", priority = 5)

        mom_work_promotion_two_prep_action = Action("Prepare for her interview", mom_work_promotion_two_prep_requirement, "mom_work_promotion_two_prep",
            menu_tooltip = "Help your mom prepare for her one-on-one interview.", priority = 10)

        mom_work_bigger_tits_reintro = Action("Talk to her about getting bigger tits", mom_work_secretary_replacement_bigger_tits_reintro_requirement, "mom_work_secretary_replacement_bigger_tits_reintro",
            menu_tooltip = "Talk to her about improving her natural assets, either with implants or by using some of your serum.", priority = 10)

        mom_sister_girlfriend_blessing_action = Action("Talk to her about Lily", sister_girlfriend_ask_blessing_requirement, "sister_girlfriend_mom_blessing",
            menu_tooltip = "Try and convince her to give you and Lily her blessing.", priority = 100)

        mom_girlfriend_return_action = Action("Give her the news", mom_girlfriend_return_requirement, "mom_girlfriend_return",
            menu_tooltip = "Tell her how your conversation with Lily went.", priority = 100)

        return [mother_offer_make_dinner, mom_work_promotion_two_prep_action, mom_work_bigger_tits_reintro, mom_sister_girlfriend_blessing_action, mom_girlfriend_return_action]


    def get_aunt_role_actions():

        #AUNT ACTIONS#
        aunt_help_move = Action("Help her move into her apartment {image=gui/heart/Time_Advance.png}", aunt_intro_moving_apartment_requirement, "aunt_intro_moving_apartment_label",
            menu_tooltip = "Help your aunt and your cousin move their stuff from your house to their new apartment. They're sure to be grateful, and it would give you a chance to snoop around.", priority = 5)

        aunt_share_drinks_action = Action("Share a glass of wine {image=gui/heart/Time_Advance.png}", aunt_share_drinks_requirement, "aunt_share_drinks_label",
            menu_tooltip = "Sit down with your aunt and share a glass or two of wine. Maybe a little bit of alcohol will loosen her up a bit.", priority = 10)

        return [aunt_help_move,aunt_share_drinks_action]

    def get_cousin_role_actions():
        #COUSIN ACTIONS#
        cousin_blackmail_action = Action("Blackmail her", cousin_blackmail_requirement, "cousin_blackmail_label",
            menu_tooltip = "Threaten to tell her mother about what she's been doing and see what you can get out of her.", priority = 10)

        return [cousin_blackmail_action]

    def get_girlfriend_role_actions():
        ask_break_up_action = Action("Break up with her", ask_break_up_requirement, "ask_break_up_label", menu_tooltip = "Breaking up may break her heart, but it'll be easier on her than catching you with another woman.")
        ask_get_boobjob_action = Action("Ask her to get a boob job\n{color=#ff0000}{size=18}Costs: $7000{/size}{/color}", ask_get_boobjob_requirement, "ask_get_boobjob_label", menu_tooltip = "A little silicone goes a long way. Ask her to get breast enhancement surgery for you.")
        girlfriend_ask_trim_pubes_action = Action("Ask her to trim her pubes", girlfriend_ask_trim_pubes_requirement, "girlfriend_ask_trim_pubes_label", menu_tooltip = "Ask her to do a little personal landscaping. Tell her to wax it off, grow it out, or shape it into anything in between.")

        return [ask_break_up_action, ask_get_boobjob_action, girlfriend_ask_trim_pubes_action]

    def get_girlfriend_role_dates():
        girlfriend_shopping_date = Action("Go shopping together {image=gui/heart/Time_Advance.png}", shopping_date_requirement, "shopping_date_intro", menu_tooltip = "Take her to the mall and do some shopping together.")
        return [girlfriend_shopping_date]

    def get_paramour_role_actions():
        plan_fuck_date_action = Action("Plan a fuck date at her place", fuck_date_requirement, "plan_fuck_date_label", menu_tooltip = "Pick a night to go over there and spend nothing but \"quality time\" with each other.")
        ask_get_boobjob_action = Action("Ask her to get a boob job\n{color=#ff0000}{size=18}Costs: $7000{/size}{/color}", ask_get_boobjob_requirement, "ask_get_boobjob_label", menu_tooltip = "A little silicone goes a long way. Ask her to get breast enhancement surgery for you.")
        girlfriend_ask_trim_pubes_action = Action("Ask her to trim her pubes", girlfriend_ask_trim_pubes_requirement, "girlfriend_ask_trim_pubes_label", menu_tooltip = "Ask her to do a little personal landscaping. Tell her to wax it off, grow it out, or shape it into anything in between.")
        girlfriend_shopping_date = Action("Go shopping together {image=gui/heart/Time_Advance.png}", shopping_date_requirement, "shopping_date_intro", menu_tooltip = "Take her to the mall and do some shopping together.")
        ask_leave_SO_action = Action("Ask her to leave her significant other for you", ask_leave_SO_requirement, "ask_leave_SO_label", menu_tooltip = "This affair has been secret long enough! Ask her to leave her significant other and make your relationship official.")

        return [plan_fuck_date_action, ask_get_boobjob_action, girlfriend_ask_trim_pubes_action, girlfriend_shopping_date, ask_leave_SO_action]

    def get_prostitute_role_actions():
        prostitute_action = Action("Pay her for sex\n{color=#ff0000}{size=18}Costs: $200{/size}{/color}", prostitute_requirement, "prostitute_label",
            menu_tooltip = "You know she's a prostitute, pay her to have sex with you.")

        return [prostitute_action]

    def get_student_role_actions():
        #STUDENT ACTIONS#
        #student_study_meetup_action = Action("Tutor her. {image=gui/heart/Time_Advance.png}", student_study_meetup_requirement, "student_study_meetup")
        student_reintro_action = Action("Ask about tutoring her", student_reintro_requirement, "student_reintro")
        student_study_propose_action = Action("Tutor her {image=gui/heart/Time_Advance.png}", student_study_propose_requirement, "student_study_propose")
        student_test_intro_action = Action("Tell her she can rewrite her exam.", student_test_intro_requirement, "student_test_intro")
        student_test_action = Action("Time to rewrite her exam. {image=gui/heart/Time_Advance.png}", student_test_requirement, "student_test")
        student_offer_job_reintro_action = Action("Offer her a job.", student_offer_job_requirement, "student_offer_job_reintro")
        return [student_reintro_action, student_study_propose_action, student_test_intro_action, student_test_action, student_offer_job_reintro_action]

    def get_freeuse_actions():
        #EMPLOYEE FREEUSE ACTIONS#
        freeuse_fuck = Action("Fuck her", freeuse_fuck_requirement, "employee_freeuse_fuck", menu_tooltip = "Grab your free use slut and have some fun with her.")
        return [freeuse_fuck]

    def get_nora_role_actions():
        #NORA ROLE#
        nora_student_exam_rewrite_request_action = Action("Ask her about the exam rewrite.", nora_student_exam_rewrite_request_requirement, "nora_student_exam_rewrite_request",
            menu_tooltip = "Ask if she can set up a new exam for your student.") # This crisis triggers if your RL ever gets to 2 or higher without her introing herself. Provides an alternative way to the university.

        return [nora_student_exam_rewrite_request_action]

    def get_trance_role_actions():
        trance_training_action = Action("Take advantage of her trance", trance_train_requirement, "trance_train_label", menu_tooltip = "Take advantage of her orgasm-induced trance and make some changes while she is highly suggestible.")
        return [trance_training_action]

    def get_breeder_role_actions():
        breeder_fuck_action = Action("Offer to knock her up", breeder_fuck_requirement, "breeder_fuck", menu_tooltip = "She wants to get pregnant, you could help with that.")
        return [breeder_fuck_action]

    def get_lactating_serum_role_actions():
        milk_for_serum_action = Action("Milk her for serum\n{color=#ff0000}{size=18}Costs: 15 {image=gui/extra_images/energy_token.png}{/size}{/color}", milk_for_serum_requirement, "milk_for_serum_label", menu_tooltip = "Those tits contain company property!")

        return [milk_for_serum_action]

    def get_hypno_orgasm_role_orgasm_actions():
        hypno_trigger_orgasm_action = Action("Trigger an orgasm", hypno_trigger_orgasm_requirement, "hypno_trigger_orgasm", menu_tooltip = "You've implanted a trigger word. You can make her cum whenever you want.")

        return [hypno_trigger_orgasm_action]

    def get_hypno_orgasm_role_online_actions():
        hypno_trigger_online_action = Action("Trigger an orgasm", hypno_trigger_orgasm_requirement, "hypno_trigger_online", menu_tooltip = "You've implanted a trigger word, it should work over a text message.")
        return [hypno_trigger_online_action]

label instantiate_roles(): #This section instantiates all of the key roles in the game. It is placed here to ensure it is properly created, saved, ect. by Renpy.
    #All of the role labels and requirements are defined in their own file, but their Action representations are stored here for saving purposes.
    python:

        employee_role = Role("Employee", get_employee_role_actions(),
            on_turn = employee_on_turn, on_day = employee_on_day)

        #EMPLOYEE BUSYWORK ACTIONS#
        employee_busywork_role = Role("Office Busywork", [], hidden = True) #TODO: Add some other actions to this role
        employee_role.link_role(employee_busywork_role) #Link this role to the employee_role, so they are removed at the same time.

        #EMPLOYEE HUMILIATING WORK ACTIONS#
        employee_humiliating_work_role = Role("Humiliating Office Work", [], hidden = True) #TODO: Add some other actions to this role.
        employee_role.link_role(employee_humiliating_work_role)

        employee_freeuse_role = Role("Freeuse Slut", get_freeuse_actions(), hidden = True)
        employee_role.link_role(employee_freeuse_role)

        head_researcher = Role("Head Researcher", get_head_researcher_actions())

        company_model_role = Role("Model", get_company_model_role_actions())

        steph_role = Role("Stephanie", [], hidden = True) #Used to hold any Stephanie specific actions not tied to another role, and to guarantee this is Steph even if she undergoes a personality change.

        student_role = Role("Student", get_student_role_actions())
        #NORA ROLE#
        # Note: Nora's role actions are assigned through Stephanie's events.
        nora_role = Role("Nora", get_nora_role_actions(), hidden = True)

        alexia_role = Role("Alexia", get_alexia_role_actions(), hidden = True) #Hide her role because we don't want to display it.

        sister_role = Role("Sister", get_sister_role_actions())

        mother_role = Role("Mother", get_mother_role_actions())

        aunt_role = Role("Aunt", get_aunt_role_actions())

        cousin_role = Role("Cousin", get_cousin_role_actions())

        student_role = Role("Student", get_student_role_actions())

        #COUSIN After start actions# - Actions that are meant to be added to her action list after the game has begun.
        #cousin_role.actions.append(cousin_talk_boobjob_again_action)

        ################
        #INTERNET ROLES#
        ################
        #These roles are given to any girl who has an account on the particular site, even if you don't know about it.

        instapic_role = Role("On InstaPic", [], hidden = True, on_turn = insta_on_turn, on_day = insta_on_day)

        dikdok_role = Role("On Dikdok", [], hidden = True, on_turn = dikdok_on_turn, on_day = dikdok_on_day)

        onlyfans_role = Role("On OnlyFanatics", [], hidden = True, on_turn = onlyfans_on_turn, on_day = onlyfans_on_day)

        ####################
        #RELATIONSHIP ROLES#
        ####################

        #GIRLFRIEND ACTIONS#
        # Give her gifts (bonus happiness + Love)
        # She tests serum for you for free.
        # Go on dates (Remove this option from the normal chat menu?)
        # If she has (of age) kids, meet them (and, amazingly, they're hot young women!)

        #Other things to add#
        # Enables new girlfriend specific crises.
        # Adds more love to seduction attempts (reduce love from other sources)
        # Fallout if your girlfriend catches you with someone else.


        girlfriend_role = Role("Girlfriend", get_girlfriend_role_actions(), role_dates = get_girlfriend_role_dates()) #Your girlfriend, and she's not in a relationship with anyone else
        #Getting married is some kind of victory for the game?


        sister_girlfriend_role = Role("Girlfriend", get_girlfriend_role_actions(), role_dates = get_girlfriend_role_dates(), looks_like = girlfriend_role) #Sister specific girlfriend role.

        mom_girlfriend_role = Role("Girlfriend", get_girlfriend_role_actions(), role_dates = get_girlfriend_role_dates(), looks_like = girlfriend_role) #Sister specific girlfriend role.

        #affair ACTIONS
        # Sneaky versions of all of the normal girlfriend stuff
        # Have her get money from her (b/f/h) and give it to you.
        # Convince her to leave her (boyfriend/fiance/husband) for you. Changes to her being your girlfriend.
        # Start to blackmail her for money or sex.

        affair_role = Role("Paramour", get_paramour_role_actions()) #A woman who is in a relationship but also wants to fuck you because of love (rather than pure sluttiness, where she thinks that's normal)


        ###################
        ### TRANCE ROLE ###
        ###################

        trance_role = Role("In a Trance", actions = get_trance_role_actions(), on_turn = trance_on_turn, on_day = trance_on_day)
        heavy_trance_role = Role("In a Deep Trance", actions = get_trance_role_actions(), on_turn = trance_on_turn, on_day = trance_on_day, looks_like = trance_role)
        very_heavy_trance_role = Role("In a Very Deep Trance", actions = get_trance_role_actions(), on_turn = trance_on_turn, on_day = trance_on_day, looks_like = heavy_trance_role)

        #######################
        ### TRAINABLE ROLES ###
        #######################

        breeder_role = Role("Eager Breeder", actions = get_breeder_role_actions()) #TODO: Add an on-day (or on-turn?) LTE when her fertility is really high and she begs you to fuck her.
        hypno_orgasm_role = Role("Hypno Orgasm", actions = get_hypno_orgasm_role_orgasm_actions(), hidden = True, on_turn = hypno_orgasm_on_turn, internet_actions = get_hypno_orgasm_role_online_actions())

        ###################
        ### OTHER ROLES ###
        ###################

        prostitute_role = Role("Prostitute", get_prostitute_role_actions())
        pregnant_role = Role("Pregnant", [], hidden = True)
        lactating_serum_role = Role("Lactating Serum", get_lactating_serum_role_actions(), hidden = True, on_turn = lactating_serum_on_turn)
    return




label pay_strip_scene(the_person):
    # TODO: Figure out where this scene should go, since this file should be a pure role-define section.
    #A loop where someone strips if you pay them. Not necessarily limited to the Lily-MC relationship.
    #Concept: tell the girl what position to stand in and ask her to take things off for you. If her outfit is conservative she'll strip for free, when it starts to get slutty she'll want extra cash.
    #High obedience will sub in for sluttiness; an obedient girl will strip just because you ask.
    #Compliment, insult, etc. to change some of her stats.

    #Requirements: Person can be told to stand in a few different positions. Some are unlocked at higher sluttiness.
    #Requirements: Person can be asked to take off clothing.
    #Requirements: Some they will strip off on their own.
    #Requirements: Person will demand some amount of $$$ while stripping if they feel it's slutty.
    #Requirements: Person will have different descriptions of stripping/dancing depending on sluttiness.
    #Optional: Some way to ask the person to change into a different outfit.
    #Optional: Way to progress from strip tease to sex and/or masturbation.

    $ pose_list = [["Turn around","walking_away"],["Turn around and look back","back_peek"],["Be flirty","stand2"],["Be casual","stand3"],["Strike a pose","stand4"],["Move your hands out of the way","stand5"],["Hands down, ass up","standing_doggy"]]
    $ pose_dances = {} #Dict that maps poses to animations that look good for them.


    $ picked_pose = the_person.idle_pose #She starts in her idle pose (which is a string)
    $ ran_num = renpy.random.randint(0,3) #Produce 4 different descriptions at each level to help keep this interesting.

    # strip_willingness is a measure of how into the whole strip process the girl is. The less dressed she get the more embarrassed she'll get,
    # the more slutty the more she'll tease you, take clothing off willingly, etc.
    $ strip_willingness = the_person.effective_sluttiness("underwear_nudity") + (5*the_person.get_opinion_score("not wearing anything")) - the_person.outfit.slut_requirement
    #If there are other things that influence how willing a person is to strip they go here!

    $ keep_stripping = True #When set to false the loop ends and the strip show stops.

    while keep_stripping:
        $ the_person.draw_person(position = picked_pose)
        if strip_willingness < 0:
            if ran_num == 0:
                "[the_person.title] blushes intensely while you watch her."
            elif ran_num == 1:
                if the_person.has_large_tits():
                    "[the_person.title] instinctively tries to cover herself with her hands, but her large tits make it a difficult task."
                else:
                    "[the_person.title] instinctively tries to cover herself with her hands."
            elif ran_num == 2:
                the_person "Oh my god..."
                "[the_person.title] covers her eyes for a moment and looks away."
            else:
                "[the_person.title] shakes her head and mutters to herself."
                the_person "I can't believe I'm doing this..."

        elif strip_willingness < 10:
            if ran_num == 0:
                "[the_person.title] stands awkwardly in front of you and avoids making eye contact."
            elif ran_num == 1:
                if the_person.has_large_tits():
                    "[the_person.title] shifts her weight from side to side while you watch her. The small movements still make her big tits jiggle around."
                else:
                    "[the_person.title] shifts her weight from side to side while you watch her."
            elif ran_num == 2:
                "You get a good look at [the_person.title] while she stands in front of you."
            else:
                "[the_person.title] blushes and looks around the room to avoid making eye contact."

        elif strip_willingness < 30:
            $the_clothing = the_person.outfit.remove_random_any(top_layer_first = True, exclude_feet = True, do_not_remove = True) #She's slutty enough that she wants to tease you a little more
            if ran_num == 0:
                if the_clothing is not None:
                    "[the_person.title] pulls at her [the_clothing.display_name] seductively."
                    the_person "Mmm, I bet you want me to take this off, right?"
                else:
                    "[the_person.title] runs her hands down her body seductively."
                    the_person "Mmm, I bet you want to get your hands on me now, right?"

            elif ran_num == 1:
                if the_person.has_large_tits():
                    "[the_person.title] moves her body side to side for you, letting her large tits bounce and jiggle while you watch."
                else:
                    "[the_person.title] moves her body side to side for you while you watch."

            elif ran_num == 2:
                if the_clothing is not None:
                    "[the_person.title] slips a hand under her [the_clothing.display_name] and starts to pull it off."
                    the_person "Maybe I should just... slip this off. What do you think?"
                else:
                    if the_person.has_large_tits():
                        "[the_person.title]'s hands slide up and down her body. She cups one of her sizeable breast and squeezes it, pinching her own nipple while she does."
                    else:
                        "[the_person.title]'s hands slide up and down her body. She rubs her small breasts, paying special attention to their firm nipples."
            else:
                the_person "I hope you're enjoying the show [the_person.mc_title]."
                "She wiggles her hips for you and winks."
            $ the_clothing = None

        else: #strip_willingness >= 30
            $the_clothing = the_person.outfit.remove_random_any(top_layer_first = True, exclude_feet = True, do_not_remove = True) #She's slutty enough that she wants to tease you a little more
            if ran_num == 0:
                if the_clothing is not None:
                    "[the_person.title] pulls at her [the_clothing.display_name]."
                    the_person "I'm going to have to get this out of the way before we can have any fun."
                else:
                    "[the_person.title] runs her hands over her own body."
                    the_person "Oh [the_person.mc_title], I think I'm going to need more than your eyes on me soon..."

            elif ran_num == 1:
                "[the_person.title] puts her hands up in the air and spins around. You get a great look at her body as she enjoys herself."

            elif ran_num == 2:
                if the_clothing is not None:
                    the_person "Don't you just think all of this clothing is just useless? How about I take it all off for you... would you like that?"
                else:
                    "[the_person.title] takes a wider stances and slides her hands down her own thighs, all while maintaining eye contact with you."
                    the_person "You're looking so good today [the_person.mc_title], did you know that?"

            else:
                "[the_person.title] wiggles her hips side to side and bites her bottom lip, as if imagining some greater pleasure yet to come."
            $ the_clothing = None


        $ strip_choice = renpy.display_menu(pay_strip_scene_build_strip_menu_items(the_person, strip_willingness),True,"Choice")
        if strip_choice == "Watch":
            if renpy.random.randint(0,1) == 0:
                $ the_clothing = the_person.outfit.remove_random_any(top_layer_first = True, exclude_feet = True, do_not_remove = True) #The clothing item she's considering taking off
                $ free_spirit_threshold = 40 + (100 - the_person.obedience)
                if renpy.random.randint(0,100) < free_spirit_threshold: #She's independent enough to strip, change pose, etc. on her own.
                    if the_clothing:
                        $ (willingness, price, taboo_break) = pay_strip_scene_calculate_willingness_and_price(the_person, strip_willingness, the_clothing)

                    if the_clothing and willingness >= (the_person.obedience-100): #A more obedient person is less willing to strip without being told to. A less obedient person will strip further on their own.
                        if price > 0:
                            "[the_person.title] steps a little closer to you and plays with the edge of her [the_clothing.display_name]."
                            if taboo_break: #TODO: If this style of stripping becomes more important this dialogue should be personality based (mainly for family related dialogue)
                                if taboo_break == "bare_pussy":
                                    the_person "Would you like a look at my pussy? How about... $[price] and I'll take off my [tease_item.display_name]."
                                elif taboo_break == "bare_tits":
                                    the_person "So, would you like to see my tits? Just, oh... $[price] and I'll take off my [tease_item.display_name]."
                                else: #Underwear_nudity
                                    the_person "Want to see what I'm wearing underneath this [tease_item.display_name]? Just $[price] and I'll show you."
                            else:
                                the_person "$[price] and I'll take this off for you..."

                            menu:
                                "Pay her\n{color=#ff0000}{size=18}Costs: $[price]{/size}{/color}" if price <= mc.business.funds:
                                    "You pull the cash out of your wallet and hand it over."
                                    $ mc.business.funds += -price
                                    $ the_person.change_obedience(-1)
                                    $ the_person.change_slut(1, 40)
                                    $ the_person.draw_animated_removal(the_clothing, position = picked_pose)
                                    "[the_person.title] takes it, puts it to the side, and starts to slide her [the_clothing.display_name] off."
                                    if the_person.update_outfit_taboos():
                                        "She seems momentarily uneasy about undressing, but shakes the feeling quickly and returns her attention to you."

                                "Pay her\n{color=#ff0000}{size=18}Requires: $[price]{/size}{/color} (disabled)" if price > mc.business.funds:
                                    pass

                                "Don't pay her":
                                    mc.name "I think you look good with it on."
                                    "[the_person.title] seems disappointed but shrugs and keeps going."

                        else:
                            $ the_person.draw_animated_removal(the_clothing, position = picked_pose)
                            "You watch as [the_person.title] grabs their [the_clothing.display_name] and pulls it off."
                    else:
                        #She has nothing to strip off or she's as slutty as she's willing to get
                        "[the_person.title] seems comfortable just the way she is."

                else: #She doesn't quite know what to do without you telling her.
                    "Without any direction [the_person.title] just keeps doing what she was doing."
                $ the_clothing = None
            else:
                #She decides to change pose half the time.
                $ new_pose = get_random_from_list(pay_strip_pose_list)
                if not new_pose[1] == picked_pose:
                    $ picked_pose = new_pose[1]
                    "While you're watching [the_person.title] changes pose so you can see her from a different angle."
                else:
                    "[the_person.title] seems comfortable just the way she is."


        elif strip_choice == "Pose":
            #You ask her to change into a different pose
            mc.name "I want to see you from a different angle."
            $ pose_choice = pay_strip_scene_get_pose(picked_pose)
            if pose_choice is not None:
                $ picked_pose = pose_choice
                "[the_person.title] nods and moves for you."

            else:
                mc.name "Never mind, you look perfect like this."

        elif strip_choice == "Finish":
            $ keep_stripping = False
            mc.name "That was fun [the_person.title], I think that's enough."
            if strip_willingness < 0:
                "[the_person.title] sighs happily."
                the_person "Oh my god, I thought I was going to die of embarrassment!"
            elif strip_willingness < 20:
                the_person "Oh, okay. That... wasn't as bad as I thought it was going to be, at least."
            else:
                the_person "Oh, is that all you wanted to see? I feel like we were just getting started!"

        else: #The only other result is an actual strip. Pay the cash, remove the piece and loop or end.
            $ mc.business.funds += -strip_choice[1]
            $ test_outfit = the_person.outfit.get_copy() #We use a temp copy so that we can get her reaction first.
            $ test_outfit.remove_clothing(strip_choice[0])
            $ the_clothing = strip_choice[0]

            $ taboo_break = None
            if test_outfit.vagina_visible() and the_person.has_taboo("bare_pussy"):
                $ taboo_break = "bare_pussy"
            elif test_outfit.tits_visible() and the_person.has_taboo("bare_tits"):
                $ taboo_break = "bare_tits"
            elif test_outfit.underwear_visible() and the_person.has_taboo("underwear_nudity"):
                $ taboo_break = "underwear_nudity"

            $ strip_willingness = the_person.effective_sluttiness("underwear_nudity") + (5*the_person.get_opinion_score("not wearing anything")) - test_outfit.slut_requirement
            mc.name "Take off your [the_clothing.display_name] for me."
            if taboo_break: #Always use special dialogue for the taboo breaks
                $ the_person.call_dialogue(taboo_break + "_taboo_break", the_clothing = the_clothing)
                $ the_person.break_taboo(taboo_break)

            if strip_choice[1] > 0:
                if strip_willingness < 0:
                    "You pull some cash from your wallet and offer it to [the_person.title]. She takes it and looks at it for a long second."
                    the_person "Oh my god... I shouldn't be doing this..."
                    $ the_person.change_obedience(2)
                    $ the_person.change_slut(1, 40)
                    $ the_person.draw_animated_removal(strip_choice[0], position = picked_pose)
                    "Nevertheless, she keeps the money and pulls off her [the_clothing.display_name]."
                elif strip_willingness < 20:
                    "You pull some cash out from your wallet and hand it over to [the_person.title]. She puts it to the side and grabs her [the_clothing.display_name]."
                    the_person "Ready?"
                    $ the_person.change_obedience(1)
                    $ the_person.change_slut(1, 40)
                    $ the_person.draw_animated_removal(strip_choice[0], position = picked_pose)
                    "You nod and [the_person.title] pulls off the piece of clothing, throwing it to the side."
                else:
                    "You're still pulling out cash as [the_person.title] strips off her [the_clothing.display_name] and chucks it to the side."
                    $ the_person.draw_animated_removal(strip_choice[0], position = picked_pose)
                    the_person "Thank you!"
                    "She plucks the cash from your hand and quickly puts it away."

            else: #She'll only do it for free if she's becoming less slutty (ie taking off lingerie, bondage gear, etc.) or if she's very slutty anyways.
                the_person "Is that all? Well, I think that's easy."
                $ the_person.draw_animated_removal(strip_choice[0], position = picked_pose)
                "[the_person.title] strips off her [the_clothing.display_name] for free, leaving it on the ground at her feet."

            $ test_outfit = None
            $ the_clothing = None
        $ strip_choice = None
        $ taboo_break = None
    return


label prostitute_label(the_person):
    mc.name "[the_person.title], I'm looking for a friend to spend some time with. Are you available?"
    the_person "If you're paying I am."
    $ mc.business.funds += -200
    $ the_person.change_obedience(1)

    $ the_person.add_situational_obedience("prostitute", 40, "I'm being paid for this, I should do whatever he wants me to do.")
    call fuck_person(the_person, private = True, ignore_taboo = True) from _call_fuck_person_23 #She's a prostitute, she doesn't care about normal taboos
    $ the_report = _return

    $ the_person.clear_situational_obedience("prostitute")
    if the_report.get("girl orgasms", 0) > 0:
        "It takes [the_person.title] a few moments to catch her breath."
        the_person "Maybe I should be paying you... Whew!"
    $ the_person.review_outfit()
    $ the_person.draw_person()

    the_person "That was fun, I hope you had a good time [the_person.mc_title]."
    $ the_person.draw_person(position = "walking_away")
    "She gives you a quick peck on the cheek, turns around, and walks away."
    $ clear_scene()
    jump game_loop  # for her the encounter is finished, so end talk.
