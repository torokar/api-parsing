#https://emojiguide.org/ru/%D0%B5%D0%B4%D0%B0-%D0%B8-%D0%BD%D0%B0%D0%BF%D0%B8%D1%82%D0%BA%D0%B8

from bs4 import BeautifulSoup as beautiful
from recepts.http_codes import connection_website

def parsing_emoji(soup):
    """Парсинг эмодзи"""
    grape = soup.find_all('i')
    grape_list = list(grape)
    emoji_list = []
    for i in range(len(grape_list)):
        el = str(grape_list[i])
        for j in range(len(el)):
            if el[j] != '<' and el[j] != 'i' and el[j] != '>' and el[j] != '/':
               emoji_list.append(el[j])
    return emoji_list

def parsing_text(soup, emoji):
    text = soup.find_all('p')
    text_list = list(text)
    emoji_text_dict = {}
    for i in range(len(text_list)):
        el = str(text_list[i])
        res = ""
        for j in range(len(el)):
            if el[j] != '<' and el[j] != 'p' and el[j] != '>' and el[j] != '/':
                res += el[j]

        emoji_text_dict[res] = emoji[i]
    return emoji_text_dict