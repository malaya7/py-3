import time
from datetime import datetime as dt

hostTemp = "hosts"
hosts = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
webSitesList = ["www.facebook.com", "facebook.com",]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,18):
        with open(hostTemp,'r+') as file:
            content = file.read()
            print(content)
            for website in webSitesList:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website+"\n")
    else:
        with open(hostTemp,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in webSitesList):
                    file.write(line)
            file.truncate()
    time.sleep(5)
