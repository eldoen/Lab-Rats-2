# init -1 python:
#     def get_appropriate_normal_job(the_person):
#
#         return #TODO: Look through the existing jobs and figure out which one the person should have.

label instantiate_jobs():
    $ list_of_jobs = [] # Random characters will be given a job from this list.
    python:
        unemployed_job = Job("Unemployed", unemployed_role, work_days = [], work_times = [])

        ## HR Jobs ##
        hr_job = Job("Personnel Manager", employee_role, job_location = mc.business.h_div, hire_function = setup_employee_stats,
            mandatory_duties = [hr_work_duty], available_duties = [] + general_duties_list + general_hr_duties)
        #TODO: Personal secretary job

        ## Market Jobs ##
        market_job = Job("Sales Representative",  employee_role, job_location = mc.business.m_div, hire_function = setup_employee_stats,
            mandatory_duties = [market_work_duty], available_duties = [] + general_duties_list + general_market_duties)


        ## R&D Jobs ##
        head_researcher_job = Job("Head Researcher", [employee_role, head_researcher], job_location = mc.business.r_div, hire_function = setup_employee_stats,
            mandatory_duties = [research_work_duty, head_researcher_duty], available_duties = [] + general_duties_list + general_rd_duties)
        rd_job = Job("R&D Scientist", employee_role, job_location = mc.business.r_div, hire_function = setup_employee_stats,
            seniority_level = 2, mandatory_duties = [research_work_duty], available_duties = [] + general_duties_list + general_rd_duties)


        ## Supply Jobs ##
        supply_job = Job("Logistics Manager", employee_role, job_location = mc.business.s_div, hire_function = setup_employee_stats,
            mandatory_duties = [supply_work_duty], available_duties = [] + general_duties_list + general_supply_duties)

        ## Production Jobs ##
        production_job = Job("Production Line Worker", employee_role, job_location = mc.business.p_div, hire_function = setup_employee_stats,
            mandatory_duties = [production_work_duty], available_duties = [] + general_duties_list + general_production_duties)

        # Jobs with existing effects #TODO Some of these should leave new roles (ex-stripper, etc.) when you hire someone.
        mom_associate_job = Job("Business Associate", mom_associate_role, job_location = mom_offices, work_times = [1,2], seniority_level = 2)
        mom_secretary_job = Job("Personal Secretary", mom_secretary_role, job_location = mom_offices, work_times = [1,2], seniority_level = 1)

        aunt_unemployed_job = Job("Unemployed", critical_job_role, work_days = [], work_times = [])

        influencer_job = Job("Influencer", critical_job_role, work_days = [], work_times = [])

        steph_lab_assistant = Job("Lab Assistant", critical_job_role, job_location = university) #Job for Steph to technically have at the start of the game so her job title is set correctly.
        nora_professor_job = Job("Professor", critical_job_role, job_location = university)

        alexia_barista_job = Job("Barista", critical_job_role, job_location = downtown)

        emily_student_job = Job("Tutee", student_role, job_location = university, work_times = [1,2])
        sister_student_job = Job("Student", sister_student_role, job_location = university, work_times = [1,2])
        student_job = Job("Student", generic_student_role, job_location = university, work_times = [1,2]) #Note that this is different from Emily's Student role, which is really a "tutee" role.

        city_rep_job = Job("City Administrator", city_rep_role, job_location = city_hall, work_days = [0,1,2,3,4,5], work_times = [1,2,3]) #ie. hide her in the private City Hall location for most of the time.

        stripper_job = Job("Stripper", stripper_role, job_location = strip_club, work_days = [0,1,2,3,4,5,6], work_times = [3,4], hire_function = stripper_hire, quit_function = stripper_replace)
        prostitute_job = Job("Prostitute", prostitute_role, job_location = downtown, work_days = [0,1,2,3,4,5,6], work_times = [3,4])

        # Random city roles, with no specific stuff related to them.
        secretary_job = Job("Secretary", unimportant_job_role, job_location = mom_office_lobby, work_days = [0,1,2,3,4], work_times = [1,2])

        barista_job = Job("Barista", unimportant_job_role, job_location = mall, work_days = [1,2,3,4,5], work_times = [1,2])

        clothing_cashier_job = Job("Cashier", unimportant_job_role, job_location = clothing_store, work_days = [0,1,2,3,4], work_times = [1,2])
        sex_cashier_job = Job("Cashier", unimportant_job_role, job_location = sex_store, work_days = [0,1,2,3,4], work_times = [1,2])
        electronics_cashier_job = Job("Cashier", unimportant_job_role, job_location = electronics_store, work_days = [0,1,2,3,4,5], work_times = [1,2])
        supply_cashier_job = Job("Cashier", unimportant_job_role, job_location = office_store, work_days = [0,1,2,3,4,5], work_times = [1,2])
        home_improvement_cashier_job = Job("Cashier", unimportant_job_role, job_location = home_store, work_days = [0,1,2,3,4,5], work_times = [1,2])

        nurse_job = Job("Nurse", unimportant_job_role, job_location = downtown, work_days = [0,1,2,3,4,5], work_times = [1,2])
        night_nurse_job = Job("Night Nurse", unimportant_job_role, job_location = downtown, work_days = [1,2,3,4,5,6], work_times = [3,4])
        gym_instructor_job = Job("Gym Instructor", unimportant_job_role, job_location = gym, work_days = [0,1,2,3,4], work_times = [1,2])
        office_worker_job = Job("Office Worker", unimportant_job_role, job_location = mom_office_lobby, work_days = [0,1,2,3,4], work_times = [1,2])


        list_of_jobs.append([unemployed_job, 30])
        list_of_jobs.append([secretary_job, 3])
        list_of_jobs.append([barista_job, 3])

        list_of_jobs.append([clothing_cashier_job, 3])
        list_of_jobs.append([sex_cashier_job, 3])
        list_of_jobs.append([electronics_cashier_job, 3])
        list_of_jobs.append([supply_cashier_job, 3])
        list_of_jobs.append([home_improvement_cashier_job, 3])

        list_of_jobs.append([nurse_job, 5])
        list_of_jobs.append([night_nurse_job, 5])
        list_of_jobs.append([gym_instructor_job, 3])
        list_of_jobs.append([office_worker_job, 5])


    return
