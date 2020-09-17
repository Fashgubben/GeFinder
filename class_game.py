

class Game:
    def __init__(self):

        self.name = ""
        self.steam_store = ""
        self.epic_store = ""
        self.uplay_store = ""
        self.steam_price = ""
        self.epic_price = ""
        self.uplay_price = ""

    def set_game_name(self, name):
        self.name = name

    def get_store_names(self, stores):

        if "Steam" in stores:
            self.set_steam_store()

        if "Epic Games Launcher" in stores:
            self.set_epic_store()

        if "Uplay" in stores:
            self.set_uplay_store()

    # AVAILABLE AT STORE
    def set_steam_store(self):
        self.steam_store = "Steam"
        self.steam_price = "0"

    def set_epic_store(self):
        self.epic_store = "Epic Games"
        self.epic_price = "0"

    def set_uplay_store(self):
        self.uplay_store = "Uplay"
        self.uplay_price = "0"

    # PRICE
    def get_steam_price(self):
        pass

    def set_steam_price(self, price):
        self.steam_price = price

    def get_epic_price(self):
        pass

    def set_epic_price(self, price):
        self.epic_price = price

    def get_uplay_price(self):
        pass

    def set_uplay_price(self, price):
        self.uplay_price = price
