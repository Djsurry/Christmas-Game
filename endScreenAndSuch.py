from settings import *
import time
def tutorial():
	scene1 = pygame.image.load('Tscene1.jpg')
	scene2 = pygame.image.load('scene2.jpg')
	start = time.time()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			
		if time.time() - start < 7:

				gameDisplay.blit(scene1, [0,0])
		elif time.time() - start >= 5 and time.time() - start <= 15:
			gameDisplay.blit(scene2, [0,0])
		else:
			break
		pygame.display.update()

 
def endScreen(sleigh):
	scene1 = pygame.image.load('scene1.jpg')
	presentPic = pygame.image.load('present.png')
	exit = False
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_m:
					exit = True
		if exit:
			break
		gameDisplay.blit(scene1, [0,0])
		messageToScreen('Your score:', BLACK, ROBOTO_FONT, 300, 600)
		messageToScreen(str(sleigh.score), BLACK, ROBOTO_FONT, 410, 650)
		gameDisplay.blit(presentPic, [350, 645])
		pygame.display.update()

