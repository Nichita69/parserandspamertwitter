import json


class TwitterParser:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows 95) AppleWebKit/533.9.2 (KHTML, like Gecko) Version/5.0.4 Safari/533.9.2'
    }

    def get_categories(self) -> None:
        file = open("parser.txt", "r", encoding='utf-8')
        twitters = file.readlines()

        clear_data = []
        result = []
        for twitter in twitters:
            clear_data.append(twitter.partition('/status')[0])

        for twitter in clear_data:
            if 'eth' in twitter.lower() or 'nft' in twitter.lower():
                result.append(twitter)

        with open('spamer.txt', 'w+', encoding='utf-8') as file:
            file.write("\n".join(set(result)))
        #

    def parsing(self) -> None:
        file = open("all.txt", "r", encoding='utf-8')
        twitters = file.readlines()
        result = []
        for twitter in twitters:
            result.append(twitter.split("/")[-1])
        with open('all.txt', 'w+', encoding='utf-8') as file:
            file.write("".join(set(result)))

