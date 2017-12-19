import pygame
pygame.init()
pygame.mixer.init()
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,155, 0)
YELLOW = (255, 215, 0)
BRIGHTYELLOW = (255, 255, 0)
BLUE = (0,0, 255)
BRIGHTGREEN = (0, 255 , 0)
DARKRED = (200, 0 , 0)
BROWN = (139,69,19)
SOFTBLUE = (217,233,255)
font1 = pygame.font.SysFont(None, 50)
font2 = pygame.font.SysFont(None, 25)
TUSJ_FONT = pygame.font.Font('FFF_Tusj.ttf', 50)
ROBOTO_FONT = pygame.font.Font('Roboto-Regular.ttf', 35)
ROBOTO_FONT2 = pygame.font.Font('Roboto-Regular.ttf', 20)
def text_objects(text, color, font):
	textSurface = font.render(text, True, color)
	return textSurface,  textSurface.get_rect()
	
coalHitSound = pygame.mixer.Sound("hitsound.wav")
presentHitSound = pygame.mixer.Sound('hitpresentsound.wav')
newLifeSound = pygame.mixer.Sound('newLifesound.wav')

def centeredMessage(msg, color, font, Y):
	textSurf, textRect = text_objects(msg, color, font)
	textRect.center = (displayWidth/2), (Y)
	gameDisplay.blit(textSurf, textRect)


def messageToScreen(msg, color, font, xcor, ycor):
	screenText = font.render(msg, True, color)
	gameDisplay.blit(screenText, [xcor, ycor])

def rect(gameDisplay, color, xcor, ycor, sizex, sizey):
	pygame.draw.rect(gameDisplay, color, [xcor, ycor, sizex, sizey])

gameMusic = 'introMusic.mp3'

introMusic = 'music.mp3'

coalSound = ''

presentSound = ''

displayWidth = 500
displayHieght = 700

backgroundImage = pygame.image.load('background.png')

introBackgroundImage = pygame.image.load('introImage.jpg')

introBackgroundImageSource = 'https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&ved=0ahUKEwiSkKn3iojYAhUn7YMKHSuhBAQQjRwIBw&url=https%3A%2F%2Fthegamechanger.newgrounds.com%2Fnews%2Fpost%2F933044&psig=AOvVaw3RjO1o6gdrdGdp_lQwFfrL&ust=1513292210913927'

presentImageSource = 'https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&ved=0ahUKEwij4u7x4ITYAhXIYd8KHZd0BxUQjRwIBw&url=http%3A%2F%2Fcliparting.com%2Ffree-present-clipart-25594%2F&psig=AOvVaw2nXLMUL4TjCgtQzpvJ5zp2&ust=1513177839070315'

coalImageSource = 'https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&ved=0ahUKEwiEuf_XnIfYAhXEQ98KHdCMBO4QjRwIBw&url=http%3A%2F%2Fthelongdark.wikia.com%2Fwiki%2FCoal&psig=AOvVaw3qC0D8OxSWaemNE2Fwj8zu&ust=1513262618316877'

backgroundImageSource = 'https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&ved=0ahUKEwjohsGXnIfYAhWtS98KHd1-DQ0QjRwIBw&url=https%3A%2F%2Fbackdropoutlet.com%2Fproducts%2Fsanta-workshop-toys-christmas-sled-printed-backdrop-6356&psig=AOvVaw0XdRhArRDOr2R2a3za47K_&ust=1513262426993347'


menuImageSource = 'https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&ved=0ahUKEwju-ufck4jYAhUE94MKHTJBAA8QjRwIBw&url=https%3A%2F%2Fwww.pinterest.com%2Fpin%2F304063412316628919%2F&psig=AOvVaw2Znd5j0gWdkBJnVCp7KATi&ust=1513294569975613'

sleighImageSource = 'Avi'



gameDisplay = pygame.display.set_mode((displayWidth,displayHieght))

pygame.display.set_caption('Santa Game')
