import pygame
import random
from settings import *
pygame.init()
class Present():
	def __init__(self, presents, first):
		self.image = pygame.image.load('present.png')
		self.w = 35
		self.h = 35
		if first:
			self.y = -len(presents)*200 + 35
		else:
			self.y = -200
		
		self.x = random.randint(0, displayWidth-self.w)
		
	def draw(self):
		gameDisplay.blit(self.image, [self.x, self.y])
	def update(self, sleigh):
		self.yv = sleigh.constantY

		self.y += self.yv
	


