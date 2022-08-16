import os
from dotenv import load_dotenv
load_dotenv()

### bots ###
print(os.environ.get('MODE'))
if os.environ.get('MODE') == 'PRODUCTION':
    test_bot = os.environ.get('BOT_TEST')
    chores_bot = os.environ.get('STUB_CHORES')
    reminders_bot = os.environ.get('STUB_HUB')
else:
    test_bot = os.environ.get('BOT_TEST')
    reminders_bot = os.environ.get('BOT_TEST')
    chores_bot = os.environ.get('BOT_TEST')

### files ###
if os.environ.get('SERVER') == 'PRODUCTION':
    fileLocation = "/home/ubuntu/chore-bot/chores.csv"
else:
    fileLocation = 'chores.csv'

### people in csv ###
names = {"Coleman", "Hudson", "Noah",
            "Peter", "Michael", "Wesley", "Luke"}
