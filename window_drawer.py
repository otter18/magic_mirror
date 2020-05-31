import pygame
import datetime
#%% иницилизация

window = pygame.display.set_mode((900,1600),0,0)
#window = pygame.display.set_mode((900,1600),pygame.FULLSCREEN ,0)
pygame.display.set_caption("mirror v1")
screen = pygame.Surface((900,1600))

#%%
def unit():
    pygame.init() 
   
#%%
def main_loop(word = "error..."):
    time_H = datetime.datetime.today().strftime("%H:%M") 
    #datetime.datetime.now().time()
    (x,y,fontSize) = (450,50,200)
    myFont = pygame.font.SysFont("none", fontSize)
    fontColor = (255,255,255)
    bgColor = (0,0,0) 
    fontImage = myFont.render(time_H, 0, (fontColor))     
    
    
    time_s = datetime.datetime.today().strftime("%S") 

    (x_s,y_s,fontSize_s) = (810,60,100)
    myFont_s = pygame.font.SysFont("none", fontSize_s)
    
    fontImage_s = myFont_s.render(time_s, 0, (fontColor))     
    
    screen.fill(bgColor) 
    screen.blit( pygame.image.load('image/weather.png'),(0,0))
    
    screen.blit(fontImage,(x,y)) 
    screen.blit(fontImage_s,(x_s,y_s))
    
    
    #datetime.datetime.now().time()
    (x,y,fontSize) = (450,1100,85)
    myFont = pygame.font.SysFont("Courier", fontSize)
    fontColor = (200,200,200)
    
    fontImage = myFont.render(word, 0, (fontColor))  
    text_rect = fontImage.get_rect() # get text rect
    text_rect.center = (x,y)
    screen.blit(fontImage,text_rect.topleft) 
    window.blit(screen,(0,0))
    pygame.display.update() 
 
    pygame.mouse.set_visible(0)





    
     














