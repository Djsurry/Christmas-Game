import pygame
import time
from settings import *
pygame.init()
class Sleigh():
	def __init__(self):
		self.image = pygame.image.load('SurrySatan.png')
		self.lives = 5
		self.w = 100
		self.h = 100
		self.speed = 18
		self.x = displayWidth/2-self.w*1/2
		self.y = displayHieght -100
		self.constantY = 15
		self.start = time.time()
		self.score = 0
		self.gameOver = False
		self.xv = 0
		self.currentTimer = False
		self.time = time.time() - self.start
		self.currentPowerUpTime = 0
	def draw(self):
		gameDisplay.blit(self.image, [self.x, self.y])
		#pygame.draw.rect(gameDisplay, WHITE, [self.x, self.y, self.w, self.h])
	def update(self):
		self.hit = False
		self.time = time.time() - self.start
		if self.currentTimer:
			self.currentPowerUpTime = time.time() - self.timerStart
		for event in pygame.event.get():
			# NOTE FOR ANY PEOPLE WHO ACTUALLY LOOK AT THE SOURCE CODE OF MY TRIPLE A 
			# CHIRSTMAS GAME FOR WHATEVER STUPID REASON THIS LOOP DOES NOT GET TRIGGERED
			# SO I HAD TO GET THE KEY INPUTS IN THE MAIN FILE. IF YOU FIGURE IT OUT
			# EMAIL ME dsurry@wearelcc.ca
			if event.type == pygame.QUIT:

				pygame.quit()
				quit()
			# if event.type == pygame.KEYDOWN:
			# 	if event.key == pygame.K_LEFT:
			# 		self.xv = -10
			# 	elif event.key == pygame.K_RIGHT:
			# 		self.xv = 10
			# if event.type == pygame.KEYUP:
			# 	if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
			# 		self.xv = 0
				

		if int(self.time) > 15 and int(self.time) < 35:
			self.constantY = 20
		elif int(self.time) > 35 and int(self.time) < 50:
			self.constantY = 25
		elif int(self.time) > 50:
			self.constantY = 30

		
	
		self.x += self.xv
	def startTimer(self):
		self.timerStart = time.time()
		self.currentTimer = True
	

