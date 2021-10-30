import csv
import requests
import datetime
from datetime import date

from defines import *


def log(msg):
    print(f"{str(datetime.datetime.now())}: {msg}")

def sendGroupMeMessage(msg, bot):
    url = 'https://api.groupme.com/v3/bots/post'
    obj = {"text": msg, "bot_id": bot}
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
sendGroupMeMessage("Program ran", test_bot)
log("Sent test message")

# Remind on Saturday
if datetime.datetime.today().weekday() == 5:  # 5
    content = "Remember to do your chores this weekend!"
    sendGroupMeMessage(content, reminders_bot)
    log("Sent chore reminder")

# Remind on Friday
if datetime.datetime.today().weekday() == 4:  # 4
    content = "Remember to settle up on Splitwise if you aren't already!"
    content += "\n-> Like this if you're settled up <-"
    # content = "Remember to settle up on Splitwise if you aren't already!\n\n"
    # content += getRandomBibleVerse()
    sendGroupMeMessage(content, reminders_bot)
    log("Send Splitwise reminder")


# Send chores when the dates in the first column are the given day
# if datetime.datetime.today().weekday() == 0:  # 0
send_chore_details = False
log("Parsing chores csv")

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
                day = row[0] + " " + str(date.today().year)
                if datetime.datetime.strptime(day, '%b %d %Y').date() == date.today():
                    send_chore_details = True
                    for i in range(len(row)):
                        if i != 0:
                            if headers[i] in names:
                                content += headers[i] + \
                                    "'s chore: " + row[i] + "\n"
        line_count += 1

if send_chore_details:
    log("Sending chores message")
    content += "\nSend a picture and like the message if you did your chore!"
    sendGroupMeMessage(content, chores_bot)
    log("Message sent!")
    log("Sending encouragement")
    msg = "Honor the Lord with your life and find joy in Him this week :)\n"
    msg += "Love you guys.\n\n"
    msg += getRandomBibleVerse()
    sendGroupMeMessage(msg, chores_bot)
    log("Encouragement sent!")

log("Done!")
print()
