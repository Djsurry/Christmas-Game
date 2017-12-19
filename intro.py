from settings import *
from snowFlake import *

class Text():
	def __init__(self, msg, y):
		self.y = y
		self.msg = msg
		self.yv = 2
	def update(self):
		self.y += self.yv
	def draw(self):
		centeredMessage(self.msg, BLACK, ROBOTO_FONT2, self.y)

def intro():
	
	pygame.mixer.music.load('notmusic.ogg')
	pygame.mixer.music.play(-1)
	gameType = None
	snowflakes = []
	for i in range(300):
		snowflakes.append(Snowflake())

	while True:
		for i in snowflakes:
			i.update()
		exit = False
		gameDisplay.blit(introBackgroundImage, [0, 0])
		for i in snowflakes:
			i.draw()
		centeredMessage('Welcome', BLACK, TUSJ_FONT, 75)
		centeredMessage('Click To Start', BLACK, ROBOTO_FONT, 225)
		
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				exit = True

		if exit:
			break

	
def menu2():
	pygame.mixer.music.load('notmusic.ogg')
	pygame.mixer.music.play(-1)
	image = pygame.image.load('menuImage.jpg')
	buttons = {}
	buttons['quickstart'] = Button(150, 400, 200, 50, 'Quickstart', SOFTBLUE, (192, 233, 255))
	buttons['start'] = Button(100, 300, 300, 75, 'Start', (192,216,144), (180, 199, 144))
	buttons['credits'] = Button(150, displayHieght-75, 200, 50, 'Credits', (211,211,211), (192,192,192))
	while True:
		clicked = None
		c = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				c = True
		gameDisplay.blit(image, [0,0])		
		for i in buttons:
			buttons[i].mouseIn()
			buttons[i].draw()
			if buttons[i].mouseOn:
				if c:
					clicked = i

		if clicked != None:
			if clicked == 'start':
				gameType = 1
			elif clicked == 'quickstart':
				gameType = 2
			else:
				gameType = 3
			break

		pygame.display.update()
	return gameType

def menu1():
	
	image = pygame.image.load('menuImage.jpg')
	buttons = {}
	buttons['quickstart'] = Button(150, 400, 200, 50, 'Quickstart', SOFTBLUE, (192, 233, 255))
	buttons['start'] = Button(100, 300, 300, 75, 'Start', (192,216,144), (180, 199, 144))
	buttons['credits'] = Button(150, displayHieght-75, 200, 50, 'Credits', (211,211,211), (192,192,192))
	while True:
		clicked = None
		c = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				c = True
		gameDisplay.blit(image, [0,0])		
		for i in buttons:
			buttons[i].mouseIn()
			buttons[i].draw()
			if buttons[i].mouseOn:
				if c:
					clicked = i

		if clicked != None:
			if clicked == 'start':
				gameType = 1
			elif clicked == 'quickstart':
				gameType = 2
			else:
				gameType = 3
			break

		pygame.display.update()
	return gameType
def credits():
	exit = False
	msgs = []
	msgs.append(Text('Created By David Surry', -50))
	msgs.append(Text('Using python3 with pygame and photoshop', -150))
	msgs.append(Text('I don\'t own any pictures or songs used',-250))
	msgs.append(Text('More info can be found in README.txt', -350))
	msgs.append(Text('Music by Borrtex and the United States Marine Band', -450))
	msgs.append(Text('Special Thanks to:', -550))
	msgs.append(Text('Avi - Photoshoped the icons', -650))
	msgs.append(Text('Alexandro - First high score', -750))
	msgs.append(Text('NerdBerg - "I always believed in you"', -850))
	msgs.append(Text('Stefania - Riley is called NerdBerg', -950))
	msgs.append(Text('Carson - Big Baller',-1050))
	msgs.append(Text('Olivier - Is French',-1150))
	msgs.append(Text('Dad - Inspiration for game', -1250))
	msgs.append(Text('Mum - Best Mum I\'ve ever had', -1350))

	image = pygame.image.load('menuImage.jpg')
	while True:
		if exit:
			break
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				
					exit = True

		gameDisplay.blit(image, [0,0])
		for i in msgs:
			i.update()
			i.draw()

		pygame.display.update()
	
	


