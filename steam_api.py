from gefinder import web_scrape
import requests
import json

def get_steam_games_json():
    #Calls steam applist api with entire steam-library
    resp = requests.get('https://api.steampowered.com/ISteamApps/GetAppList/v02/')
    return resp.json()

def create_steam_dict(steam):
    #creats a dict with steam game name and steam game id from the api response
    game_and_id={}
    for k,v in steam.items():
        for k1,v1 in v.items():
            for item in v1:
                game = item.get('name')
                game_id =  item.get('appid')
                game_and_id[game] = game_id

    return game_and_id
    
def steam_api_statuscode():
    #Checks if steam api is responding with 'OK'
    resp = requests.get('https://api.steampowered.com/ISteamApps/GetAppList/v0002/')
    if resp.status_code == 200:
        return True
    else:
        return False

def get_steam_games_from_list(gamewatcher_list):
    #Returns list containing game names with steam as platform from Gamewatcher.com
    game_list = []
    for item in gamewatcher_list:
        if (str(item)[len(str(item))-10:-5]) == "Steam":
            game_list.append(str(item)[4:-13])
        else:
            pass
    return game_list    

def find_geforce_in_steam(geforce,steam):
    #creates a dict with geforce games in steam + price
    gsi = {}
    #k = name, v = id
    for k,v in steam.items():
        for g in geforce:
            if k == g:
                #Gets steam price from steam api through  appID
                gsi[k]= get_steam_game_price(v)
    return gsi
    

def get_steam_game_price(v):
    try:
        resp = requests.get(f'https://store.steampowered.com/api/appdetails?appids={v}')
        resp_json = resp.json()
        is_free = resp_json[f'{v}']['data']['is_free']
        if is_free == False:
            price = resp_json[f'{v}']['data']['price_overview']['final_formatted']
            return price

    except (TypeError, KeyError) as e:
        print(e)
    
def write_to_json_file(final_list):
    with open("final_list.json", 'w', encoding='utf-8') as f:
        json.dump(final_list, f, ensure_ascii=False, indent=4)



if __name__ == "__main__":
    steam_api_statuscode()

    gamewatcher_list = web_scrape()

    geforce_games = get_steam_games_from_list(gamewatcher_list)

    steam_games = create_steam_dict(get_steam_games_json())

    final_list = find_geforce_in_steam(geforce_games, steam_games)
    
    write_to_json_file(final_list)
