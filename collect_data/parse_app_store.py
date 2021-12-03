import re
import requests
import lxml.html
from utils.process_lang import preprocess_text

def get_class_html(text, class_name="section__description"):
    html = lxml.html.fromstring(text)
    a = html.find_class(class_name)
    v = a[0].text_content()
    return preprocess_text(v)


def game_in_app(link):
    r = requests.get("https://" + link)
    text = r.text
    dict_data_game = {
        "number_votes": float(re.findall(r'(?<=Оценок:)(.*)(?=\.)', text)[0].split(",")[0]) if len(
            re.findall(r'(?<=Оценок:)(.*)(?=\.)', text)) > 0 else 0,
        "rank": float(
            re.findall(r'(?<="we-rating-count star-rating__count">)(.*)(?= • О)', text)[0].replace(",", ".")) if len(
            re.findall(r'(?<="we-rating-count star-rating__count">)(.*)(?= • О)', text)) > 0 else 0,
        "text": get_class_html(text)
    }
    return dict_data_game


def appstore_com(word="fugo"):
    url_russia = "https://www.apple.com/ru/search/" + word + "?src=serp"
    r = requests.get(url_russia)
    text = r.text
    res=[]
    links_game = []
    for elem in re.findall(r'(?<=<a href=\"https:\/\/)(.*id.*)(?=")', text)[:5]:
        links_game.append(elem)
        res.append(game_in_app(elem))
    return res

if __name__ == "__main__":
    print(appstore_com())
