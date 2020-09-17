import csv
from bs4 import BeautifulSoup
import requests
import class_game
import re


def status_report(status):
    """Simply prints status"""

    if status == 1:
        return "\n\n*** Start sequence initiated ***\n\n*** Now retrieving data... ***"
    elif status == 2:
        return "\n*** Data received successfully ***\n\n*** Formatting data... ***"
    elif status == 3:
        return "\n*** Writing data to csv-file... ***\n"
    elif status == 4:
        return "*** Done ***"


def instantiate_games(games):
    """Creates instances of each game in list and adds attributes"""

    objects = []
    for game in games:

        game_name = game[0]
        game_store = game[1]

        # Creates an instance, sets attributes and stores in list.
        game_instance = class_game.Game()
        game_instance.set_game_name(game_name)
        game_instance.get_store_names(game_store)
        objects.append(game_instance)

    return objects


def remove_html_tags(text):
    """Removes html tags with regular expression"""

    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


def reverse_string(text):
    """Returns a reversed string"""

    return text[::-1]


def reverse_two_strings(text_1, text_2):
    """Redirects two strings to the reverse_string function"""

    text_1 = reverse_string(text_1)
    text_2 = reverse_string(text_2)
    return text_1, text_2


def strip_spaces(text1, text2):
    """Takes two strings and strips them from blank spaces"""

    text1 = text1.strip()
    text2 = text2.strip()
    return text1, text2


def formatter(html_item):
    """Returns the values in the html item in right format"""

    item = remove_html_tags(html_item.text)

    # I want to split on the last dash so I simply reverse the text and split on the first dash.
    # When the format is correct I reverse them again and return the the two strings.
    reversed_item = reverse_string(item)
    reversed_store, reversed_game = reversed_item.split("-", 1)
    reversed_store, reversed_game = strip_spaces(reversed_store, reversed_game)

    return reverse_two_strings(reversed_game, reversed_store)


def web_scrape():
    """Web scrapes and gets the requested list from url"""

    try:
        response = requests.get("https://www.gamewatcher.com/news/nvidia-geforce-now-games-list")
        html = response.text
        soup = BeautifulSoup(html, features="lxml")

        article = soup.find('div', class_='content')
        section = article.find('ul')
        return section.findAll('li')

    except Exception as error_message:
        web_scrape_fail(error_message)


def web_scrape_fail(error_message):
    """Informs user if web scraping failed, then exits program"""

    print("\n*** Web scraping failed ***")
    print("\nERROR MESSAGE: ")
    print(error_message)
    print("\nPOSSIBLE SOLUTION(S):\n"
          "- Check internet connection.\n"
          "- Ensure that the URL is still relevant.")
    exit()


def clear_csv():
    """Clears all text files"""

    try:
        open('games.csv', 'w', encoding='utf-8').close()
    except PermissionError as error:
        csv_file_fail(error)


def write_to_csv(games, vendor_amount):
    """Stores the data in csv-file"""

    with open('games.csv', 'w', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["GAME", f"STEAM ({vendor_amount[0]})", "STEAM PRICE", f"EPIC GAMES ({vendor_amount[1]})",
                             "EPIC GAMES PRICE", f"UPLAY ({vendor_amount[2]})", "UPLAY PRICE"])

        for game in games:
            csv_writer.writerow([game.name, game.steam_store, game.steam_price, game.epic_store, game.epic_price,
                                 game.uplay_store, game.uplay_price])


def csv_file_fail(error_message):
    """Informs user if csv reading failed, then exits program"""

    print("\n*** CSV failed to open ***")
    print("\nERROR MESSAGE: ")
    print(error_message)

    print("\nPOSSIBLE SOLUTION(S):\n"
          "- Try closing your CSV reader and restart GeFinder.")
    exit()


def separate_items(html_list):
    """Takes each item in the html list and separates game from store"""

    for item in html_list:
        try:
            game, store = formatter(item)
        except ValueError:
            continue

        separated_item = [game, store]
        game_list.append(separated_item)


def per_vendor(games):
    """Returns the number of games per vendor"""

    steam = 0
    epic = 0
    uplay = 0

    for game in games:

        if game.steam_store is not "":
            steam += 1
        if game.epic_store is not "":
            epic += 1
        if game.uplay_store is not "":
            uplay += 1

    return steam, epic, uplay


def run_gefinder():
    """Runs application"""

    print(status_report(1))
    # Clear all text files
    clear_csv()

    html_list = web_scrape()
    print(status_report(2))
    separate_items(html_list)

    # Creates objects of each line in the li-list
    game_objects = instantiate_games(game_list)
    print(status_report(3))

    vendor_amount = per_vendor(game_objects)
    write_to_csv(game_objects, vendor_amount)
    print(status_report(4))


if __name__ == '__main__':

    game_list = []
    run_gefinder()



