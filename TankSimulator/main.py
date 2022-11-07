import arcade
from our_tank import *
from enemy_tank import *
from bullet import *
from base import *

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Tanks"

class MainGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.bg = arcade.load_texture("images/background.png")
        self.player = Player(self)
        self.enemy = arcade.SpriteList()
        self.bullets = arcade.SpriteList()
        self.red_base = Base("images//red_base.png", self, False)
        self.green_base = Base("images//green_base.png", self, True)
        self.red_base.set_position(1035, 350)
        self.green_base.set_position(165, 350)
        self.time_to_shoot = time.time()
        self.time_to_start = time.time()
        self.timer_1 = arcade.load_texture("images/1.png")
        self.timer_2 = arcade.load_texture("images/2.png")
        self.timer_3 = arcade.load_texture("images/3.png")
        self.timer_go = arcade.load_texture("images/go.png")
        self.win_picture_sprite = arcade.load_texture("images//win.png")
        self.win_picture = None
        self.setup()

    def setup(self):
        for i in range (200, 601, 200):
            enemy = Enemy(self, "images//red.png")
            enemy.set_position(800, i)
            self.enemy.append(enemy)
        self.timer_to_start()
        
            

    def timer_to_start(self):
        if time.time() - self.time_to_start < 5:
            if time.time() - self.time_to_start < 1:
                self.timer_texture = self.timer_3
            if 1 < time.time() - self.time_to_start < 2:
                self.timer_texture = self.timer_2
            if 2 < time.time() - self.time_to_start < 3:
                self.timer_texture = self.timer_1
            if 3 < time.time() - self.time_to_start < 5:
                self.timer_texture = self.timer_go
            
            if self.time_to_start != None:
                arcade.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH/2, SCREEN_HEIGHT, self.timer_texture)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg)
        self.player.draw()
        self.enemy.draw()
        self.bullets.draw()
        self.red_base.draw()
        self.green_base.draw()
        self.timer_to_start()
        if self.win_picture != None:
            arcade.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, self.win_picture, alpha = 122)
        
        
    def update(self, delta_time):
        if time.time() - self.time_to_start >= 3:
            self.player.update()
            self.enemy.update()
            self.bullets.update()
            self.red_base.update(False)
            self.green_base.update(True)
            for bullet in self.bullets:
                if bullet.center_x <= 0 or bullet.center_y <= 0:
                    bullet.kill()
                elif bullet.center_x >= 1200 or bullet.center_y >= 700:
                    bullet.kill()
            if self.player.hp <= 0:
                self.player.texture = arcade.load_texture("images//green_broken.png")
            if self.red_base.hp <= 0:
                self.win_picture = self.win_picture_sprite


    def on_key_press(self, key, modifiers):
        if self.player.hp > 0:
            if arcade.key.A == key:
                self.player.change_angle = 3
            elif arcade.key.D == key:
                self.player.change_angle = -3
            if arcade.key.W == key:
                self.player.change_x = 2
                self.player.change_y = 2
            if arcade.key.SPACE == key:
                if time.time() - self.time_to_shoot > 1:
                    self.player.shoot()
                    self.time_to_shoot = time.time()
            if arcade.key.E == key and (self.red_base.hp <= 0 or self.green_base.hp <= 0):
                self.reset()
    
    def on_key_release(self, key, modifiers):
        if arcade.key.A == key or arcade.key.D == key:
            self.player.change_angle = 0
        if arcade.key.W == key:
            self.player.change_x = 0
            self.player.change_y = 0
    
    def reset(self):
        self.player = Player(self)
        self.enemy = arcade.SpriteList()
        self.bullets = arcade.SpriteList()
        self.red_base = Base("images//red_base.png", self, False)
        self.green_base = Base("images//green_base.png", self, True)
        self.red_base.set_position(1035, 350)
        self.green_base.set_position(165, 350)
        self.setup()
        self.time_to_start = time.time()
        self.win_picture = None

        
        


window = MainGame()
arcade.run()

#Устранить эпилептическое мессиво
#поставить таймер на выстерлы, как у PeaShooter
#если пуля вылетит за пределы экрана, то уничтожать ее
#дз:
#сделать смерть противника и игрока
#если хп кончилось, то надо перестать двигаться и поменять self.texture на broken соответствующего 
#От Pavel Maitakov всем 06:51 PM
#сделать попадание по базе, чтобы у нее отнималось хп
#настроить баланс

