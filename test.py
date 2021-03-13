import requests

bot = "7708f26577f448fd1271f9727d"
url = 'https://api.groupme.com/v3/bots/post'
# TEST!!
# obj = {"text": msg, "bot_id": bot}
obj = {"text": "Hello", "bot_id": "7708f26577f448fd1271f9727d"}
print(bot)
# obj = {"text": msg, "bot_id": test_bot}
x = requests.post(url, json=obj)
print(x)

