import random, pygame
from settings import * 


class PowerUp():
	def __init__(self, type):
		self.type = type
		self.w = 50
		self.h = 50
		self.x = random.randint(0, displayWidth - self.w)
		self.y = -200
		if self.type == 'life':
			self.image = pygame.image.load('surryLife.png')
		elif self.type == 'speed':
			self.image = pygame.image.load('surrySwift.png')

	def draw(self):
		gameDisplay.blit(self.image, [self.x, self.y])

	def update(self, sleigh):
		self.yv = sleigh.constantY

		self.y += self.yv