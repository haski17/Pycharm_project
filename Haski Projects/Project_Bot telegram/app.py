import requests


API_Link="https://api.telegram.org/bot5659184782:AAHIdoBtMibTET6IpRQSRyu1djG5MzP5BYw"

updates= requests.get(API_Link + "/getUpdates?offset=-1").json()

print(updates)

message= updates["result"][0]["message"]

chat_id= message["from"]["id"]
text= message["text"]

sent_message= requests.get(API_Link + f"/sendMessage?chat_id={chat_id}]&text=Привет ты написал{text}")