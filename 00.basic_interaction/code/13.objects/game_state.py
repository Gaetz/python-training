class GameState(object):
    def __init__(self):
        self.quit = False
        self.key = False

    def get_quit(self):
        return self.quit

    def set_quit(self, value):
        self.quit = value

    def get_key(self):
        return self.key

    def set_key(self, value):
        self.key = value