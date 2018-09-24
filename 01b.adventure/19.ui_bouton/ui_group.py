class UiGroup(object):
    def __init__(self):
        self.elements = []

    def add_element(self, element):
        self.elements.append(element)

    def set_visible(self, value):
        for e in self.elements:
            e.set_visible(value)

    def inputs(self, events):
        for e in self.elements:
            e.inputs(events)

    def update(self):
        for e in self.elements:
            e.update()

    def draw(self, screen):
        for e in self.elements:
            e.draw(screen)