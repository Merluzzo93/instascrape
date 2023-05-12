import csv
import requests
from bs4 import BeautifulSoup

instagram_links = [
    "https://www.instagram.com/beatnicstore/",
    "https://www.instagram.com/cicointhewoods/",
    "https://www.instagram.com/stellavizzino/"
]

with open("instagram_bios.csv", mode="w", encoding="utf-8") as csv_file:
    fieldnames = ["Username", "Bio"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    for link in instagram_links:
        page = requests.get(link)
        soup = BeautifulSoup(page.content, "html.parser")
        username_tag = soup.select_one(".rhpdm")
        bio_tag = soup.select_one("h1.-vDIg")

        if username_tag is not None and bio_tag is not None:
            username = username_tag.text.strip()
            bio = bio_tag.text.strip().replace("\n", " ")
        else:
            username = "Username not found"
            bio = "Bio not found"

        writer.writerow({"Username": username, "Bio": bio})

print("Instagram bios scraped and exported to CSV file successfully!")
