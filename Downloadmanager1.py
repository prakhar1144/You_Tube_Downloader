import requests
import validators
import os
import re
from requests.exceptions import RequestException

path = "C:/Users/Prakhar Pratyush/Desktop"

for i in range(1, 50):
    URL = str(input("Enter the URL"))

    valid = validators.url(URL)
    if valid == True:
        print("Searching...")
        break
    else:
        print("Invalid URL")
        continue

receive = requests.get(URL, stream ="true")
try:
    fname = ''
    if "Content-Disposition" in receive.headers.keys():
        fname = re.findall(("filename=(.+)", receive.headers["Content-Disposition"]))[0]
    else:
        fname = URL.split("/")[-1]
    file = fname
    with open(os.path.join(path, file), 'wb') as dm:
        # dm.write(receive.content) for pdf
        for chunk in receive.iter_content(chunk_size=1024):
            dm.write(chunk)

except RequestException as e:
    print(e)


print(receive.status_code)
print(receive.headers)

