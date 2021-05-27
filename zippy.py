import random
import requests
import string
import bs4

def randomLink():
    letters = string.ascii_letters + string.digits
    return ( ''.join(random.choice(letters) for i in range(9)) )

while True:
    link = f"https://www1.zippyshare.com/v/{randomLink()}/file.html"
    request = requests.get(link)
    if "File does not exist on this server" not in request.text:
        print(link)
    print("Working..")