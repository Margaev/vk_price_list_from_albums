import UserInterface
import VkHandler
import re


def main():
    vk_handler = VkHandler.Album()

    album_title_list = vk_handler.get_album_titles()
    ui = UserInterface.UserInterface(album_title_list)

    indices = ui.get_selected_items()

    album_title_list = [album_title_list[i] for i in indices]

    photo_descriptions = {}
    album_ids = []
    for i in indices:
        album_ids.append(vk_handler.get_albums()['items'][i]['id'])
    photos = vk_handler.get_photos(album_ids)
    for key, value in photos.items():
        photo_descriptions[key] = []
        for i in value:
            photo_descriptions[key].append(str(i['id']) + '\n' + i['text'])
    for key, value in photo_descriptions.items():
        for i, item in enumerate(value):
            photo_descriptions[key][i] = item.split('\n')[:3]
            while len(photo_descriptions[key][i]) < 3:
                photo_descriptions[key][i].append(' ')
    make_table(photo_descriptions, vk_handler, album_title_list)


def make_table(descriptions, vk_handler, album_title_list):
    with open('Price_list.txt', 'w') as f:
        f.write('ссылка\tназвание\tцена\n\n')
        i = 0
        for key, value in descriptions.items():
            # f.write('https://vk.com/album' + vk_handler.group_id + '_' + str(key) + '\n')
            f.write(str(album_title_list[i]) + '\n\n')
            i += 1
            for v in value:
                try:
                    prices_str = str(v[2])
                    prices_re = re.compile(r'\((\d+),(\d+),(\d+),(\d+)\+\)')
                    try:
                        prices = list()
                        prices.append(prices_re.search(prices_str).group(1))
                        prices.append(prices_re.search(prices_str).group(2))
                        prices.append(prices_re.search(prices_str).group(3))
                        prices.append(prices_re.search(prices_str).group(4))
                        f.write('https://vk.com/photo' + vk_handler.group_id + '_' + str(v[0]) + '\t'
                                + str(v[1]) + '\t' + prices[0] + '\t' + prices[1]
                                + '\t' + prices[2] + '\t' + prices[3] + '\n\n')
                    except AttributeError:
                        pass

                except IndexError:
                    continue
                except UnicodeEncodeError:
                    f.write('Ошибка!\n')


if __name__ == '__main__':
    main()
