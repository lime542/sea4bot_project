import telebot
from telebot import types
from bs4 import BeautifulSoup
import requests
import urllib.parse

token = 'апи'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, 'Привет! Это первый поисковик в телеграм. Я использую библиотеку bs4 чтобы парсить поисковик DuckDuckGo, и выдавать первые 10 ссылок. Я работаю в inline режиме. Чтобы пользоваться мной, просто введи в любом чате мой ник, и запрос. Например:"@sea4bot что такое duckduckgo"')

@bot.inline_handler(lambda query: query.query != None)
def query_text(query):
    try:
        global html
        global clean_url
        global durty_header
        global clean_header
        durty_header = []
        clean_header = []
        clean_url = []
        global lll
        global titled
        lll = []
        titled = []
        search_resp = query.query
        search_resp = urllib.parse.quote(search_resp)
        html = get_html(search_resp)
        parsing_url(html)
        clear()
        title(html)
        clear_title()

        header(html)
        clear_headers()
        icon = 'https://www.cultofmac.com/wp-content/uploads/2019/02/Image-05-02-2019-11-03-780x624@2x.jpeg'
        sea1 = types.InlineQueryResultArticle(id='1', title=clean_header[0], input_message_content=types.InputTextMessageContent(message_text=clean_url[0] + '\n' + titled[0]), description=titled[0], thumb_url=icon, thumb_width=48, thumb_height=48)
        sea2 = types.InlineQueryResultArticle(id='2', title=clean_header[1], input_message_content=types.InputTextMessageContent(message_text=clean_url[1] + '\n' + titled[1]), description=titled[1], thumb_url=icon, thumb_width=48, thumb_height=48)
        sea3 = types.InlineQueryResultArticle(id='3', title=clean_header[2], input_message_content=types.InputTextMessageContent(message_text=clean_url[2] + '\n' + titled[2]), description=titled[2], thumb_url=icon, thumb_width=48, thumb_height=48)
        sea4 = types.InlineQueryResultArticle(id='4', title=clean_header[3], input_message_content=types.InputTextMessageContent(message_text=clean_url[3] + '\n' + titled[3]), description=titled[3], thumb_url=icon, thumb_width=48, thumb_height=48)
        sea5 = types.InlineQueryResultArticle(id='5', title=clean_header[4], input_message_content=types.InputTextMessageContent(message_text=clean_url[4] + '\n' + titled[4]), description=titled[4], thumb_url=icon, thumb_width=48, thumb_height=48)
        sea6 = types.InlineQueryResultArticle(id='6', title=clean_header[5], input_message_content=types.InputTextMessageContent(message_text=clean_url[5] + '\n' + titled[5]), description=titled[5], thumb_url=icon, thumb_width=48, thumb_height=48)
        sea7 = types.InlineQueryResultArticle(id='7', title=clean_header[6], input_message_content=types.InputTextMessageContent(message_text=clean_url[6] + '\n' + titled[6]), description=titled[6], thumb_url=icon, thumb_width=48, thumb_height=48)
        sea8 = types.InlineQueryResultArticle(id='8', title=clean_header[7], input_message_content=types.InputTextMessageContent(message_text=clean_url[7] + '\n' + titled[7]), description=titled[7], thumb_url=icon, thumb_width=48, thumb_height=48)
        sea9 = types.InlineQueryResultArticle(id='9', title=clean_header[8], input_message_content=types.InputTextMessageContent(message_text=clean_url[8] + '\n' + titled[8]), description=titled[8], thumb_url=icon, thumb_width=48, thumb_height=48)
        sea10 = types.InlineQueryResultArticle(id='10', title=clean_header[9], input_message_content=types.InputTextMessageContent(message_text=clean_url[9] + '\n' + titled[9]), description=titled[9], thumb_url=icon, thumb_width=48, thumb_height=48)
        bot.answer_inline_query(inline_query_id = query.id, results = [sea1, sea2, sea3, sea4, sea5, sea6, sea7, sea8, sea9, sea10])
        clean_url = []
        titled = []
        lll = []
        durty_header = []
        clean_header = []
        clean_ico = []
    except Exception as e:
        error_result = types.InlineQueryResultArticle(id='1', title='uncorrect results', input_message_content=types.InputTextMessageContent(message_text='uncorrect results!'))
        bot.answer_inline_query(inline_query_id = query.id, results = [error_result])
        clean_url = []
        titled = []
        lll = []
        durty_header = []
        clean_header = []
        clean_ico = []
#получаю html страничку сайта
def get_html(search_resp):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"}
    full_url = "https://html.duckduckgo.com/html/?q=" + search_resp + '&kp=-1&kl=ru-ru'
    result = requests.post(full_url, headers=headers)
    return result.text
#парсим ссылки
def parsing_url(html):
    soup = BeautifulSoup(html, 'html.parser')
    for a in soup.find_all('a', href=True, class_='result__url'): 
        if a.text:
            clean_url.append(a['href'])
#парсим титлы
def title(html):
    soup = BeautifulSoup(html, 'lxml')
    lll = soup.findAll('a', class_='result__snippet')
    for i in range(len(lll)):
        titled.append(lll[i].text)
#убираем ненужные титлы, оставляем только первые 10
def clear_title():
    global titled
    titled.append("nothing found")
    titled.append("nothing found")
    titled.append("nothing found")
    titled.append("nothing found")
    titled.append("nothing found")
    titled.append("nothing found")
    titled.append("nothing found")
    titled.append("nothing found")
    titled.append("nothing found")
    titled.append("nothing found")
    size_list = len(titled)
    if size_list == 10:
        pass
    elif size_list > 10:
        titled = titled[:10]
    elif size_list < 10:
        pass
    else:
        pass

#убираем ненужные ссылки, оставляем только первые 10
def clear():
    global clean_url
    clean_url.append("nothing found")
    clean_url.append("nothing found")
    clean_url.append("nothing found")
    clean_url.append("nothing found")
    clean_url.append("nothing found")
    clean_url.append("nothing found")
    clean_url.append("nothing found")
    clean_url.append("nothing found")
    clean_url.append("nothing found")
    clean_url.append("nothing found")
    size_list = len(clean_url)
    if size_list == 10:
        pass
    elif size_list > 10:
        clean_url = clean_url[:10]
    elif size_list < 10:
        pass
    else:
        pass
#парсим заголовки
def header(html):
    soup = BeautifulSoup(html, 'lxml')
    durty_header = soup.findAll('a', class_='result__a')
    for i in range(len(durty_header)):
        clean_header.append(durty_header[i].text)
#убираем ненужные заголовки, оставляем только первые 10
def clear_headers():
    global clean_header
    clean_header.append("nothing found")
    clean_header.append("nothing found")
    clean_header.append("nothing found")
    clean_header.append("nothing found")
    clean_header.append("nothing found")
    clean_header.append("nothing found")
    clean_header.append("nothing found")
    clean_header.append("nothing found")
    clean_header.append("nothing found")
    clean_header.append("nothing found")
    size_list = len(clean_header)
    if size_list == 10:
        pass
    elif size_list > 10:
        clean_header = clean_header[:10]
    elif size_list < 10:
        pass
    else:
        pass
if __name__ == '__main__':
    bot.polling(none_stop=True)