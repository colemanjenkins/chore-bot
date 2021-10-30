import os
from dotenv import load_dotenv
load_dotenv()

### bots ###
print(os.environ.get('MODE'))
if os.environ.get('MODE') == 'PRODUCTION':
    test_bot = "7708f26577f448fd1271f9727d"
    chores_bot = "9405772b208b778b444749aa58"
    reminders_bot = "b623f516a520ffc3ca3a5aedec"
else:
    test_bot = "7708f26577f448fd1271f9727d"
    reminders_bot = test_bot
    chores_bot = test_bot





### files ###
if os.environ.get('SERVER') == 'PRODUCTION':
    fileLocation = "/home/ubuntu/chore-bot/chores.csv"
else:
    fileLocation = 'chores.csv'

### people in csv ###
names = {"Coleman", "Hudson", "Peter",
            "Noah", "Phil", "David", "Michael", "Wesley"}
