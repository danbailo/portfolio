import json
import re

from bs4 import BeautifulSoup
import requests

PATH = "../docs/"

# Scrap pinned items from https://github.com/{user}


def get_pinned_items(path_to_save, url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    pinned_content = soup.find(
        "div", attrs={"class": "js-pinned-items-reorder-container"})
    pinned_items = pinned_content.find_all(
        "div", attrs={"class": "pinned-item-list-item-content"})

    data = {}

    for pinned_item in pinned_items:
        repo = pinned_item.find("a")
        link_repo = pinned_item.find("a").get("href")
        name_repo = repo.text
        description_repo = pinned_item.find("p").text
        predominant_lang = pinned_item.find(
            "span",
            attrs={"itemprop": "programmingLanguage"}).text

        # removing breaklines and whitesaces
        name_repo = re.sub(r"\n|\s{2,}", "", name_repo)
        link_repo = re.sub(r"\n|\s{2,}", "", link_repo)
        description_repo = re.sub(r"\n|\s{2,}", "", description_repo)
        predominant_lang = re.sub(r"\n|\s{2,}", "", predominant_lang)

        data[name_repo] = {
            "link_repo": link_repo,
            "description_repo": description_repo,
            "predominant_lang": predominant_lang}

    with open(path_to_save+"pinned_repos.json", "w") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


get_pinned_items(PATH, "https://github.com/danbailo")
