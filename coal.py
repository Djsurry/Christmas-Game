import pygame, random
from settings import *
pygame.init()
class Coal():
	def __init__(self, coals, first):
		self.w = 50 
		self.h = 50
		self.image = pygame.image.load('Coal.png')

		self.x = random.randint(0, displayWidth - self.w)
		if first:
			self.y = -len(coals)*200 + 150
		else:
			self.y = -100

	def draw(self):
		gameDisplay.blit(self.image, [self.x, self.y])

	def update(self, sleigh):
		self.yv = sleigh.constantY

		self.y += self.yv
	


