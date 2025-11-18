from datetime import datetime


def generate_profile(age):
    if age < 13:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    else:
        return "Adult"


current_datetime = datetime.now()
current_year = current_datetime.year

user_name = str(input("Hello, please enter your full name "))
birth_year_str = input("Please enter your birth year ")
birth_year = int(birth_year_str)
current_age = current_year - birth_year

hobbies = []

hobby = None

while hobby != "stop":
    hobby = str(input("Enter your favorite hobby or type 'stop' to finish: "))
    if hobby != "stop" and hobby != "":
        hobbies.append(hobby)

user_profile = {'name': user_name,
                'age': current_age,
                'stage': generate_profile(current_age),
                'hobbies': hobbies}

print(f'Profile Summary:\n'
      f'Name: {user_profile['name']}\n'
      f'Age: {user_profile['age']}\n'
      f'Life Stage: {user_profile['stage']}')
if hobbies:
    print(f'Favorite hobbies ({len(hobbies)}):')
    for i in hobbies:
        print(f'- {i}')
else:
    print(f"You didn't mention any hobbies.")
