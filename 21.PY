


def check_driving_age():
    age = int(input("21: "))
    
    if age >= 18:
        print("You are old enough to drive.")
    else:
        years_to_wait = 18 - age
        print(f"Sorry, you are not old enough to drive. Please wait {years_to_wait} more {'year' if years_to_wait == 1 else 'years'}.")
