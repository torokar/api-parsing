import requests as req
# https://sky.pro/wiki/html/kody-sostoyaniya-http-chto-oni-znachat/
# # def retry(func):
# #     def wrapper(website):
# #         for i in range(3):
# #             print(i + 1)
# #             try:
# #                 return func(website)
# #             except:
# #                 print('Ошибка подключения к серверу!', website)
# #                 return None
# #     return wrapper
# #
# # @retry
def connection_website(name_website):
    """Подключение к серверу"""
    response = req.get(name_website)
    return response

def for_dict(list_text_website):
    """Парсинг данных кодов в словарь"""
    code_dict = {}
    for code_text in range(len(list_text_website)):
        if ':' in list_text_website[code_text]:
            index_cut = code_text
            while True:
                find_number = list_text_website[index_cut]
                if find_number.isdigit():
                    break
                else:
                    index_cut -= 1

            end_index = min(code_text + 1, index_cut + 3)
            cut_key = ' '.join(list_text_website[index_cut:end_index])

            index_val = code_text + 1
            while index_val < len(list_text_website):
                find_number = list_text_website[index_val]
                if find_number.isdigit():
                    break
                else:
                    index_val += 1

            cut_val = ' '.join(list_text_website[code_text + 1:index_val])
            code_dict[cut_key] = cut_val
    return code_dict






























