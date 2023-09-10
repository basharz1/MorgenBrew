from tuya_iot.tuya_enums import AuthType
from requests import get
import datetime
import time
from tuya_iot import (
    TuyaOpenAPI,
    AuthType,
)
from env import (ACCESS_ID, ACCESS_KEY, USERNAME, PASSWORD, ENDPOINT, FINGERBOT_DEVICE_ID)

# Connect to Tuya API and login
openapi = TuyaOpenAPI(endpoint=ENDPOINT, access_id=ACCESS_ID, access_secret=ACCESS_KEY, auth_type=AuthType.CUSTOM)
result = openapi.connect(username=USERNAME, password=PASSWORD)

print("device test-> ", openapi.token_info)
commands = {'commands': [{'code':'switch', 'value':True}]}

UserInput = input("Please type when do you like your coffee ready every morning (Use HH:MM 24-hours format): ")


while(len(UserInput) != 5 or not UserInput[:2].isnumeric() or not UserInput[3:].isnumeric() or UserInput[2] != ':' or int(UserInput[:2]) < 0 or int(UserInput[:2]) >23 or int(UserInput[3:]) < 0 or int(UserInput[3:]) >59):

    UserInput = input("Incorrect input! Please type in the following format: (HH:MM 24-hours format)")

hour = int(UserInput[:2])
min = int(UserInput[3:])

print(f"Your coffee will be ready at {UserInput}!")
print("Press Ctrl + C to stop")

while(True):
    now = datetime.datetime.now()
    if now.hour ==hour and now.minute ==min and now.second == 50: #now.hour == 16 and now.minute == 53 and now.second ==30 :

        result = openapi.post(f"/v1.0/iot-03/devices/{FINGERBOT_DEVICE_ID}/commands",commands)
        print(result)
        time.sleep(1)