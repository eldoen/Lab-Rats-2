init 1 python:
    integration_test_labels.append("run_world_turn_integration_test")

label run_world_turn_integration_test():
    "Testing advancing time."
    call advance_time() from _call_advance_time_8
    "..."
    call advance_time() from _call_advance_time_34
    "..."
    call advance_time() from _call_advance_time_35
    "..."
    call advance_time() from _call_advance_time_36
    "..."
    call advance_time() from _call_advance_time_37

    menu:
        "Tests successful.":
            return True

        "Tests failed.":
            return False
