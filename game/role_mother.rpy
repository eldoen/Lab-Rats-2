﻿init -2 python:
    #MOM ACTION REQUIREMENTS
    def mom_weekly_pay_requirement(the_person):
        if time_of_day == 4 and day%7 == 4: #It is the end of the day on friday
            return True
        return False

    def mom_offer_make_dinner_requirement(the_person):
        if time_of_day == 3:
            return True
        return False

### MOM ACTION LABELS ###

label mom_weekly_pay_label(the_person):

    #todo: at some point demand to take over the house, adds extra "house rules" options
    $ bedroom.show_background()
    "You're getting ready for bed when [the_person.possessive_title] calls from downstairs."
    the_person.char "[the_person.mc_title], could we talk for a moment?"
    mc.name "Sure, down in a second."
    $ kitchen.show_background()
    $ the_person.draw_person(position = "sitting")
    "[the_person.title] is sitting at the kitchen table, a collection of bills laid out in front of her."

    if the_person.sluttiness < 20:
        the_person.char "This new morgage on the house is really stressing our finances. It would really help if you could chip in."
        call mom_low_sluttiness_weekly_pay(the_person) from _call_mom_low_sluttiness_weekly_pay #The menu is separated out to make looping easier.
    else:
        if mc.business.event_triggers_dict.get("Mom_Payment_Level",0) >= 1: #We've been through this song and dance already.
            the_person.char "The budget is still really tight [the_person.mc_title], so I was wondering if you wanted to buy any sort of favour from me?"

        else:
            the_person.char "Our budget is really stretched thin right now, and it would be a huge relief if you could help out."
            the_person.char "I wouldn't feel right about just taking your hard earned money though, so I was hoping we could make a deal..."
            mc.name "What sort of deal Mom?"
            the_person.char "Remember last summer, and you paid me for some... personal favours?"
            "She blushes and looks away for a second before regaining her composure."
            the_person.char "Maybe we could start doing that again... I know I shouldn't even bring it up."
            mc.name "No Mom, you're doing it for the good of the family, right? I think it's a great idea."
            $ the_person.change_slut_temp(2)
            $ the_person.change_happiness(5)
            $ the_person.change_love(2)
            the_person.char "Of course, it's the best thing for all of us. What would you like to do?"
            $ mc.business.event_triggers_dict["Mom_Payment_Level"] = 1
        call mom_high_sluttiness_weekly_pay(the_person) from _call_mom_high_sluttiness_weekly_pay


    $ mom_weekly_pay_action = Action("mom weekly pay", mom_weekly_pay_requirement, "mom_weekly_pay_label", args=mom, requirement_args =[mom]) # Reload the event for next week.
    $ mc.business.mandatory_crises_list.append(mom_weekly_pay_action)
    return

label mom_low_sluttiness_weekly_pay(the_person):
    menu:
        "Give her nothing.":
            mc.name "Sorry Mom, I'm just not turning a profit right now. Hopefully we will be soon though. I'll help out as soon as I can."
            $ the_person.change_happiness(-5)
            $ the_person.change_love(-1)
            $ the_person.draw_person(position = "sitting", emotion = "sad")
            the_person.char "Okay sweetheart, I understand. I'll talk with Lily and let her know that we have to cut back on non essentials."

        "Help out.\n{size=22}-$100{/size}" if mc.business.funds >= 100:
            "You pull out your wallet and count out some cash, but hesitate before you hand it over."
            $ mc.business.funds += -100
            menu:
                "Ask for a kiss.":
                    mc.name "I'd like a kiss for it though."
                    the_person.char "A kiss?"
                    mc.name "For being such a good son."
                    the_person.char "Oh, well that's easy then."
                    "She stands up and leans in to give you a kiss on the cheek."
                    mc.name "On the lips, [the_person.mc_title]. Please?"
                    the_person.char "You've always been so affectionate. Not like other boys at all, you know. Fine."
                    "She leans forward and pecks you on the lips."
                    $ the_person.change_slut_temp(2)
                    the_person.char "There, have I earned my reward?"
                    "You hold out the cash for her and she takes it."
                    the_person.char "Thank you so much, every little bit helps."

                "Make her say please.":
                    mc.name "What are the magic words?"
                    the_person.char "Abracadabra?"
                    mc.name "No, the words we say when we want help?"
                    the_person.char "Oooh, I see what you're getting at. I've drilled it into you and I'm getting a taste of my own medicine."
                    the_person.char "May I please have some help with the bills?"
                    mc.name "I'm not sure if you mean it..."
                    the_person.char "Pretty please?"
                    $ the_person.change_obedience(2)
                    "You hold out the cash and she takes it."
                    mc.name "And..."
                    the_person.char "Thank you [the_person.mc_title], you're very kind."
            $ the_person.change_happiness(5)
            $ the_person.change_love(3)
            $ the_person.draw_person(position = "sitting", emotion = "happy")
            "She gives you a hug and turns her attention back to the bills."

        "Help out.\n{size=22}-$100{/size} (disabled)" if mc.business.funds < 100:
            pass
    return

label mom_high_sluttiness_weekly_pay(the_person):
    menu:
        "Have her strip for you. -$100" if mc.business.funds >= 100:
            if mc.business.event_triggers_dict.get("Mom_Strip",0) >= 1:
                mc.name "I want you to show off yourself off to me, how does that sound?"
                the_person.char "Fair is fair, but I'll need a little extra if you want to see anything... inappropriate."
                $ mc.business.funds += -100
                "You hand over the cash and sit back while [the_person.possessive_title] entertains you."
            else:
                $ mc.business.event_triggers_dict["Mom_Strip"] = 1
                mc.name "I'd like to see a little more of you Mom, how about I pay you to give me a little strip tease."
                the_person.char "Oh my god, I've raised such a dirty boy. How about I pose for you a bit, and if you want to see more you can contribute a little extra."
                mc.name "Sounds like a good deal Mom."
                $ mc.business.funds += -100
                "You hand over the cash and sit back while [the_person.possessive_title] entertains you."

            call pay_strip_scene(the_person) from _call_pay_strip_scene_2

        "Have her strip for you. -$100 (disabled)" if mc.business.funds <100:
            pass

        "Have her test some serum. -$100" if mc.business.funds >= 100:
            if mc.business.event_triggers_dict.get("Mom_Serum_Test",0) >= 1:
                mc.name "I've got some more serum I'd like you to test Mom."
                call give_serum(the_person) from _call_give_serum_10
                if _return:
                    $ mc.business.funds += -100
                    "You hand the serum to [the_person.possessive_title], followed by the cash."
                    the_person.char "Okay, so that's all for now?"
                    mc.name "That's all. I'll just be keeping an eye on you in the future, but you don't need to worry about that."
                    the_person.char "Well thank you sweetheart, this money will really make a difference. I'm so proud of you!"
                else:
                    mc.name "Actually, I don't have anything right now. Maybe next wek though, okay?"
                    the_person.char "Okay sweetheart, thanks for at least thinking about it."
            else:
                $ mc.business.event_triggers_dict["Mom_Serum_Test"] = 1
                mc.name "I have something you could help me with Mom."
                the_person.char "What is it sweetheart? I'll do whatever I can for you."
                mc.name "We have a little bit of a research bottleneck at work. I have something I'd like you to test for me."
                the_person.char "Oh, okay. If it helps I can be your for hire test subject!"
                mc.name "Excellent, let me just see if I have anything with me right now..."
                call give_serum(the_person) from _call_give_serum_11
                if _return:
                    $ mc.business.funds += -100
                    "You hand the serum to [the_person.possessive_title], followed by the cash."
                    the_person.char "Okay, so that's all for now?"
                    mc.name "That's all. I'll just be keeping an eye on you in the future, but you don't need to worry about that."
                    the_person.char "Well thank you sweetheart, this money will really make a difference. I'm so proud of you!"
                else:
                    mc.name "Actually, I don't have anything right now. Maybe next wek though, okay?"
                    the_person.char "Okay sweetheart, thanks for at least thinking about it."

        # "I want to make some changes around here." if the_person.obedience >= 120:
        #     #TODO: Requires obedience, but unlocks a bunch of other options, like having your Mom bring you breakfast every morning, not wearing anything at home, etc.
        #     #TODO TODO TODO
        #     mc.name "Now that I'm the man of the house, I want to make some changes around the house."
        #     the_person.char "What sorts of changes?"
        #     call mom_make_house_changes(the_person)
        #
        # "I want to make some changes around here.\nRequires: 120 Obedience (disabled)" if the_person.obedience < 120:
        #     pass

        "Have her suck you off. -$300" if mc.business.funds >= 300 and the_person.sluttiness >= 30:
            mc.name "Alright, I'll pay you to give me a blowjob."
            if the_person.sex_record.get("Blowjobs",0) > 0 or the_person.sluttiness >= 60:
                the_person.char "If that's what you need."
                "You pull out your wallet and count out her cash while [the_person.possessive_title] gets onto her knees in front of you."
                $ the_person.draw_person(position = "blowjob")
                the_person.char "Remember, not a word to anyone else though. Okay>"
                mc.name "Of course, this is just between you and me."

            else:
                the_person.char "What? I mean... I could never do that! How could you even say that?"
                "You pull out your wallet and count out the cash while you talk."
                mc.name "Sure you could. It's just me and you here, nobody would ever need to know."
                mc.name "Besides, it's for the family, right? This is just another way to help everyone out. Myself included, I've been real stressed at work lately."
                $ mc.business.funds += -300
                "You lay the cash down on the table. [the_person.possessive_title] hesitates, then meekly reaches for the money."
                the_person.char "Not a word to anyone, or I'll kick you out of the house."
                mc.name "Of course [the_person.title], don't you trust your own son?"
                $ the_person.draw_person(position = "blowjob")
                "She sighs and kneels down in front of you. You unzip your pants and pull your cock out for your mother."
                mc.name "Don't worry, it won't bite."
                the_person.char "This isn't my exactly my first blowjob sweety, I'm not worried."

            "With that she opens her mouth and slides the tip of your hard cock inside. Her tongue swirls around the tip, sending a jolt of pleasure up your spine."
            call fuck_person(the_person, private = True, start_position = blowjob, skip_intro = True, position_locked = True) from _call_fuck_person_33
            if the_person.arousal >= 100:
                "You pull up your pants while [the_person.possessive_title] is on her knees panting, trying to get her breath back."
                mc.name "I didn't know you were going to enjoy that so much. Maybe you should be paying me next time."
                the_person.char "Ah... I hope we can come to some sort of deal... Ah... In the future..."
            else:
                "You pull your pants up while [the_person.possessive_title] gets off of her knees and cleans herself up."
            $ the_person.reset_arousal()
            $ the_person.review_outfit()
            $ the_person.change_obedience(4)

        "Have her suck you off. -$300 (disabled)" if mc.business.funds < 300 and the_person.sluttiness >= 30:
            pass

        "Nothing this week.":
            mc.name "Sorry Mom, but I'm tight on cash right now as well. Maybe next week, okay?"
            "[the_person.possessive_title] nods and turns back to her bills."
            the_person.char "I understand sweetheart. Now don't let me keep you, I'm sure you were up to something important."
            pass

        #TODO: pay her to fuck you.
        #TODO: pay her to change her wardrobe
        #TODO: pay her to do somehting with Lily.
        #TODO: have Lily start a cam show to make cash, then bring your Mom into it.



    return

# label mom_make_house_changes(the_person):
#     # A list of house rules to put into place.
#     menu:
#         "TODOTODOTODO":
#             #TODO: Decide what sort of house wide changes the player is able to make.
#             pass
#
#         "Never mind.":
#             call mom_high_sluttiness_weekly_pay(the_person) #Go back and pick something else.
#     return

label mom_offer_make_dinner_label(the_person):
    #TODO you offer to make dinner. It takes up time, but you can slip serum to your mom and sister.
    mc.name "You've been working yourself so hard lately Mom, how about you let me make dinner tonight?"
    the_person.char "Oh [the_person.mc_title], that's such a sweet thing for you to offer!"
    $ the_person.change_happiness(5)
    $ the_person.change_obedience(-1)
    $ the_person.change_love(2)
    "[the_person.possessive_title] gives you a hug."
    the_person.char "Do you know where everything is?"
    mc.name "Yeah, I think I can take care of it."
    the_person.char "Well thank you, you're always such a help around here!"
    $ renpy.scene("Active")
    $ kitchen.show_background()
    "You head to the kitchen and get to work. The cooking isn't hard, but it takes up most of your evening."
    "As you're plating out dinner you have a perfect opportunity to give your mother or sister some serum in secret."
    menu:
        "Add serum to Mom's food.":
            call give_serum(mom) from _call_give_serum_8

        "Leave Mom's food alone.":
            pass

    menu:
        "Add serum to [lily.name]'s food.":
            call give_serum(lily) from _call_give_serum_9

        "Leave [lily.name]'s food alone.":
            pass

    "You bring the food out and have a nice family dinner together."
    call advance_time from _call_advance_time_10
    return
