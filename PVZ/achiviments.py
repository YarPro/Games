import arcade
import time
import constants
class Achiviments():
    def __init__(self, name, img, descript):
        self.name = name
        self.img = arcade.load_texture(img)
        self.descript = descript

    def draw(self):
        arcade.draw_texture_rectangle(constants.SCREEN_WIDTH -250, constants.SCREEN_HEIGHT -60, 120, 100, self.img)
        arcade.draw_text(self.descript, constants.SCREEN_WIDTH - 220, constants.SCREEN_HEIGHT - 60, arcade.color.BLACK)

class EventAchiviments():
    def __init__(self):
        self.dict = {}
        self.dict["first_kill"] = Achiviments("Первая кровь", "achiviments//first_blood.png", "Ты грохнул первого зомбаря!")
        self.activated_achiviments = []
        

    def draw(self):
        for achiviment in self.activated_achiviments:
            achiviment.draw()

    def append(self, name):
        self.activated_achiviments.append(self.dict[name])
        