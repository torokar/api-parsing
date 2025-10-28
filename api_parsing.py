from recepts.http_codes import for_dict, connection_website
from bs4 import BeautifulSoup as beautiful
from recepts.emoji import parsing_emoji, parsing_text
website = 'https://sky.pro/wiki/html/kody-sostoyaniya-http-chto-oni-znachat/'

"""Коды ошибок"""
result_response = connection_website(website)
soup = beautiful(result_response.content, 'html.parser')
li = soup.find_all('li')

text_website = ''
for i in li:
    text_website += i.text

text_with_space = text_website.replace('.', ' . ')
list_text_website = text_with_space.split(' ')
code_dict = {}
code_dict = for_dict(list_text_website)
print(code_dict)

"""Эмодзи"""
website_emoji = 'https://emojiguide.org/ru/%D0%B5%D0%B4%D0%B0-%D0%B8-%D0%BD%D0%B0%D0%BF%D0%B8%D1%82%D0%BA%D0%B8'
emoji_list = []
emoji_text_dict = {}
connection_website(website_emoji)
result_response_emoji = connection_website(website_emoji)
soup = beautiful(result_response_emoji.text, 'html.parser')
emoji_list = parsing_emoji(soup)
emoji_text_dict = parsing_text(soup, emoji_list)
print(emoji_text_dict)
