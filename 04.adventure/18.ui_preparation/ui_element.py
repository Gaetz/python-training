class UiElement(object):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.visible = True
        self.events = {}

    def set_visible(self, value):
        self.visible = value

    def set_event(self, event_type, function):
        self.events[event_type] = function