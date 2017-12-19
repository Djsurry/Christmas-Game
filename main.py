import pygame, json


from sleigh import *
from present import *
from coal import *
from intro import *
from endScreenAndSuch import *
from powerUps import *
pygame.init()

gameDisplay.fill(BLACK)

powerUps = []
presents = []

coals = []

sprites = []

gameOver = False

numOfPresents = 4

numOfcoals = 3


def oof():
	pygame.mixer.Sound.play(coalHitSound)

def presentHit():
	pygame.mixer.Sound.play(presentHitSound)

def newLife():
	pygame.mixer.Sound.play(newLifeSound)
 
def draw(sprites):
	for i in sprites:
		i.draw()
def up(presents, coals, sleigh, powerUps):
	gameOver = False
	for i in presents:
		i.update(sleigh)
	for i in coals:
		i.update(sleigh)
	for i in powerUps:
		i.update(sleigh)

	sleigh.update()
	
	for i in presents:

		if i.y > displayHieght:
			presents.remove(i)
			
		if i.x >= sleigh.x and i.x <= sleigh.x + sleigh.w:
			if i.y + i.h >=sleigh.y and i.y + i.h <= sleigh.y + sleigh.h:
				sleigh.score += 1
				presentHit()
				presents.remove(i)
		elif i.x + i.w >= sleigh.x and i.x + i.w <= sleigh.x + sleigh.w:
			if i.y + i.h >=sleigh.y and i.y + i.h <= sleigh.y + sleigh.h:
				sleigh.score += 1
				presentHit()
				presents.remove(i)

	for i in coals:
		if i.y > displayHieght:
			coals.remove(i)
			
		if i.x >= sleigh.x and i.x <= sleigh.x + sleigh.w:
			if i.y + i.h >=sleigh.y and i.y + i.h <= sleigh.y + sleigh.h:
				gameOver = True
				oof()
				coals.remove(i)
				break
			elif i.y >= sleigh.y and i.y <= sleigh.y + sleigh.h:
				gameOver = True
				oof()
				coals.remove(i)
				break

		elif i.x + i.w >= sleigh.x and i.x + i.w <= sleigh.x + sleigh.w:
			if i.y + i.h >=sleigh.y and i.y + i.h <= sleigh.y + sleigh.h:
				gameOver = True
				oof()
				coals.remove(i)
				break
			elif i.y >= sleigh.y and i.y <= sleigh.y + sleigh.h:
				gameOver = True
				oof()
				coals.remove(i)
				break
	for i in powerUps:

		if i.y > displayHieght:
	
			powerUps.remove(i)
		
		if i.x >= sleigh.x and i.x <= sleigh.x + sleigh.w:
			if i.y + i.h >=sleigh.y and i.y + i.h <= sleigh.y + sleigh.h:
				
				powerUps.remove(i)
				if i.type == 'speed':
		
					sleigh.speed = 30
					sleigh.startTimer()
				elif i.type == 'life':
					newLife()
					sleigh.lives += 1
				
			elif i.y >= sleigh.y and i.y <= sleigh.y + sleigh.h:
				powerUps.remove(i)
				if i.type == 'speed':
					sleigh.speed = 30
					sleigh.startTimer()
				elif i.type == 'life':
					newLife()
					sleigh.lives += 1

		elif i.x + i.w >= sleigh.x and i.x + i.w <= sleigh.x + sleigh.w:
			if i.y + i.h >=sleigh.y and i.y + i.h <= sleigh.y + sleigh.h:
				powerUps.remove(i)
				if i.type == 'speed':
					sleigh.speed = 30
					sleigh.startTimer()
				elif i.type == 'life':
					sleigh.lives += 1

			elif i.y >= sleigh.y and i.y <= sleigh.y + sleigh.h:
				powerUps.remove(i)
				if i.type == 'speed':
					sleigh.speed = 30
					sleigh.startTimer()
				elif i.type == 'life':
					sleigh.lives += 1

	while len(presents) < numOfPresents:
		presents.append(Present(presents, False))
	while len(coals) < numOfcoals:
		coals.append(Coal(coals, False))
	return [gameOver, presents, coals, sleigh, powerUps]
def game():

	currentTimeTested = False

	presents = []

	coals = []

	sprites = []
	possiblePowerUps = ['life', 'speed']
	powerUps = []

	gameOver = False

	numOfPresents = 4

	numOfcoals = 3

	for i in range(numOfPresents):
		presents.append(Present(presents, True))

	for i in range(numOfcoals):
		coals.append(Coal(coals, True))

	sleigh = Sleigh()
	sprites += coals
	sprites += presents
	sprites += powerUps
	sprites.append(sleigh)
	pygame.mixer.music.load('introMusic.mp3')
	pygame.mixer.music.play(-1)
	while True:
	
		if int(sleigh.time) % 5 == 0:
			if random.randint(1, 2) ==1 and not currentTimeTested:
				toadd = random.choice(possiblePowerUps)
				powerUps.append(PowerUp(toadd))
			currentTimeTested = True
			
		if currentTimeTested:
			if int(sleigh.time) % 5==1:
				currentTimeTested = False
				
		if sleigh.currentTimer:

			if sleigh.currentPowerUpTime > 10:
				
				sleigh.speed = 18		
		lostLife = False
		for event in pygame.event.get():
		
			if event.type == pygame.QUIT:

				pygame.quit()
				quit()
			# REFER TO FILE sleigh.py AS TO WHY THIS IS HERE AND NOT IN THE SLEIGH OBJECT 
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					sleigh.xv = -sleigh.speed
				elif event.key == pygame.K_RIGHT:
					sleigh.xv = sleigh.speed
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					sleigh.xv = 0
		returnVal = up(presents, coals, sleigh, powerUps)
		if returnVal[0] == True:
			lostLife = True
			
			sleigh.lives -= 1

		if sleigh.lives == 0:
			break
		presents = returnVal[1]
		coals = returnVal[2]
		sleigh = returnVal[3]
		powerUps = returnVal[4]
		sprites = []
		sprites += coals
		sprites += presents
		sprites += powerUps
		sprites.append(sleigh)
		gameDisplay.blit(backgroundImage, [0,0])

		draw(sprites)
		messageToScreen(('Score: ' + str(sleigh.score)), WHITE, font2, 0, 0)
		messageToScreen(('Lives: ' + str(sleigh.lives)), WHITE, font2, displayWidth-75, 0)

		pygame.display.update()
	return sleigh

intro()
first = True
def main(first):
	if first:
		i = menu1()
		first = False
	else:
		i = menu2()
	if i == 3:
		credits()
		main(first)
	elif i == 1:
		tutorial()
	
		sleigh = game()

		endScreen(sleigh)
		
		main(first)
	else:
		
		sleigh = game()
		endScreen(sleigh)
		
		main(first)

main(first)