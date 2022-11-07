import arcade
import random
from plants import *
from items import *
from constants import *
from zombies import *
from achiviments import *

class My_game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.bg = arcade.load_texture("textures/background.jpg")
        self.menu = arcade.load_texture("textures/menu_vertical.png")
        self.seed_sound =arcade.load_sound("sounds/seed.mp3")
        self.suns_sound =arcade.load_sound("sounds/sunspawn.mp3")
        self.peas_sound =arcade.load_sound("sounds/peaspawn.mp3")
        self.main_theme =arcade.load_sound("sounds/grasswalk.mp3")
        self.seed = None
        self.plants = arcade.SpriteList()
        self.peas = arcade.SpriteList()
        self.suns = arcade.SpriteList()
        self.zombies = arcade.SpriteList()
        self.sun_score = 100
        self.falling_sun = time.time()
        self.zombie_spawn = time.time()
        self.zom_time_to_spawn = 15
        self.z_choice = random.randint(1,3)
        self.achiviment_event = EventAchiviments()
        self.first_blood_flag = False
        self.main_theme.play (0.6,0,True)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(500, 300, 1000, 600, self.bg)
        arcade.draw_texture_rectangle(67, 300, 134, 600, self.menu)
        self.plants.draw()
        self.peas.draw()
        self.suns.draw()
        self.zombies.draw()
        self.achiviment_event.draw()
        if self.sun_score >= 0:
            arcade.draw_text(f'{self.sun_score}', 33, 490, (255, 255, 0), 33)
        else:
            arcade.draw_text(f'Неправильно, попробуй ещё раз!', 33, 490, (255, 255, 0), 33)

        if self.seed != None:
            self.seed.draw()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if 16 <= x <= 116:
            if 370 <= y <= 480:
                self.seed = SunFlower(self)
            if 255 <= y <= 365:
                self.seed = PeaShooter(self)
            if 140 <= y <= 250:
                self.seed = WallNut(self)
            if 25 <= y <= 135:
                self.seed = TorchWood(self)
        
        for sun in self.suns:
            if sun.left < x < sun.right and sun.bottom < y < sun.top:
                sun.kill()
                self.sun_score += 25
                 
                
    
    def on_mouse_motion(self, x, y, dx, dy):
        if self.seed != None:
            self.seed.center_x = x
            self.seed.center_y = y
    
    def on_mouse_release(self, x, y, button, modifiers):
        if 248 <= x <= 950 and 24 <= y <= 524 and self.seed != None:
                new_x, col = cal_cent_x(x)
                new_y, cal = cal_cent_y(y)
                self.seed.center_x = new_x
                self.seed.center_y = new_y
                if self.sun_score >= self.seed.cost:
                    self.plants.append(self.seed)
                    self.seed_sound.play (0.6,0,False)
                    self.sun_score -= self.seed.cost

                else:
                    self.sun_score = -50
            
        self.seed = None
        
        
    
    def update(self, delta_time):
        self.plants.update()
        self.plants.update_animation(delta_time/3)
        self.peas.update()
        self.suns.update()
        for zombie in self.zombies:
            first_zombie_death = zombie.update()
            if first_zombie_death == True and self.first_blood_flag == False:
                self.achiviment_event.append("first_kill")
                self.first_blood_flag = True

        self.zombies.update_animation(delta_time/3)
        for plant in self.plants:
            if arcade.check_for_collision_with_list(plant, self.plants):
                self.plants.remove(plant)
        if time.time() - self.falling_sun >= 7.5:
            x = random.randint(248, 1000)
            y = SCREEN_HEIGHT + 25
            self.suns.append(SunsFall(x, y))
            self.suns_sound.play (0.6,0,False)
            self.falling_sun = time.time()

        if time.time() - self.zombie_spawn >= self.zom_time_to_spawn:
            if 1 <= self.z_choice <= 680:
                self.zombies.append(Default_Z(self))
            if 681 <= self.z_choice <= 890:
                self.zombies.append(Conus_Z(self))
            if 891 <= self.z_choice <= 999:
                self.zombies.append(Bucket_Z(self))
            if self.z_choice == 1000:
                self.zombies.append(Bucket_Z(self))
            self.zombie_spawn = time.time()
            if self.zom_time_to_spawn > 3:
                self.zom_time_to_spawn -= 0.1
            self.z_choice = random.randint(1,1000)
        
        
            

        

    
window = My_game()
arcade.run()

#надо определить границы для кнопок в координатах
#в фунции нажатия на кнопку выводить координаты на экран, таким образом X у тебя для всех кнопок, а Y разным
#сделать анимацию для всех спрайтов растений
#1) загрузить все изображения анимации
#2) запустить анимацию в main
#домашнее задание:
#1) сделать спавн солнышек из растения 
#2) добавить возможность собирать солнышки (очень похоже на то как мы сделали нажатие на кнопки в меню, надо разобрать спрайт лист всех солнышек и проверять их лево и право на x, а также верх и них по y)
#3) добавить счет солнышек по координатам 33, 490

#домашнее задание:
#реализовать возможность, чтобы нельзя было поставить 2 растения в одну клетку:
#1) создать пустой лист в мейне
#2) при постановке растения проверять не занята данная ячейка? < if (row, col ) not in self.plantList > 
#3) добавлять номер строки и столбца в виде кортежа (кортеж - это скобки), состоящего из номера строки и столбца

#сделать инит для всех зомби, определить для них характеристики, загрузить текстуры для анимации
#для проверки можешь поставить одного зомби и сделать так, чтобы по нему можно было стрелять

#№1
#настроить баланс в игре
#№2
#сделать так, чтобы зомби мог есть растение
