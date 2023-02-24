from types import CellType
import pygame,time,random
from pygame import mixer
from pygame.time import Clock
pygame.init()
mixer.init()

#### color ######
white=(255,255,255)
blue=(224, 247, 250)
black=(0,0,0)
green=(0,255,0)
yellow=(254,255,128)
red=(255,0,0)
cyan=(0,216,216)
#musi2,c
def music(tune,volume): 
    mixer.music.load(tune)
    mixer.music.set_volume(volume)
    mixer.music.play(-1)

music("jungle_start.mp3",0.9)

#### screen Font ######
def screen_font(word,x,y,style,size,color):
    font=pygame.font.SysFont(style,size)
    text=font.render(word,True, color)
    screen.blit(text,(x,y))
    

###### Game Image or icons #######
def game_images(image,x,y,width,height):
    pic = pygame.image.load(image).convert_alpha()
    pic=pygame.transform.scale(pic,(width,height))
    screen.blit(pic,(x,y))
   

#### Screen Background Image ####
def screen_background(image,x,y):
    pic = pygame.image.load(image).convert_alpha()
    screen.blit(pic,(x,y))
   

#screen display
screen=pygame.display.set_mode((1500,700))
pygame.display.set_caption("MONKEY")
#logic
icon = pygame.image.load("lets_go.png")
pygame.display.set_icon(icon)

#start part
back_logo=pygame.image.load("monkey_logo.jpg")
back_logo=pygame.transform.scale(back_logo,(1500,900))
screen.blit(back_logo,(0,0))
screen_font("MONKEY CATCH",580,20,'calibri',70,(255,255,255))
screen_font("LOADING...",650,350,'calibri',60,(255,255,255))

pygame.display.update()
time.sleep(4)


manual=pygame.image.load('mannual.jpg').convert_alpha()
start=pygame.image.load('play.png').convert_alpha()
exit=pygame.image.load('exit3.png').convert_alpha()

class Button:
    def __init__(self,x,y,image):
        self.image=pygame.transform.scale(image,(130,130))
        self.x=x
        self.y=y

    def draw(self):
        screen.blit(self.image,(self.x,self.y))
#Manual=Button(20,200,manual)
Start=Button(550,400,start)
Exit=Button(900,400,exit)


game_images("back.jpg",0,0,1500,900)
screen_font("MONKEY CATCH UP",500,30,'calibri',70,blue)

Start.draw()
Exit.draw()
pygame.display.update()
###################function for calling in the events#####

def manual_fun():
    game_images("circle.png",700,170,600,600)
    screen_font(" MANUAL RULES",880,200,'callibri',40,blue)
    pygame.display.update()

# Game Module #######
def start_games(move_x,move_y):
    if((move_x<=10 or move_x>=1210) and (move_y==0)):
        game_images("monkey.png",1210,0,100,90)
        pygame.display.update()
    # else:
    #     game_images("monkey.png",move_x,move_y,100,90)
    #     game_images("pipe.png",10,0,200,210)
    #     game_images("pipe.png",410,0,200,210)
    #     game_images("pipe.png",810,0,200,210)
    #     game_images("pipe.png",1210,0,200,210)
    #     pygame.display.update()

brown=(139,69,19)
pipe1=pygame.Rect(0,70,90,210)
pipe2=pygame.Rect(490,70,90,210)
pipe3=pygame.Rect(930,70,90,210)
pipe4=pygame.Rect(1360,70,90,210)

def pipes():
    pygame.draw.rect(screen,green,pipe1)
    pygame.draw.rect(screen,green,pipe2)
    pygame.draw.rect(screen,green,pipe3)
    pygame.draw.rect(screen,green,pipe4)

fall_speed=7
fall_y=0


# def eating():
#     global fall_speed,fall_y
#     eatable=["apple.png","banana.png","brocoli.png","burger.png","cake.png","carrot.png","chocolates.png","cucumber.png","dragon-fruit.png","eggplant.png","french_fries.png","grapes.png","guava.png","mango.png","orange.png","pineapple.png","pizza.png","spinach.png","tomato.png"]
#     pos=[10,500,940,1370]
#     eating=pygame.image.load(eatable)
#     eating=pygame.transform.scale(eating,(60,60))
#     eating_rect=eating.get_rect()
#     eating_rect.x=pos
#     eating_rect.y=fall_y
#     return eating,eating_rect.x,eating_rect.y



lev=0

def levels():    
    green=pygame.image.load("green_back.jpg")
    green=pygame.transform.scale(green,(1500,1000))
    screen.blit(green,(0,0))
    monkey_help=pygame.image.load("help.png")
    monkey_help=pygame.transform.scale(monkey_help,(90,90))
    monkey_rect=monkey_help.get_rect()
    monkey_rect.x=1300
    monkey_rect.y=30
    screen.blit(monkey_help,(monkey_rect.x,monkey_rect.y))
    font=pygame.font.SysFont('calibri',80)
    text=font.render("LEVELS",True, (0,255,0))
    screen.blit(text,(700,50))

    level_1=pygame.image.load("level_1.png")
    level_1=pygame.transform.scale(level_1,(80,80))
    level1=pygame.image.load("level1.png")
    level1=pygame.transform.scale(level1,(80,80))

    l_1=level_1.get_rect()
    l1=level1.get_rect()
    l_1.x=360
    l_1.y=160
    l1.x=500
    l1.y=160
    screen.blit(level_1,(l_1.x,l_1.y))
    screen.blit(level1,(l1.x,l1.y))
    screen_font("BASIC LEVEL",600,160,'calibri',80,(0,0,255))

    level_2=pygame.image.load("level_2.png")
    level_2=pygame.transform.scale(level_2,(80,80))
    level2=pygame.image.load("level2.png")
    level2=pygame.transform.scale(level2,(80,80))

    l_2=level_2.get_rect()
    l2=level2.get_rect()
    l_2.x=360
    l_2.y=360
    l2.x=500
    l2.y=360
    screen.blit(level_2,(l_2.x,l_2.y))
    screen.blit(level2,(l2.x,l2.y))
    screen_font("INTERMEDIATE LEVEL",600,360,'calibri',80,(0,0,255))

    level_3=pygame.image.load("level_3.png")
    level_3=pygame.transform.scale(level_3,(80,80))
    level3=pygame.image.load("level3.png")
    level3=pygame.transform.scale(level3,(80,80))
    l_3=level_3.get_rect()
    l3=level3.get_rect()
    l_3.x=360
    l_3.y=560
    l3.x=500
    l3.y=560
    screen.blit(level_3,(l_3.x,l_3.y))
    screen.blit(level3,(l3.x,l3.y))
    screen_font("ADVANCED LEVEL",600,560,'calibri',80,(0,0,255))
    pygame.display.update()
    while True:
        pos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                if (pos[0]>=l_1.left and pos[0]<=l_1.right) and (pos[1]<=l_1.bottom and pos[1]>=l_1.top):
                    pygame.draw.rect(screen,(0,0,255),l_1,4)
                    pygame.display.update()
                    time.sleep(1)
                    return 1
                    
                elif (pos[0]>=l_2.left and pos[0]<=l_2.right) and (pos[1]<=l_2.bottom and pos[1]>=l_2.top):
                    pygame.draw.rect(screen,(0,0,255),l_2,4)
                    pygame.display.update()
                    time.sleep(1)
                    print("2")
                    return 2
                elif (pos[0]>=l_3.left and pos[0]<=l_3.right) and (pos[1]<=l_3.bottom and pos[1]>=l_3.top):
                    pygame.draw.rect(screen,(0,0,255),l_3,4)
                    pygame.display.update()
                    time.sleep(1)
                    return 3
                elif (pos[0]>=monkey_rect.left and pos[0]<=monkey_rect.right) and (pos[1]<=monkey_rect.bottom and pos[1]>=monkey_rect.top):
                    return 4
                    
def mannual():
    
    image=pygame.image.load("mannual.jpg")
    image=pygame.transform.scale(image,(2500,1200))

    back=pygame.image.load("back.png")
    back=pygame.transform.scale(back,(80,80))
    back_rect=back.get_rect()
    back_rect.x=30
    back_rect.y=30
    screen.blit(image,(0,0))
    screen.blit(back,(back_rect.x,back_rect.y))
    screen_font("Game Mannual",650,30,'calibri',50,(0,0,255))
    screen_font("In this game the will catch up the items.",450,80,'calibri',50,(255,255,255))
    screen_font("The items wil coming From the pipes randomly!.",250,140,'calibri',50,(255,255,255))
    screen_font("The Monkey have to catch up all the healthy edible items",250,180,'calibri',50,(255,255,255))
    screen_font("The Monkey only move along the x-axis",250,220,'calibri',50,(255,255,255))
    screen_font("=============================================",150,360,'calibri',50,(255,255,255))
    screen_font("GAME  CONTROL",600,290,'calibri',50,(0,0,255))
    screen_font("LEFT ARROW => FOR LEFT ALONG X-AXIS",350,400,'calibri',50,(255,255,255))
    screen_font("RIGHT ARROW => FOR RIGHT ALONG X-AXIS",350,460,'calibri',50,(255,255,255))
    pygame.display.update()
    
    while True:
        pos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if (pos[0]>=back_rect.left and pos[0]<=back_rect.right) and (pos[1]<=back_rect.bottom and pos[1]>=back_rect.top):
                    start_fun()
            elif event.type==pygame.QUIT:
                exit()
        
   

global level
def start_fun():

    lev=levels()#######start from here#######
    if lev==4:
        mannual()
        lev=levels()
    velocity_x=0

    end=False
    screen.fill(black)
    game_images("lets_go.png",500,150,500,500)
    pygame.display.update()
    # time.sleep(1)

    # game_images("background.jpg",0,0,900,900)
    spaceship=pygame.image.load("monkey.png")
    spaceship=pygame.transform.scale(spaceship,(100,90))

    monkey=spaceship.get_rect()
    monkey.x=500
    monkey.y=600

    # eatable=["apple.png","banana.png","brocoli.png","burger.png","cake.png","carrot.png","chocolates.png","cucumber.png","dragon-fruit.png","eggplant.png","french_fries.png","grapes.png","guava.png","mango.png","orange.png","pineapple.png","pizza.png","spinach.png","tomato.png"]
    pos=[10,500,940,1370]
    global fall_speed,fall_y

    item=["apple.png","banana.png","brocoli.png","burger.png","cake.png","carrot.png","chocolates.png","cucumber.png","dragon-fruit.png","eggplant.png","french_fries.png","grapes.png","guava.png","mango.png","orange.png","pineapple.png","pizza.png","spinach.png","tomato.png"]
    fruits=["apple.png","banana.png","grapes.png","guava.png","dragon-fruit.png","orange.png","pineapple.png","mango.png"]
    vegies=["brocoli.png","carrot.png","cucumber.png","eggplant.png","spinach.png"]
    
    eat=random.choice(item)
    place=random.choice(pos)
    eating=pygame.image.load(eat)
    eating=pygame.transform.scale(eating,(60,60))
    eating_rect=eating.get_rect()
    eating_rect.x=place
    eating_rect.y=80
    # elif lev==2:
    #     eat=random.choice(vegies)
    #     place=random.choice(pos)
    #     eating=pygame.image.load(eat)
    #     eating=pygame.transform.scale(eating,(60,60))
    #     eating_rect=eating.get_rect()
    #     eating_rect.x=place
    #     eating_rect.y=80
    # elif lev==3:
    #     eat=random.choice(item)
    #     place=random.choice(pos)
    #     eating=pygame.image.load(eat)
    #     eating=pygame.transform.scale(eating,(60,60))
    #     eating_rect=eating.get_rect()
    #     eating_rect.x=place
    #     eating_rect.y=80

    health_count=3
    bonus_count=0

    
    # level=1
    # target=random.randint(10,30)
    # fruit1=random.choice(fruits)
    # f=pygame.image.load(fruit1)
    # f=pygame.transform.scale(f,(30,30))
    target=random.randint(1,5)
    
    collect_fruits=random.randint(1,3)
    fruit2=random.choice(fruits)
    f=pygame.image.load(fruit2)
    f=pygame.transform.scale(f,(30,30))
    
    collect_vegies=random.randint(1,3)
    vegies1=random.choice(vegies)
    v = pygame.image.load(vegies1)
    v=pygame.transform.scale(v,(30,30))

    ######################### For level 3 ###################
    # fruit3=random.choice(fruits)     
    # vegies3=random.choice(vegies)
    min=2
    sec=60
    milisec=0
    
    
    while not end:

        game_level="GAME_LEVEL::"+str(lev)
        life="[LIFE:"+str(int(health_count))+"]"
        score="[ SCORE:"+str(int(bonus_count))+"]"
        goal="[ Target:"+str(int(target))+"]"
        
        screen_font(goal,10,10,'calibri',35,red)
        screen_font(score,180,10,'calibri',35,red)
        screen_font(life,360,10,'calibri',35,red)
        screen_font(game_level,750,10,'calibri',35,(0,0,255))
        
        global fall_speed
        if lev==1:
            screen.blit(f,(480,10))
            fruit_collect=":"+str(int(collect_fruits))
            screen_font(fruit_collect,520,10,'calibri',35,red)
           
        elif lev==2:
            # fruit_collect=":"+str(int(collect))+"]" 
            # screen.blit(f,(480,10))
            # screen_font(fruit_collect,520,10,'calibri',35,red)
            screen.blit(v,(480,10))
            vegies_collect=":"+str(int(collect_vegies))  
            screen_font(vegies_collect,520,10,'calibri',35,red)
            
        elif lev==3:
            screen.blit(f,(480,10))
            fruit_collect=":"+str(int(collect_fruits)) 
            screen_font(fruit_collect,520,10,'calibri',35,red)
            
            screen.blit(v,(580,10))
            vegies_collect=":"+str(int(collect_vegies))  
            screen_font(vegies_collect,610,10,'calibri',35,red)

            timing="["+str(min)+":"+str(sec)+"]"
            screen_font(timing,1360,10,'calibri',35,red)
        
        pygame.display.update()

        game_images("background.jpg",0,0,1800,900)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            spaceship=pygame.image.load("monkey.png")
            spaceship=pygame.transform.scale(spaceship,(100,90))
            spaceship=pygame.transform.flip(spaceship,True,False)
            velocity_x=-20
            
        elif keys[pygame.K_RIGHT]:
            spaceship=pygame.image.load("monkey.png")
            spaceship=pygame.transform.scale(spaceship,(100,90))
            spaceship=pygame.transform.rotate(spaceship,360)
            velocity_x=20
            
       
        monkey.x=monkey.x+velocity_x
        screen.blit(spaceship,(monkey.x,monkey.y))
        velocity_x=0
        # eating(eat,place) 
        # eating=pygame.image.load(eat)
        # eating=pygame.transform.scale(eating,(60,60))
        # eating_rect=eating.get_rect()
        # eating_rect.x=place
        # eating_rect.y=fall_y
        # eating_rect.y=eating_rect.y+fall_speed
        
        eating_rect.y=eating_rect.y+fall_speed
        
        if eating_rect.y>=800:
            eat=random.choice(item)
            place=random.choice(pos)
            eating=pygame.image.load(eat)
            eating=pygame.transform.scale(eating,(60,60))
            eating_rect=eating.get_rect()
            eating_rect.x=place
            eating_rect.y=80

        elif eating_rect.y<800: 
            if lev==1:
                mixer.music.stop()
                music("game_start.mp3",0.9)
                
                if eat==fruit2:      
                    if eating_rect.colliderect(monkey):
                        pygame.draw.rect(screen,(0,255,0),monkey,2)
                        bonus_count=bonus_count+0.04
                        collect_fruits=collect_fruits-0.04
                elif eat=="burger.png":
                    if eating_rect.colliderect(monkey):
                        pygame.draw.rect(screen,red,monkey,2)
                        health_count=health_count-0.04
                elif eat=="cake.png":
                    if eating_rect.colliderect(monkey):
                        pygame.draw.rect(screen,red,monkey,2)
                        health_count=health_count-0.04
                elif eat=="chocolates.png":
                    if eating_rect.colliderect(monkey):
                        pygame.draw.rect(screen,red,monkey,2)
                        health_count=health_count-0.04
                elif eat=="french_fries.png":
                    if eating_rect.colliderect(monkey):
                        pygame.draw.rect(screen,red,monkey,2)
                        health_count=health_count-0.04
                elif eat=="pizza.png":
                    if eating_rect.colliderect(monkey):
                        pygame.draw.rect(screen,red,monkey,2)
                        health_count=health_count-0.04  
                else:
                    if eating_rect.colliderect(monkey):
                        bonus_count=bonus_count+0.04
                        pygame.draw.rect(screen,(0,255,0),monkey,2)
                
                if bonus_count>=target and collect_fruits<=1:
                    target=random.randint(1,5)
                    health_count=3
                    bonus_count=0
                    collect_fruits=random.randint(1,3)
                    fruit2=random.choice(fruits)
                    f=pygame.image.load(fruit2)
                    f=pygame.transform.scale(f,(30,30))
                    win=pygame.image.load("win.png")
                    win=pygame.transform.scale(win,(140,140))
                    ending=pygame.image.load("background.jpg")
                    screen.blit(ending,(0,0))
                    screen.blit(win,(250,400))
                    screen_font("HURREY!, You completed the Level_1!",450,450,'calibri',50,(255,255,0))
                    pygame.display.update()
                    mixer.music.stop()
                    music("monkey_happy.wav",0.9)
                    time.sleep(3)
                    mixer.music.stop()
                    music("jungle_start.mp3",0.9)
                    lev=0
                    lev=levels()

            elif lev==2:
                mixer.music.stop()
                music("game_start.mp3",0.9)

                if eat==vegies1:
                    if eating_rect.colliderect(monkey):
                        pygame.draw.rect(screen,(0,255,0),monkey,2)
                        bonus_count=bonus_count+0.03
                        collect_vegies=collect_vegies-0.03
                        pygame.draw.rect(screen,(0,255,0),monkey,2)
                elif eat=="burger.png":
                    if eating_rect.colliderect(monkey):
                        pygame.draw.rect(screen,red,monkey,2)
                        health_count=health_count-0.03
                elif eat=="cake.png":
                    if eating_rect.colliderect(monkey):
                        pygame.draw.rect(screen,red,monkey,2)
                        health_count=health_count-0.03
                elif eat=="chocolates.png":
                    if eating_rect.colliderect(monkey):
                        pygame.draw.rect(screen,red,monkey,2)
                        health_count=health_count-0.03
                elif eat=="french_fries.png":
                    if eating_rect.colliderect(monkey):
                        pygame.draw.rect(screen,red,monkey,2)
                        health_count=health_count-0.03
                elif eat=="pizza.png":
                    if eating_rect.colliderect(monkey):
                        pygame.draw.rect(screen,red,monkey,2)
                        health_count=health_count-0.03
                else:
                    if eating_rect.colliderect(monkey):
                        pygame.draw.rect(screen,(0,255,0),monkey,2)
                        bonus_count=bonus_count+0.03
                
                if bonus_count>=target and collect_vegies<=1:
                    target=random.randint(1,5)
                    health_count=3
                    bonus_count=0
                    collect_vegies=random.randint(1,3)
                    vegies1=random.choice(vegies)
                    v=pygame.image.load(vegies1)
                    v=pygame.transform.scale(v,(30,30))
                    win=pygame.image.load("win.png")
                    win=pygame.transform.scale(win,(140,140))
                    ending=pygame.image.load("background.jpg")
                    screen.blit(ending,(0,0))
                    screen.blit(win,(250,300))
                    screen_font("COOL!, You completed the Level_2!",550,300,'calibri',50,(255,255,0))
                    pygame.display.update()
                    mixer.music.stop()
                    music("monkey_happy.wav",0.9)
                    time.sleep(3)
                    mixer.music.stop()
                    music("jungle_start.mp3",0.9)
                    lev=0
                    lev=levels()

            elif lev==3:
                mixer.music.stop()
                music("game_start.mp3",0.9)

                if eat==vegies1:
                    if eating_rect.colliderect(monkey):
                        pygame.draw.rect(screen,(0,255,0),monkey,2)
                        bonus_count=bonus_count+0.03
                        collect_vegies=collect_vegies-0.03
                        pygame.draw.rect(screen,(0,255,0),monkey,2)
                elif eat==fruit2: 
                    if eating_rect.colliderect(monkey):
                        pygame.draw.rect(screen,(0,255,0),monkey,2)
                        bonus_count=bonus_count+0.03
                        collect_fruits=collect_fruits-0.03
                        pygame.draw.rect(screen,(0,255,0),monkey,2)
                elif eat=="burger.png":
                    if eating_rect.colliderect(monkey):
                        pygame.draw.rect(screen,red,monkey,2)
                        health_count=health_count-0.03
                elif eat=="cake.png":
                    if eating_rect.colliderect(monkey):
                        pygame.draw.rect(screen,red,monkey,2)
                        health_count=health_count-0.03
                elif eat=="chocolates.png":
                    if eating_rect.colliderect(monkey):
                        pygame.draw.rect(screen,red,monkey,2)
                        health_count=health_count-0.03
                elif eat=="french_fries.png":
                    if eating_rect.colliderect(monkey):
                        pygame.draw.rect(screen,red,monkey,2)
                        health_count=health_count-0.03
                elif eat=="pizza.png":
                    if eating_rect.colliderect(monkey):
                        pygame.draw.rect(screen,red,monkey,2)
                        health_count=health_count-0.03 
                else:
                    if eating_rect.colliderect(monkey):
                        pygame.draw.rect(screen,(0,255,0),monkey,2)
                        bonus_count=bonus_count+0.03
                
                milisec=milisec+1
                if milisec==20:
                    sec=sec-1
                    if sec==0:
                        min=min-1
                        sec=60
                    milisec=0
                
                if bonus_count>=target:
                    if collect_fruits<=1 and collect_vegies<=1:
                        target=random.randint(1,5)
                        health_count=3
                        bonus_count=0

                        collect_fruits=random.randint(1,3)
                        fruit2=random.choice(fruits)
                        f=pygame.image.load(fruit2)
                        f=pygame.transform.scale(f,(30,30))

                        collect_vegies=random.randint(1,3)
                        vegies1=random.choice(vegies)
                        v = pygame.image.load(vegies1)
                        v=pygame.transform.scale(v,(30,30))
                        win=pygame.image.load("win.png")
                        win=pygame.transform.scale(win,(140,140))
                        ending=pygame.image.load("background.jpg")
                        screen.blit(ending,(0,0))
                        screen.blit(win,(150,300))
                        screen_font("AMAZING!, You completed the Level_3!",350,300,'calibri',50,(255,255,0))
                        pygame.display.update()
                        mixer.music.stop()
                        music("monkey_happy.wav",0.9)
                        time.sleep(3)
                        mixer.music.stop()
                        music("jungle_start.mp3",0.9)
                        lev=0
                        lev=levels()
                
                elif(min<=0):
                    ending=pygame.image.load("background.jpg")
                    ending=pygame.transform.scale(ending,(1500,1000))
                    screen.blit(ending,(0,0))
                    screen_font("Time_up OOOPS!!!!!!!",550,500,'calibri',40,(0,0,255))
                    time_up=pygame.image.load("life_end.png")
                    time_up=pygame.transform.scale(time_up,(140,140))
                    screen.blit(time_up,(350,500))
                    pygame.display.update()
                    min=2
                    sec=60
                    milisec=0
                    time.sleep(4)
                    lev=0
                    lev=level()

        screen.blit(eating,(eating_rect.x,eating_rect.y))
        
        pipes()

        if health_count<=1:
            life_end=pygame.image.load("life_end.png")
            life_end=pygame.transform.scale(life_end,(150,150))
            screen.blit(life_end,(400,400))
            screen_font("Game Over!",650,400,'calibri',100,blue)
            pygame.display.update()
            time.sleep(2)
            
            target=random.randint(1,5)
            health_count=3
            bonus_count=0
            lev=0
            collect_fruits=random.randint(1,3)
            fruit2=random.choice(fruits)
            f=pygame.image.load(fruit2)
            f=pygame.transform.scale(f,(30,30))

            collect_vegies=random.randint(1,3)
            vegies1=random.choice(vegies)
            v = pygame.image.load(vegies1)
            v=pygame.transform.scale(v,(30,30))
            lev=levels()


        pygame.display.update()
        clock.tick(60)

############### Game Specific Variable and Functions ########### 
exit= False
new =False
game_over=False

clock=Clock()
yellow=(255,255,0)
   
while not exit:
    pos=pygame.mouse.get_pos()
   
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            screen.fill(black)
            pygame.display.update()
            exit()

        elif event.type==pygame.MOUSEBUTTONDOWN:
            if((pos[0]>=542 and pos[0]<=690) and (pos[1]>=391 and pos[1]<=530)):
                l,m,r=pygame.mouse.get_pressed()
                if l:  
                    start_fun()
            elif((pos[0]>=895 and pos[0]<=1024) and (pos[1]>=399 and pos[1]<=530)):
                l,m,r=pygame.mouse.get_pressed()
                if l:
                    screen.fill(black)
                    pygame.display.update()
                    game_images("exit2.png",450,150,500,500)
                    time.sleep(2)
                    exit()
            