import csv
import requests
import datetime
from datetime import date

if datetime.datetime.today().weekday() == 5:
    content = "Remember to do your chores this weekend!\n\nBe still, and know that I am God"
    url = 'https://api.groupme.com/v3/bots/post'
    obj = {"text" : content, "bot_id" : "b623f516a520ffc3ca3a5aedec"}
    x = requests.post(url, data = obj)
    exit()

if datetime.datetime.today().weekday() == 0:
    bibleUrl = 'http://labs.bible.org/api/?passage=random'
    obj = requests.get(bibleUrl)
    js = obj.content.decode('utf-8')

    startIdx = js.index("<b>") + 3
    endIdx = js.index("</b>")
    verseStart = endIdx + 5

    names = {"Coleman", "Hudson", "Peter", "Noah", "Phil", "Danny P", "Michael"}
    content = ""
    with open("chores.csv") as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        headers = []
        for row in reader:
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}')
                headers = row
                line_count += 1
            else:
                check = False
                for elem in row:
                    if elem == '':
                        check = True
                if check:
                    continue
                day = row[0] + " 2021"
                if datetime.datetime.strptime(day, '%b %d %Y').date() == date.today():
                    for i in range(len(row)):
                        if i != 0:
                            if headers[i] in names:
                                content += headers[i] + "'s chore: " + row[i] + "\n"
        # print(f'Processed {line_count} lines.')
    url = 'https://api.groupme.com/v3/bots/post'
    content += "Like the message if you did your chore!\n - Your favorite bot\n\n\n"
    content += js[startIdx:endIdx] + "\n"
    content += js[verseStart:len(js)  - 1]
    print(content)
    obj = {"text" : content, "bot_id" : "b623f516a520ffc3ca3a5aedec"}
    x = requests.post(url, data = obj)
    line_count += 1
