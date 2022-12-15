import json


class TwitterParser:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows 95) AppleWebKit/533.9.2 (KHTML, like Gecko) Version/5.0.4 Safari/533.9.2'
    }

    def get_categories(self) -> None:
        file = open("parser.txt", "r", encoding='utf-16')
        twitters = file.readlines()

        clear_data = []
        result = []
        for twitter in twitters:
            clear_data.append(twitter.partition('/status')[0])

        for twitter in clear_data:
            if 'eth' in twitter.lower() or 'nft' in twitter.lower():
                    result.append(twitter)

        with open('fsf.txt', 'w+', encoding='utf-8') as file:
            file.write("\n".join(set(result)))
        #

    def parsing(self) -> None:
        file = open("first100.txt", "r", encoding='utf-8')
        twitters = file.readlines()
        result = []
        for twitter in twitters:
            result.append(twitter)
        with open('first100.txt', 'w+', encoding='utf-8') as file:
            file.write("".join(set(result)))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# import os
# from contextlib import suppress
#
# files = os.listdir("C:\\Users\\artem.pryatka\\Desktop\\Andrew\\100k pass")
# print("All files", len(files), files)
#
# result = []import json
#
#
# class TwitterParser:
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows; U; Windows 95) AppleWebKit/533.9.2 (KHTML, like Gecko) Version/5.0.4 Safari/533.9.2'
#     }
#
#     def get_categories(self) -> None:
#         file = open("parser.txt", "r", encoding='utf-16')
#         twitters = file.readlines()
#
#         clear_data = []
#         result = []
#         for twitter in twitters:
#             clear_data.append(twitter.partition('/status')[0])
#
#             for twitter in clear_data:
#                 if 'eth' in twitter.lower() or 'nft' in twitter.lower():
#                     result.append(twitter)
#
#         with open('eladiipidor.txt', 'w+', encoding='utf-8') as file:
#             file.write("\n".join(set(result)))
#         #
#
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
#
# # import os
# # from contextlib import suppress
# #
# # files = os.listdir("C:\\Users\\artem.pryatka\\Desktop\\Andrew\\100k pass")
# # print("All files", len(files), files)
# #
# # result = []
# #
# # for file in files:
# #     if file.endswith(".txt"):
# #         with suppress(UnicodeDecodeError):
# #             print("File", file)
# #             with open("C:\\Users\\artem.pryatka\\Desktop\\Andrew\\100k pass\\" + file, "rb") as f:
# #                 for i, ln in enumerate(f):
# #                     if i > 10:
# #                         line = ln.decode()
# #                         if "http" in line:
# #                             with suppress(IndexError, StopIteration):
# #                                 url = line.split(" ")[1].strip()
# #                                 username = next(f).decode().split(" ")[1].strip()
# #                                 password = next(f).decode().split(" ")[1].strip()
# #
# #                                 result.append(f'{url}:{username}:{password}\n')
# #
# # print("Result", len(result), result)
# # with open("result.txt", "w") as f:
#
# for file in files:
#     if file.endswith(".txt"):
#         with suppress(UnicodeDecodeError):
#             print("File", file)
#             with open("C:\\Users\\artem.pryatka\\Desktop\\Andrew\\100k pass\\" + file, "rb") as f:
#                 for i, ln in enumerate(f):
#                     if i > 10:
#                         line = ln.decode()
#                         if "http" in line:
#                             with suppress(IndexError, StopIteration):
#                                 url = line.split(" ")[1].strip()
#                                 username = next(f).decode().split(" ")[1].strip()
#                                 password = next(f).decode().split(" ")[1].strip()
#
#                                 result.append(f'{url}:{username}:{password}\n')
#
# print("Result", len(result), result)
# with open("result.txt", "w") as f:
#     f.write("".join(result))
