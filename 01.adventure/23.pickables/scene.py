import pygame
from sprite_controlled import SpriteControlled
from sprite import Sprite
from sprite_pickable import SpritePickable
from warp import Warp
from ui_group import UiGroup
from ui_panel import UiPanel
from ui_button import UiButton

class Scene:
    
    path = 'D:\\Code\\ArtFx\\Python\\python-training\\01.adventure\\23.pickables\\data\\'

    def __init__(self, filename):
        self.filename = filename
        self.load(filename)

    def load(self, filename):
        file = open(Scene.path + filename)
        data = file.read().splitlines()

        ground_height = 0
        self.cursor = Sprite(0, 0, 'cursor.png', False)
        self.sprites = []
        self.warps = []
        self.pickables = []

        self.ui_top = UiGroup()
        panel = UiPanel(0, 0, 800, 110)
        self.ui_top.add_element(panel)

        for line in data:
            cell = line.split(";")
            # Ground
            if(cell[0] == "ground"):
                self.ground = Sprite(0, 0, cell[1]+".png", False)
                _, screen_h = pygame.display.get_surface().get_size()
                ground_height = screen_h - self.ground.surface.get_height()
                self.ground.y = ground_height
            # Background
            elif(cell[0] == "background"):
                self.background = Sprite(0, 0, cell[1]+".png", False)
            # Player
            elif(cell[0] == "player"):
                height = 0
                if cell[3] == "ground":
                    height = -1
                self.player = SpriteControlled(int(cell[2]), height, cell[1]+".png", True, int(cell[4]))
            # Sprites
            elif(cell[0] == "sprite"):
                height = 0
                if cell[3] == "ground":
                    height = -1
                sprite = Sprite(int(cell[2]), height, cell[1]+".png", True)
                self.sprites.append(sprite)
            # Warps
            elif(cell[0] == "warp"):
                height = 0
                if cell[3] == "ground":
                    height = -1
                warp = Warp(int(cell[2]), height, cell[1]+".png", False, eval(cell[4]))
                self.warps.append(warp)
            # Items
            elif(cell[0] == "pickable"):
                height = 0
                if cell[3] == "ground":
                    height = -1
                item = SpritePickable(int(cell[2]), height, cell[1]+"_ingame.png", False, cell[1])
                self.pickables.append(item)

        # Set heights
        if(self.player.y == -1):
            self.player.y = ground_height
        for s in self.sprites:
            if(s.y == -1):
                s.y = ground_height
        for w in self.warps:
            if(w.y == -1):
                w.y = ground_height - w.surface.get_height() / 2
        for p in self.pickables:
            if(p.y == -1):
                p.y = ground_height - p.surface.get_height()

    def inputs(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click = pygame.mouse.get_pos()
                if(mouse_click[1] > self.ui_top.elements[0].h): # Dirty but effective
                    self.player.move_to(mouse_click[0])
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_F5]:
                    self.load(self.filename)
        self.ui_top.inputs(events)           

    def update(self, change_scene, inventory):
        self.cursor.set_position(pygame.mouse.get_pos())
        self.player.update()
        for w in self.warps:
            if(self.player.intersects(w)):
                change_scene(w.to_scene, w.to_scene_x)
        for p in self.pickables:
            if(self.player.intersects(p)):
                inventory.append(p.pick())
        self.ui_top.update()

    def draw(self, screen):
        self.background.draw(screen)
        self.ground.draw(screen)
        for w in self.warps:
            w.draw(screen)
        for p in self.pickables:
            p.draw(screen)
        for s in self.sprites:
            s.draw(screen)
        self.player.draw(screen)
        self.ui_top.draw(screen)
        self.cursor.draw(screen)
