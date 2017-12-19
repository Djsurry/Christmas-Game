from settings import *
import random, pygame



class Snowflake():
	def __init__(self):
		self.x = random.randint(0, displayWidth)
		self.y = random.randint(-800, 0)
		self.const = random.randint(3, 8)
	def draw(self):
		pygame.draw.circle(gameDisplay, WHITE, [self.x, self.y], 2, 0)
	def update(self):
		self.y += self.const
		if self.y > displayHieght:
			self.y = random.randint(-800, 0)


class Button():
	def __init__(self, x, y, w, h, msg, color, ccolor):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.msg = msg
		self.color = color
		self.ccolor = ccolor
		self.mouseOn = False

	def draw(self):
		if self.mouseOn:
			s = pygame.Surface((self.w,self.h))
			s.set_alpha(200)
			s.fill(self.color)
			gameDisplay.blit(s, (self.x,self.y))
			centeredMessage(self.msg, BLACK, ROBOTO_FONT2, self.y + 20)
		else:
			s = pygame.Surface((self.w,self.h))
			s.set_alpha(128)
			s.fill(self.color)
			gameDisplay.blit(s, (self.x,self.y))
			centeredMessage(self.msg, BLACK, ROBOTO_FONT2, self.y + 20)

	def mouseIn(self):
		mouse = pygame.mouse.get_pos()
		if mouse[0] >= self.x and mouse[0] <= self.x + self.w and mouse[1] >= self.y and mouse[1] <= self.y + self.h:
			self.mouseOn = True
			return True
		else:
			self.mouseOn = False
			return False
