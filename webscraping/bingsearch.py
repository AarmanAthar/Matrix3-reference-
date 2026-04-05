import requests
from bs4 import BeautifulSoup
import os
import json

query = "weakness"
url = f"https://www.bing.com/images/search?q={query}"

headers = {"User-Agent": "Mozilla/5.0"}
res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, "html.parser")

# 👇 IMPORTANT CHANGE
images = soup.find_all("a", class_="iusc")

os.makedirs("images", exist_ok=True)

count = 0
for img in images:
    try:
        m = json.loads(img["m"])
        img_url = m["murl"]   # 👈 FULL IMAGE URL

        img_data = requests.get(img_url).content
        with open(f"images/img_{count}.jpg", "wb") as f:
            f.write(img_data)

        print(f"Saved img_{count}.jpg")
        count += 1

    except Exception as e:
        pass

    if count == 5:
        break