# This file holds the initialization information and general storyline info for all of the roles in the game. Individual roles and individual files.
init -1 python:
    def always_true(the_person):
        return True

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

        sister_boobjob_ask_action = Action("Talk about getting implants", sister_get_boobjob_talk_requirment, "sister_get_boobjob",
            menu_tooltip = "Talk to your sister about the implants she wants to get.", priority = 10)

        sister_mom_girlfriend_blessing_action = Action("Talk about Mom", mom_girlfriend_ask_blessing_requirement, "mom_girlfriend_sister_blessing",
            menu_tooltip = "Try and convince her to give you and Mom her blessing.", priority = 100)

        sister_girlfriend_return_action = Action("Give her the news", sister_girlfriend_return_requirement, "sister_girlfriend_return",
            menu_tooltip = "Tell her how your conversation with Mom went.", priority = 100)

        return [sister_reintro_action, sister_serum_test_action, sister_strip_reintro_action, sister_strip_action, sister_boobjob_give_serum_action, sister_boobjob_ask_action, sister_mom_girlfriend_blessing_action, sister_girlfriend_return_action]

    def get_sister_student_role_actions():
        sister_hire_offer_action = Action("Offer to hire her", sister_offer_to_hire_requirement, "sister_offer_to_hire",
            menu_tooltip = "Offer her a job at your company. You'll have to convince her to drop out of school first...")

        return [sister_hire_offer_action]

    def get_mother_role_actions():
        #MOTHER ACTIONS#
        mother_offer_make_dinner = Action("Offer to make dinner {image=gui/heart/Time_Advance.png}", mom_offer_make_dinner_requirement, "mom_offer_make_dinner_label",
            menu_tooltip = "Earn some good will by making dinner for your mother and sister.", priority = 5)

        mom_work_promotion_two_prep_action = Action("Prepare for her interview", mom_work_promotion_two_prep_requirement, "mom_work_promotion_two_prep",
            menu_tooltip = "Help your mom prepare for her one-on-one interview.", priority = 10)

        mom_work_bigger_tits_reintro = Action("Talk about getting bigger tits", mom_work_secretary_replacement_bigger_tits_reintro_requirement, "mom_work_secretary_replacement_bigger_tits_reintro",
            menu_tooltip = "Talk to her about improving her natural assets, either with implants or by using some of your serum.", priority = 10)

        mom_sister_girlfriend_blessing_action = Action("Talk about Lily", sister_girlfriend_ask_blessing_requirement, "sister_girlfriend_mom_blessing",
            menu_tooltip = "Try and convince her to give you and Lily her blessing.", priority = 100)

        mom_girlfriend_return_action = Action("Give her the news", mom_girlfriend_return_requirement, "mom_girlfriend_return",
            menu_tooltip = "Tell her how your conversation with Lily went.", priority = 100)

        return [mother_offer_make_dinner, mom_work_promotion_two_prep_action, mom_work_bigger_tits_reintro, mom_sister_girlfriend_blessing_action, mom_girlfriend_return_action]

    def get_mother_associate_actions():
        mom_convince_quit_action = Action("Convince her to quit her job", mom_convince_quit_requirement, "mom_convince_quit_label", priority = -5)

        return [mom_convince_quit_action]

    def get_aunt_role_actions():

        #AUNT ACTIONS#
        aunt_help_move = Action("Help her move into her apartment {image=gui/heart/Time_Advance.png}", aunt_intro_moving_apartment_requirement, "aunt_intro_moving_apartment_label",
            menu_tooltip = "Help your aunt and your cousin move their stuff from your house to their new apartment. They're sure to be grateful, and it would give you a chance to snoop around.", priority = 5)

        aunt_share_drinks_action = Action("Share a glass of wine {image=gui/heart/Time_Advance.png}", aunt_share_drinks_requirement, "aunt_share_drinks_label",
            menu_tooltip = "Sit down with your aunt and share a glass or two of wine. Maybe a little bit of alcohol will loosen her up a bit.", priority = 10)

        aunt_offer_hire_action = Action("Offer to hire her", aunt_offer_hire_requirement, "aunt_offer_hire", priority = -5)

        return [aunt_help_move,aunt_share_drinks_action, aunt_offer_hire_action]

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
        plan_fuck_date_action = Action("Plan a fuck date at her place", fuck_date_requirement, "plan_fuck_date_label", menu_tooltip = "Pick a night to go over there and spend nothing but \"quality time\" with each other.")
        girlfriend_shopping_date = Action("Go shopping together {image=gui/heart/Time_Advance.png}", shopping_date_requirement, "shopping_date_intro", menu_tooltip = "Take her to the mall and do some shopping together.")
        return [plan_fuck_date_action, girlfriend_shopping_date]

    def get_paramour_role_actions():
        ask_get_boobjob_action = Action("Ask her to get a boob job\n{color=#ff0000}{size=18}Costs: $7000{/size}{/color}", ask_get_boobjob_requirement, "ask_get_boobjob_label", menu_tooltip = "A little silicone goes a long way. Ask her to get breast enhancement surgery for you.")
        girlfriend_ask_trim_pubes_action = Action("Ask her to trim her pubes", girlfriend_ask_trim_pubes_requirement, "girlfriend_ask_trim_pubes_label", menu_tooltip = "Ask her to do a little personal landscaping. Tell her to wax it off, grow it out, or shape it into anything in between.")
        ask_leave_SO_action = Action("Ask her to leave her significant other for you", ask_leave_SO_requirement, "ask_leave_SO_label", menu_tooltip = "This affair has been secret long enough! Ask her to leave her significant other and make your relationship official.")

        return [ask_get_boobjob_action, girlfriend_ask_trim_pubes_action, ask_leave_SO_action]

    def get_paramour_role_dates():
        plan_fuck_date_action = Action("Plan a fuck date at her place", fuck_date_requirement, "plan_fuck_date_label", menu_tooltip = "Pick a night to go over there and spend nothing but \"quality time\" with each other.")
        return [plan_fuck_date_action]

    def get_unemployed_role_actions():
        unemployed_hire_action = Action("Offer to hire her", offer_to_hire_requirement, "unemployed_offer_hire")
        return [unemployed_hire_action]

    def get_unimportant_job_role_actions():
        unimportant_hire_action = Action("Offer to hire her", offer_to_hire_requirement, "unimportant_job_offer_hire")
        return [unimportant_hire_action]

    def get_stripper_role_actions():
        stripper_dance_action = Action("Ask for a private dance\n{color=#ff0000}{size=18}Costs: $100{/size}{/color}", stripper_private_dance_requirement, "stripper_private_dance_label",
            menu_tooltip = "Ask her to a back room for a private dance.")
        stripper_hire_action = Action("Offer to hire her", offer_to_hire_requirement, "stripper_offer_hire")

        return [stripper_dance_action, stripper_hire_action]

    def get_prostitute_role_actions():
        prostitute_action = Action("Pay her for sex\n{color=#ff0000}{size=18}Costs: $200{/size}{/color}", prostitute_requirement, "prostitute_label",
            menu_tooltip = "You know she's a prostitute, pay her to have sex with you.")
        prostitute_hire_action = Action("Offer to hire her", offer_to_hire_requirement, "prostitute_hire_offer")
        return [prostitute_action, prostitute_hire_action]

    def get_student_role_actions():
        #STUDENT ACTIONS#
        #student_study_meetup_action = Action("Tutor her. {image=gui/heart/Time_Advance.png}", student_study_meetup_requirement, "student_study_meetup")
        student_reintro_action = Action("Ask about tutoring her", student_reintro_requirement, "student_reintro")
        student_study_propose_action = Action("Tutor her {image=gui/heart/Time_Advance.png}", student_study_propose_requirement, "student_study_propose")
        student_test_intro_action = Action("Tell her she can rewrite her exam", student_test_intro_requirement, "student_test_intro")
        student_test_action = Action("Time to rewrite her exam {image=gui/heart/Time_Advance.png}", student_test_requirement, "student_test")
        student_offer_job_reintro_action = Action("Offer her a job", student_offer_job_requirement, "student_offer_job_reintro")
        return [student_reintro_action, student_study_propose_action, student_test_intro_action, student_test_action, student_offer_job_reintro_action]

    def get_freeuse_actions():
        #EMPLOYEE FREEUSE ACTIONS#
        freeuse_fuck = Action("Fuck her", freeuse_fuck_requirement, "employee_freeuse_fuck", menu_tooltip = "Grab your free use slut and have some fun with her.")
        return [freeuse_fuck]

    def get_nora_role_actions():
        #NORA ROLE#
        nora_student_exam_rewrite_request_action = Action("Ask her about the exam rewrite", nora_student_exam_rewrite_request_requirement, "nora_student_exam_rewrite_request",
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

    def get_city_rep_role_actions():
        city_rep_negotiate_action = Action("Negotiate Deal", city_rep_negotiate_requirement, "city_rep_negotiate")
        city_rep_bribe_action = Action("Offer a Bribe", city_rep_bribe_requirement, "city_rep_bribe")
        city_rep_order_action = Action("Order her to leave", city_rep_order_requirement, "city_rep_order")
        city_rep_seduce_action = Action("Try to seduce her", city_rep_seduce_requirement, "city_rep_seduce")
        city_rep_hire_action = Action("Offer to hire her", offer_to_hire_requirement, "city_rep_offer_hire")
        return [city_rep_negotiate_action, city_rep_bribe_action, city_rep_order_action, city_rep_seduce_action, city_rep_hire_action]

    def get_city_rep_role_trainables():
        city_rep_dressup_training = Trainable("City_Rep_Dressup", "city_rep_dressup_training", "Slutty Work Uniform.", unlocked_function = city_rep_dressup_training_requirement, doubling_amount = 4)
        city_rep_penalty_reduction_training = Trainable("City_Rep_Pen_Reduct", "city_rep_penalty_reduction_training", "Reduce Penalty Severity", 200, city_rep_penalty_reduction_training_requirement)
        city_rep_internal_sabotage_training = Trainable("City_Rep_Sabot", "city_rep_internal_sabotage_training", "Sabotage Investigations", 400, city_rep_internal_sabotage_training_requirement)
        return [city_rep_dressup_training, city_rep_penalty_reduction_training, city_rep_internal_sabotage_training]

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
            on_turn = employee_on_turn, on_day = employee_on_day, hidden = True)

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

        #NORA ROLE#
        # Note: Nora's role actions are assigned through Stephanie's events.
        nora_role = Role("Nora", get_nora_role_actions(), hidden = True)

        alexia_role = Role("Alexia", get_alexia_role_actions(), hidden = True) #Hide her role because we don't want to display it.

        sister_role = Role("Sister", get_sister_role_actions(), on_day = sister_on_day)
        sister_student_role = Role("Student", get_sister_student_role_actions(), hidden = True)

        mother_role = Role("Mother", get_mother_role_actions(), on_day = mom_on_day)
        mom_associate_role = Role("Business Associate", get_mother_associate_actions(), hidden = True) #Used for the different jobs she holds in various events
        mom_secretary_role = Role("Personal Associate", get_mother_associate_actions(), hidden = True) #TODO: Have the ability to link random events to roles.

        aunt_role = Role("Aunt", get_aunt_role_actions())

        cousin_role = Role("Cousin", get_cousin_role_actions())

        #GENERIC STUDENT
        generic_student_role = Role("Student", [], hidden = True)

        student_role = Role("Student", get_student_role_actions())

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

        #Setting Harem Roles = Polyamory, Polyamorous relationship for more ideas refer to
        #https://affirmativecouch.com/polyamorous-relationship-structures/ 
        # Hierarchial Polyamory would be what everyone is familiar with as a Harem
        # mc viewed as the Primary, then rest would fall under the following
        # Dependant Polyamory - chooses to live with mc
        # Solo Polyamory - chooses to live seperately
        # Polycules formed by individuals... so they might want only one on one with mc, but eventually threesome with another
        # - so you can make a relationship dependant on polycules = ie Emily will do threesome with mc and Sarah, but doesn't like others that way
        # - could use the relationship structure to define polycules between persons in the harem?
        # harem_role/cousin/aunt when they are girlfriend and added to the poly they get the generic girlfriend role, this is just to keep things tied up
        harem_role = Role("Girlfriend in Polyamory", get_harem_role_actions(), role_dates = get_harem_role_dates(), looks_like = girlfriend_role) #Generic specific girlfriend role.
        cousin_girlfriend_role = Role("Girlfriend", get_girlfriend_role_actions(), role_dates = get_girlfriend_role_dates(), looks_like = girlfriend_role) #Generic specific girlfriend role.
        aunt_girlfriend_role = Role("Girlfriend", get_girlfriend_role_actions(), role_dates = get_girlfriend_role_dates(), looks_like = girlfriend_role) #Generic girlfriend role.


        sister_girlfriend_role = Role("Girlfriend", get_girlfriend_role_actions(), role_dates = get_girlfriend_role_dates(), looks_like = girlfriend_role) #Generic specific girlfriend role.
        mom_girlfriend_role = Role("Girlfriend", get_girlfriend_role_actions(), role_dates = get_girlfriend_role_dates(), looks_like = girlfriend_role) #Generic specific girlfriend role.

        #affair ACTIONS
        # Sneaky versions of all of the normal girlfriend stuff
        # Have her get money from her (b/f/h) and give it to you.
        # Convince her to leave her (boyfriend/fiance/husband) for you. Changes to her being your girlfriend.
        # Start to blackmail her for money or sex.

        affair_role = Role("Paramour", get_paramour_role_actions(), role_dates = get_paramour_role_dates()) #A woman who is in a relationship but also wants to fuck you because of love (rather than pure sluttiness, where she thinks that's normal)


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
        unemployed_role = Role("Unemployed", get_unemployed_role_actions(), hidden = True)
        unimportant_job_role = Role("Unimportant Job", get_unimportant_job_role_actions(), hidden = True) # Used for roles where it is relatively simple to get the character to quit their job.
        critical_job_role = Role("Critical Job", [], hidden = True) # Used for role where it is impossible to get the character to quit their job, but they don't have anything else going on.
        stripper_role = Role("Stripper", get_stripper_role_actions(), hidden = True)

        prostitute_role = Role("Prostitute", get_prostitute_role_actions(), hidden = True)
        pregnant_role = Role("Pregnant", [], hidden = True)
        lactating_serum_role = Role("Lactating Serum", get_lactating_serum_role_actions(), hidden = True, on_turn = lactating_serum_on_turn, on_day = lactating_serum_on_day)

        city_rep_role = Role("City Representative", get_city_rep_role_actions(), role_trainables = get_city_rep_role_trainables())
    return
