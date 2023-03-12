import os, requests

SHEETY_FLIGHT_DEALS_ENDPOINT = os.environ["SHEETY_FLIGHT_DEALS_ENDPOINT"]
USERS_ENDPOINT = f"{SHEETY_FLIGHT_DEALS_ENDPOINT}/users"

print("Welcome to Azad's Flight Club\nWe find the best flight deals and email you.")
first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
email = input("What is your email?\n")

validate_email = True
while validate_email:
    again_email = input("Type your email again.\n")
    if email == again_email:
        validate_email = False
        user_data = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email,
            }
        }
        response = requests.post(
            url=USERS_ENDPOINT,
            json=user_data,
        )
        print("Success! Your email has been added.")
    else:
        print("Invalid email entered")

print("You're in the club!")
