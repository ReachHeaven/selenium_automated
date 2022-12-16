import requests
from html2image import Html2Image
import re


def html_to_jpg():
    hti = Html2Image()
    hti.screenshot(
        html_file='results/report.html',
        css_file='results/assets/style.css',
        save_as='report.jpg'
    )


def bot_sendtext():
    html_to_jpg()
    bot_token = '5491281500:AAGSVWZoZZrAsPdv4JQ-eLzEAERtbOtK76k'
    chat_id = "-831945454"
    file = "report.jpg"
    html_page = "results/report.html"
    photo = {
        'photo': open(file, 'rb'),
    }

    with open("results/output.txt", 'r', encoding='utf-16') as f:
        string = f.read()
    pattern = re.compile(r"^tests.*", re.MULTILINE)
    result = re.findall(pattern, string)
    s = '\n'.join(result)
    print(s)

    message = ('https://api.telegram.org/bot' + bot_token + '/sendPhoto?chat_id='
               + chat_id + f'&caption=' + s)
    send = requests.post(message, files=photo)
