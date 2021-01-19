import csv
import requests

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
            if line_count == 1:
                for i in range(len(row)):
                    if i != 0:
                        if headers[i] in names:
                            content += headers[i] + "'s chore: " + row[i] + "\n"
            line_count += 1
    # print(f'Processed {line_count} lines.')

url = 'https://api.groupme.com/v3/bots/post'
content += "Like the message if you did your chore!\n - Your favorite bot"
print(content)
obj = {"text" : content, "bot_id" : "b623f516a520ffc3ca3a5aedec"}
x = requests.post(url, data = obj)