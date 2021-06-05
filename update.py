import csv
import requests
import datetime
from datetime import date

# fileLocation = "/home/ubuntu/chore-bot/chores.csv"
# fileLocation = 'chores.csv'

# fileLocation = "/home/ubuntu/chore-bot/summer_data.csv"
fileLocation = 'summer_data.csv'

def log(msg):
    print(f"{str(datetime.datetime.now())}: {msg}")


test_bot = "7708f26577f448fd1271f9727d"
production_bot = "7708f26577f448fd1271f9727d"
# production_bot = "b623f516a520ffc3ca3a5aedec"


def sendGroupMeMessage(msg, bot):
    url = 'https://api.groupme.com/v3/bots/post'
    # TEST!!
    obj = {"text": msg, "bot_id": bot}
    # obj = {"text": msg, "bot_id": test_bot}
    x = requests.post(url, json=obj)


def getRandomBibleVerse():
    log("Getting bible verse")
    bibleUrl = 'http://labs.bible.org/api/?passage=random'
    obj = requests.get(bibleUrl)
    log("Got bible verse")

    js = obj.content.decode('utf-8')
    startIdx = js.index("<b>") + 3
    endIdx = js.index("</b>")
    verseStart = endIdx + 5

    content = js[startIdx:endIdx] + "\n"
    content += js[verseStart:len(js) - 1]
    return content


log("Starting run")

# Send alive message every time it runs
sendGroupMeMessage("@Coleman Jenkins Program ran", test_bot)
log("Sent test message")

# Remind on Saturday
if datetime.datetime.today().weekday() == 5:  # 5
    content = "Remember to do your chores this weekend!\n\n"
    content += getRandomBibleVerse()
    sendGroupMeMessage(content, production_bot)
    log("Sent chore reminder")

# Remind on Friday
if datetime.datetime.today().weekday() == 4:  # 4
    content = "Remember to settle up on Splitwise if you aren't already!\n\n"
    content += getRandomBibleVerse()
    sendGroupMeMessage(content, production_bot)
    log("Send Splitwise reminder")


# Send chores on Monday
if datetime.datetime.today().weekday() == 0:  # 0
    log("Sending chores...")

    log("Reading csv")
    names = {"Coleman", "Hudson", "Peter",
             "Noah", "Phil", "Danny P", "Michael", "Extra"}
    content = ""
    with open(fileLocation) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        headers = []
        for row in reader:
            if line_count == 0:
                headers = row
            else:
                if row[0]:
                    day = row[0] + " 2021"
                    if datetime.datetime.strptime(day, '%b %d %Y').date() == date.today():
                        for i in range(len(row)):
                            if i != 0:
                                if headers[i] in names:
                                    content += headers[i] + \
                                        "'s chore: " + row[i] + "\n"
            line_count += 1
    content += "\nFor the summer, if someone's not there, other people just do it!"
    content += "\nLike the message if you did your chore.\nHonor the Lord with your life and find joy in Him this week :)\n - Your favorite bot\n\n"
    content += getRandomBibleVerse()
    sendGroupMeMessage(content, production_bot)
    log("Message sent!")

log("Done!")
print()
