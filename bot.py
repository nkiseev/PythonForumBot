import requests
from forum_parser import get_content
from db_manager import DbManager

API_KEY = '<bot_api_key>'

URL = 'https://api.telegram.org/bot{BOT_API_KEY}/sendMessage?chat_id={CHANNEL_NAME}&text={MESSAGE_TEXT}'

CHANNEL_NAME = '<channel_name>'

MSG_TEMPLATE = '''На форуме новый вопрос: "{title}"
Опубликуйте ответ тут: {link}'''

if __name__ == '__main__':
    print('Start')
    posts = get_content()
    if len(posts) == 0:
        exit(0)

    db = DbManager('test.db')
    db.connect()
    for post in posts:
        title = post['title']
        link = post['link']
        result = db.find_post(title)

        if len(result) == 0:
            db.add_new_post(title, link)
            msg = MSG_TEMPLATE.format(title=title, link=link)
            url = URL.format(
                BOT_API_KEY=API_KEY,
                CHANNEL_NAME=CHANNEL_NAME,
                MESSAGE_TEXT=msg
            )

            resp = requests.post(url)

    db.close()
    print('Stop')
